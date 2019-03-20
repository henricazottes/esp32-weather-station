
class Font5x8:
	def __init__(s, lcd):
		s.lcd=lcd
		s.a={}
		s._m()
		s._invert=False
	def invert(s):
		s._invert=not s._invert
	def _m(s):
		a=s.a;a[10]=s._nl;a[32]=s._32;a[33]=s._33;a[34]=s._34;a[35]=s._35;a[36]=s._36;a[37]=s._37;a[38]=s._38;a[39]=s._39;a[40]=s._40;a[41]=s._41;a[42]=s._42;a[43]=s._43;a[44]=s._44;a[45]=s._45;a[46]=s._46;a[47]=s._47;a[48]=s._48;a[49]=s._49;a[50]=s._50;a[51]=s._51;a[52]=s._52;a[53]=s._53;a[54]=s._54;a[55]=s._55;a[56]=s._56;a[57]=s._57;a[58]=s._58;a[59]=s._59;a[60]=s._60;a[61]=s._61;a[62]=s._62;a[63]=s._63;a[64]=s._64;a[65]=s._65;a[66]=s._66;a[67]=s._67;a[68]=s._68;a[69]=s._69;a[70]=s._70;a[71]=s._71;a[72]=s._72;a[73]=s._73;a[74]=s._74;a[75]=s._75;a[76]=s._76;a[77]=s._77;a[78]=s._78;a[79]=s._79;a[80]=s._80;a[81]=s._81;a[82]=s._82;a[83]=s._83;a[84]=s._84;a[85]=s._85;a[86]=s._86;a[87]=s._87;a[88]=s._88;a[89]=s._89;a[90]=s._90;a[91]=s._91;a[92]=s._92;a[93]=s._93;a[94]=s._94;a[95]=s._95;a[96]=s._96;a[97]=s._97;a[98]=s._98;a[99]=s._99;a[100]=s._100;a[101]=s._101;a[102]=s._102;a[103]=s._103;a[104]=s._104;a[105]=s._105;a[106]=s._106;a[107]=s._107;a[108]=s._108;a[109]=s._109;a[110]=s._110;a[111]=s._111;a[112]=s._112;a[113]=s._113;a[114]=s._114;a[115]=s._115;a[116]=s._116;a[117]=s._117;a[118]=s._118;a[119]=s._119;a[120]=s._120;a[121]=s._121;a[122]=s._122;a[123]=s._123;a[124]=s._124;a[125]=s._125;a[126]=s._126
	def _p(s, b):
		if s._invert:
			_b=[]
			for i, v in enumerate(b):
				_b.append(0xFF & ~v)
			b=_b
		s.lcd.data(bytearray(b))
	def _nl(s):
		(x, y)=s.lcd.position();s.lcd.relativeCursorMove(-x,1)
	def _32(s):
		s._p(b'\x00\x00\x00\x00\x00')
	def _33(s):
		s._p(b'\x00\x00\xBE\x00\x00')
	def _34(s):
		s._p(b'\x00\x0E\x00\x0E\x00')
	def _35(s):
		s._p(b'\x28\xFE\x28\xFE\x28')
	def _36(s):
		s._p(b'\x48\x54\xFE\x54\x24')
	def _37(s):
		s._p(b'\x46\x26\x10\xC8\xC4')
	def _38(s):
		s._p(b'\x6C\x92\xAA\x44\xA0')
	def _39(s):
		s._p(b'\x00\x00\x06\x00\x00')
	def _40(s):
		s._p(b'\x00\x38\x44\x82\x00')
	def _41(s):
		s._p(b'\x00\x82\x44\x38\x00')
	def _42(s):
		s._p(b'\x28\x10\x7C\x10\x28')
	def _43(s):
		s._p(b'\x10\x10\x7C\x10\x10')
	def _44(s):
		s._p(b'\x00\xA0\x60\x00\x00')
	def _45(s):
		s._p(b'\x10\x10\x10\x10\x10')
	def _46(s):
		s._p(b'\x00\xC0\xC0\x00\x00')
	def _47(s):
		s._p(b'\x40\x20\x10\x08\x04')
	def _48(s):
		s._p(b'\x7C\xA2\x92\x8A\x7C')
	def _49(s):
		s._p(b'\x00\x84\xFE\x80\x00')
	def _50(s):
		s._p(b'\x84\xC2\xA2\x92\x8C')
	def _51(s):
		s._p(b'\x42\x82\x8A\x96\x62')
	def _52(s):
		s._p(b'\x30\x28\x24\xFE\x20')
	def _53(s):
		s._p(b'\x4E\x8A\x8A\x8A\x72')
	def _54(s):
		s._p(b'\x78\x94\x92\x92\x60')
	def _55(s):
		s._p(b'\x06\xE2\x12\x0A\x06')
	def _56(s):
		s._p(b'\x6C\x92\x92\x92\x6C')
	def _57(s):
		s._p(b'\x0C\x92\x92\x52\x3C')
	def _58(s):
		s._p(b'\x00\x6C\x6C\x00\x00')
	def _59(s):
		s._p(b'\x00\xAC\x6C\x00\x00')
	def _60(s):
		s._p(b'\x00\x10\x28\x44\x00')
	def _61(s):
		s._p(b'\x28\x28\x28\x28\x28')
	def _62(s):
		s._p(b'\x00\x44\x28\x10\x00')
	def _63(s):
		s._p(b'\x04\x02\xA2\x12\x0C')
	def _64(s):
		s._p(b'\x64\x92\xF2\x82\x7C')
	def _65(s):
		s._p(b'\xFC\x22\x22\x22\xFC')
	def _66(s):
		s._p(b'\xFE\x92\x92\x92\x6C')
	def _67(s):
		s._p(b'\x7C\x82\x82\x82\x44')
	def _68(s):
		s._p(b'\xFE\x82\x82\x82\x7C')
	def _69(s):
		s._p(b'\xFE\x92\x92\x92\x82')
	def _70(s):
		s._p(b'\xFE\x12\x12\x12\x02')
	def _71(s):
		s._p(b'\x7C\x82\x82\x92\xF4')
	def _72(s):
		s._p(b'\xFE\x10\x10\x10\xFE')
	def _73(s):
		s._p(b'\x00\x82\xFE\x82\x00')
	def _74(s):
		s._p(b'\x40\x82\x82\x7E\x02')
	def _75(s):
		s._p(b'\xFE\x10\x28\x44\x82')
	def _76(s):
		s._p(b'\xFE\x80\x80\x80\x80')
	def _77(s):
		s._p(b'\xFE\x04\x08\x04\xFE')
	def _78(s):
		s._p(b'\xFE\x08\x10\x20\xFE')
	def _79(s):
		s._p(b'\x7C\x82\x82\x82\x7C')
	def _80(s):
		s._p(b'\xFE\x12\x12\x12\x0C')
	def _81(s):
		s._p(b'\x7C\x82\xA2\x42\xBC')
	def _82(s):
		s._p(b'\xFE\x12\x32\x52\x8C')
	def _83(s):
		s._p(b'\x4C\x92\x92\x92\x64')
	def _84(s):
		s._p(b'\x02\x02\xFE\x02\x02')
	def _85(s):
		s._p(b'\x7E\x80\x80\x80\x7E')
	def _86(s):
		s._p(b'\x3E\x40\x80\x40\x3E')
	def _87(s):
		s._p(b'\x7E\x80\x70\x80\x7E')
	def _88(s):
		s._p(b'\xC6\x28\x10\x28\xC6')
	def _89(s):
		s._p(b'\x0E\x10\xE0\x10\x0E')
	def _90(s):
		s._p(b'\xC2\xA2\x92\x8A\x86')
	def _91(s):
		s._p(b'\x00\xFE\x82\x82\x00')
	def _92(s):
		s._p(b'\x04\x08\x10\x20\x40')
	def _93(s):
		s._p(b'\x00\x82\x82\xFE\x00')
	def _94(s):
		s._p(b'\x08\x04\x02\x04\x08')
	def _95(s):
		s._p(b'\x80\x80\x80\x80\x80')
	def _96(s):
		s._p(b'\x00\x02\x04\x08\x00')
	def _97(s):
		s._p(b'\x40\xA8\xA8\xA8\xF0')
	def _98(s):
		s._p(b'\xFE\x90\x88\x88\x70')
	def _99(s):
		s._p(b'\x70\x88\x88\x88\x40')
	def _100(s):
		s._p(b'\x70\x88\x88\x90\xFE')
	def _101(s):
		s._p(b'\x70\xA8\xA8\xA8\x30')
	def _102(s):
		s._p(b'\x10\xFC\x12\x02\x04')
	def _103(s):
		s._p(b'\x10\xA8\xA8\xA8\x78')
	def _104(s):
		s._p(b'\xFE\x10\x08\x08\xF0')
	def _105(s):
		s._p(b'\x00\x90\xFA\x80\x00')
	def _106(s):
		s._p(b'\x00\x40\x88\x7A\x00')
	def _107(s):
		s._p(b'\xFE\x20\x50\x88\x00')
	def _108(s):
		s._p(b'\x00\x82\xFE\x80\x00')
	def _109(s):
		s._p(b'\xF8\x08\xF0\x08\xF0')
	def _110(s):
		s._p(b'\xF8\x10\x08\x08\xF0')
	def _111(s):
		s._p(b'\x70\x88\x88\x88\x70')
	def _112(s):
		s._p(b'\xF8\x28\x28\x28\x10')
	def _113(s):
		s._p(b'\x10\x28\x28\x30\xF8')
	def _114(s):
		s._p(b'\xF8\x10\x08\x08\x10')
	def _115(s):
		s._p(b'\x90\xA8\xA8\xA8\x48')
	def _116(s):
		s._p(b'\x08\x7E\x88\x80\x40')
	def _117(s):
		s._p(b'\x78\x80\x80\x40\xF8')
	def _118(s):
		s._p(b'\x38\x40\x80\x40\x38')
	def _119(s):
		s._p(b'\x78\x80\x60\x80\x78')
	def _120(s):
		s._p(b'\x88\x50\x20\x50\x88')
	def _121(s):
		s._p(b'\x18\xA0\xA0\xA0\x78')
	def _122(s):
		s._p(b'\x88\xC8\xA8\x98\x88')
	def _123(s):
		s._p(b'\x00\x10\x6C\x82\x00')
	def _124(s):
		s._p(b'\x00\x00\xFE\x00\x00')
	def _125(s):
		s._p(b'\x00\x82\x6C\x10\x00')
	def _126(s):
		s._p(b'\x20\x10\x10\x20\x10')
	def print(s, text, x=None, y=None):
		if x is None or y is None:
			(x, y)=s.lcd.position()
		else:  
			s.lcd.position(x, y)
		for char in text:
			s.a[ord(char)]()