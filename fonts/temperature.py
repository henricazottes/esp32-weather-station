
class Temperature:
	def __init__(s, lcd, space=0, invert=False):
		s.lcd=lcd
		s.a={}
		s._m()
		s._space = space
		s._invert=False
	def set_space(s, space):
		s._space=space
	def invert(s):
		s._invert=not s._invert
	def _m(s):
		a=s.a;a[10]=s._nl;a[39]=s._39;a[48]=s._48;a[49]=s._49;a[50]=s._50;a[51]=s._51;a[52]=s._52;a[53]=s._53;a[54]=s._54;a[55]=s._55;a[56]=s._56;a[57]=s._57;a[67]=s._67
	def _p(s, b):
		if s._invert:
			_b=[]
			for i, v in enumerate(b):
				_b.append(0xFF & ~v)
			b=_b
		s.lcd.data(bytearray(b))
		if s._space:
			s.lcd.relativeCursorMove(1,0)
	def _nl(s):
		(x, y)=s.lcd.position();s.lcd.relativeCursorMove(-x,2)
	def _39(s):
		s._p(b'\x00\x00\xF8\xFC\x8C\x8C\xFC\xF8\x00\x00');s.lcd.relativeCursorMove(-10, 1);s._p(b'\x00\x00\x00\x01\x01\x01\x01\x00\x00\x00');s.lcd.relativeCursorMove(0, -1)
	def _48(s):
		s._p(b'\xF0\xF8\x1C\x0C\x0C\x8C\xCC\xFC\xF8\xF0');s.lcd.relativeCursorMove(-10, 1);s._p(b'\x3F\x7F\xFC\xCE\xC7\xC3\xC1\xE0\x7F\x3F');s.lcd.relativeCursorMove(0, -1)
	def _49(s):
		s._p(b'\x00\x00\x30\x30\xF8\xFC\x00\x00\x00\x00');s.lcd.relativeCursorMove(-10, 1);s._p(b'\x00\x00\xC0\xC0\xFF\xFF\xC0\xC0\x00\x00');s.lcd.relativeCursorMove(0, -1)
	def _50(s):
		s._p(b'\x70\x78\x1C\x0C\x0C\x0C\x0C\x9C\xF8\xF0');s.lcd.relativeCursorMove(-10, 1);s._p(b'\xC0\xE0\xF0\xF8\xDC\xCE\xC7\xC3\xC1\xC0');s.lcd.relativeCursorMove(0, -1)
	def _51(s):
		s._p(b'\x70\x78\x1C\x0C\x0C\x0C\x0C\x9C\xF8\xF0');s.lcd.relativeCursorMove(-10, 1);s._p(b'\x38\x78\xE0\xC0\xC3\xC3\xC3\xE7\x7F\x3C');s.lcd.relativeCursorMove(0, -1)
	def _52(s):
		s._p(b'\x00\x80\xC0\xE0\x70\x38\xFC\xFC\x00\x00');s.lcd.relativeCursorMove(-10, 1);s._p(b'\x0F\x0F\x0D\x0C\x0C\x0C\xFF\xFF\x0C\x0C');s.lcd.relativeCursorMove(0, -1)
	def _53(s):
		s._p(b'\xFC\xFC\x8C\x8C\x8C\x8C\x8C\x8C\x0C\x0C');s.lcd.relativeCursorMove(-10, 1);s._p(b'\x39\x79\xE1\xC1\xC1\xC1\xC1\xE3\x7F\x3E');s.lcd.relativeCursorMove(0, -1)
	def _54(s):
		s._p(b'\xF0\xF8\x1C\x0C\x0C\x0C\x0C\x1C\x38\x30');s.lcd.relativeCursorMove(-10, 1);s._p(b'\x3F\x7F\xE6\xC3\xC3\xC3\xC3\xE7\x7E\x3C');s.lcd.relativeCursorMove(0, -1)
	def _55(s):
		s._p(b'\x3C\x3C\x0C\x0C\x0C\x0C\x8C\xCC\xFC\x7C');s.lcd.relativeCursorMove(-10, 1);s._p(b'\x00\x00\x00\xFC\xFE\x07\x03\x01\x00\x00');s.lcd.relativeCursorMove(0, -1)
	def _56(s):
		s._p(b'\xF0\xF8\x9C\x0C\x0C\x0C\x0C\x9C\xF8\xF0');s.lcd.relativeCursorMove(-10, 1);s._p(b'\x3C\x7F\xE7\xC3\xC3\xC3\xC3\xE7\x7F\x3C');s.lcd.relativeCursorMove(0, -1)
	def _57(s):
		s._p(b'\xF0\xF8\x9C\x0C\x0C\x0C\x0C\x9C\xF8\xF0');s.lcd.relativeCursorMove(-10, 1);s._p(b'\x30\x71\xE3\xC3\xC3\xC3\xC3\xE3\x7F\x3F');s.lcd.relativeCursorMove(0, -1)
	def _67(s):
		s._p(b'\xF0\xF8\x1C\x0C\x0C\x0C\x0C\x1C\x78\x70');s.lcd.relativeCursorMove(-10, 1);s._p(b'\x3F\x7F\xE0\xC0\xC0\xC0\xC0\xE0\x78\x38');s.lcd.relativeCursorMove(0, -1)
	def print(s, text, x=None, y=None):
		if x is None or y is None:
			(x, y)=s.lcd.position()
		else:  
			s.lcd.position(x, y)
		for char in text:
			s.a[ord(char)]()