import pcd8544
import font5x8
import picto_small
import picto_big
import temperature
import utime
import gc
import micropython
from machine import Pin, SPI, TouchPad, Timer
from microWebCli import MicroWebCli
import wifimgr

touchMiddle = TouchPad(Pin(13))
touchLeft   = TouchPad(Pin(0))
touchRight  = TouchPad(Pin(2))

touchMiddle.config(500)
touchLeft.config(500)
touchRight.config(500)

touchPads       = [touchLeft, touchMiddle, touchRight]
touchStates     = [0,0,0]
tim = Timer(-1)

# GLOBALS

TRESHOLD    = 150
timestamp_g = 999999999
wlan        = None


# Time diff between Micropython ref (2000) and Api ref (1976)
time_diff = 946684800

# Lcd Setup
spi = SPI(1, baudrate=328125, bits=8, polarity=0, phase=1, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
spi.init()
cs = Pin(5, Pin.OUT)
dc = Pin(15, Pin.OUT)
rst = Pin(4, Pin.OUT)
bl = Pin(32, Pin.OUT, value=0)
lcd = pcd8544.PCD8544(spi, cs, dc, rst)
lcd.reset()
lcd.init()
lcd.clear()

# Font setup
font = font5x8.Font5x8(lcd, space=1)
tempFont = temperature.Temperature(lcd)
pictoBig = picto_big.picto_big(lcd)
pictoSmall = picto_small.picto_small(lcd)

# Weather id categories
categories_ids = [
    [800],                                              #very_sunny_ids
    [801],                                              #sunny_ids 
    [802],                                              #cloudy_ids 
    [803, 804],                                         #very_cloudy_ids 
    [300,310,500,520],                                  #light_rain_ids 
    [301,311,501],                                      #rain_ids 
    [302, 312, 313, 314, 321],                          #heavy_rain_ids 
    [200, 201, 202, 210, 211, 212, 221, 230, 231, 232], #thunder_ids 
    [600,601,602,611,612,615,616,620,621,622]           #snow_ids 
]

# API Setup
location = "?q=Toulouse,fr"
app_id = "" # "&appid=5eaadaddb1142fa0de056db0f11e647a" Set your app id here
base_url = "https://owm-proxy.herokuapp.com/"
weather_url = base_url + "weather" + location + app_id
forecast_url = base_url + "forecast" + location + app_id

def switchOffBl():
    bl.off()

def leftHandler():
    print("Left touched")

def rightHandler():
    print("Right touched")

def middleHandler():
    print("Middle touched")
    bl.on()
    tim.init(period=6000, mode=Timer.ONE_SHOT, callback=lambda t:bl.off())

touchHandlers   = [leftHandler, middleHandler, rightHandler]

def getWeekDay(timestamp):
    return utime.localtime(timestamp - time_diff)[6]

def getDate(timestamp):
    localtime = utime.localtime(timestamp - time_diff)
    month   = str(localtime[1])
    day     = str(localtime[2])
    month   = month if len(month) > 1 else ("0" + month)
    day     = day if len(day) > 1 else ("0" + day)
    return day + "/" + month

def getTime(timestamp):
    localtime = utime.localtime(timestamp - time_diff)
    hours   = str(localtime[3])
    mins    = str(localtime[4])
    mins    = mins if len(mins) > 1 else ("0" + mins)
    hours   = hours if len(hours) > 1 else ("0" + hours)
    return hours + ":" + mins

def getIconId(weather_id):
    icon_id = -1
    for i, category in enumerate(categories_ids):
        if weather_id in category:
            icon_id = i
            break
    return icon_id


def getWeekiconIds():
    print("Forecast url: " + forecast_url)
    result = MicroWebCli.JSONRequest(forecast_url, connTimeoutSec=15)
    week_icon_ids = [-1,-1,-1,-1,-1,-1,-1]
    for index, weather_id in enumerate(result["list"]):
        week_icon_ids[index] = getIconId(weather_id)
    return week_icon_ids

def getWeather():
    print("Weather url: " + weather_url)
    weather = {}
    result = MicroWebCli.JSONRequest(weather_url, connTimeoutSec=15)
    weather["weather_id"]   = getIconId(result['weather'])
    weather["temp"]         = int(round(result["temp"]))
    weather["dt"]           = result['dt']
    return weather

def drawWeather(weather):
    lcd.position(0,3)
    temp_s = ""
    if abs(weather['temp']) < 10:
        lcd.relativeCursorMove(10,0)
    if weather['temp'] > 0:
        lcd.relativeCursorMove(10,0)
    tempFont.print(str(weather['temp'])+"'C")
    lcd.relativeCursorMove(10,0)
    pictoBig.print(str(weather['weather_id']))
    lcd.position(20,5)
    # font.print(str(weather['min_temp'])+ " / " + str(weather['max_temp']))
    
def drawWeekDays(weekday):
    weekdayInitials = ["L", "M", "M", "J", "V", "S", "D"]
    for index, initial in enumerate(weekdayInitials):
        font.print(initial, 12*index + 5,0)
    
def drawWeekIcons(week_icon_ids, day_index):
    for index, icon_id in enumerate(week_icon_ids):
        if icon_id >= 0:
            pictoSmall.print(str(icon_id), index*12+2,1)
        else:
            font.print("-", 12*index + 5, 1)
    font.print("^", 12*day_index + 5, 2)

def drawDateAndTime(timestamp):
    date = getDate(timestamp)
    time = getTime(timestamp)
    font.print("     ", 5,5)
    font.print("     ", 55,5)
    font.print(date, 5, 5)
    font.print(time, 55, 5)

def run():
    weather         = getWeather()
    day_index       = getWeekDay(weather['dt'])
    week_icon_ids   = getWeekiconIds()
    timestamp_g     = weather['dt'] + 60*60 # French time offset

    lcd.clear()
    
    drawWeekDays(day_index)
    drawWeekIcons(week_icon_ids, day_index)
    drawDateAndTime(timestamp_g)
    drawWeather(weather)

    return timestamp_g

def displayInstructions(ssid, pwd, url):
    print("Could not initialize the network connection.")
    lcd.clear()
    font.print("1. Connect to:\n")
    font.print(ssid)
    font.print("\n2. PWD:\n" + pwd)
    font.print("\n3. Open:\n" + url)

def displaySuccess():
    lcd.clear()
    font.print("\n\nConnection Ok!")
    font.print("Weather check.", 0, 3)

def verifyWifiStatus(wlan):
    if not wlan or (not wlan.isconnected()):
        lcd.clear()
        pictoSmall.print("0", 2, 0)
        font.print(" WStation ")
        pictoSmall.print("0")
        font.print("Connecting to", 0, 2)
        font.print("wifi...", 0, 3)
        pictoSmall.print("w", 37, 5)
        wlan = wifimgr.get_connection(cb_error=displayInstructions, cb_success=displaySuccess)
        print("Waiting...")
        utime.sleep(2)
        print("Done.")

def checkTouchPads():
    for i in range(len(touchHandlers)):
        value = TRESHOLD
        # if i == 0:
            # value = touchLeft.read()
        if i == 1:
            value = touchMiddle.read()
        else:
            value = touchRight.read()
        
        if value < TRESHOLD:
            if i == 0:
                leftHandler()
            elif i == 1:
                middleHandler()
            else:
                rightHandler()

while True:
    verifyWifiStatus(wlan)
    timestamp_g = run()
    for i in range(10):
        for j in range(240):
            checkTouchPads()
            utime.sleep(0.25)
        timestamp_g += 60
        drawDateAndTime(timestamp_g)