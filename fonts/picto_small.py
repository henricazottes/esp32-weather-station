
class picto_small:
	def __init__(s, lcd, space=0, invert=False):
		s.lcd=lcd
		s.a={}
		s._m()
		s._space = space
		s._invert=False
	def set_space(s, space):
		s._space=space
	def set_invert(s, invert):
		s._invert=invert
	def _m(s):
		a=s.a;a[10]=s._nl;a[48]=s._48;a[49]=s._49;a[50]=s._50;a[51]=s._51;a[52]=s._52;a[53]=s._53;a[54]=s._54;a[55]=s._55;a[56]=s._56;a[57]=s._57;a[119]=s._119
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
		(x, y)=s.lcd.position();s.lcd.relativeCursorMove(-(x-1),1)
	def _48(s):
		s._p(b'\x40\x44\x08\xE0\x90\x96\x90\xE0\x08\x44')
	def _49(s):
		s._p(b'\x60\x90\x90\x94\xA0\xB8\xAA\xB8\xA0\x44')
	def _50(s):
		s._p(b'\x70\x88\x88\x98\x84\x82\x82\x92\x9C\x60')
	def _51(s):
		s._p(b'\x70\xE8\xC8\xD8\xC4\xC2\xC2\xD2\xDC\x70')
	def _52(s):
		s._p(b'\x00\x0C\x52\x12\x14\x52\x12\x12\x52\x0C')
	def _53(s):
		s._p(b'\x00\x8C\x52\x12\x94\x52\x12\x92\x52\x0C')
	def _54(s):
		s._p(b'\x80\x4C\x1E\x9E\x5C\x1E\x9E\x5E\x1E\x0C')
	def _55(s):
		s._p(b'\x80\x4C\x1E\x9E\x5C\x1E\x1E\xCE\x6E\x0C')
	def _56(s):
		s._p(b'\x00\x4C\xE2\x52\x14\x52\xE2\x52\x12\x0C')
	def _57(s):
		s._p(b'\x48\x24\x12\x12\x24\x48\x48\x24\x12\x12')
	def _119(s):
		s._p(b'\x04\x02\x09\x25\x95\x95\x25\x09\x02\x04')
	def print(s, text, x=None, y=None):
		if x is None or y is None:
			(x, y)=s.lcd.position()
		else:  
			s.lcd.position(x, y)
		for char in text:
			s.a[ord(char)]()