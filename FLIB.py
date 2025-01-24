import time as t
from math import *
def tmdprintf(dat, speed):
	for x in str(dat):
		print(x, end='')
		t.sleep(speed)
def tmdprint(dat1, speed1):
	for x1 in str(dat1):
		print(x1, end='')
		t.sleep(speed1)
	print('')
def JNL2Str(wut:str,ls:str):
	for x in ls:
		return (wut.join(ls))
def printf(string):
	print(string, end="")
def RposNschar(str1, c):
	lst = list(str1)
	for i in range(0, len(lst)):
		if lst[i] == lst[c]:
			a = ''.join(lst).replace(''.join(lst[c]), '')
			#if c == str() and c == float(): raise Exception('Position Input Must Be Integer Or Byte Not String, Character Or Float')
	return a 
def ReplcChar(str2, c2, rpl):
	lst2 = list(str2)
	for w in range(0, len(lst2)):
		if lst2[w] == lst2[c2]:
			a2 = ''.join(lst2).replace(''.join(lst2[c2]), rpl)
			if len(list(rpl)) > 1: raise Exception("Replace Input Must Be Character Not Integer")
	return a2
def Char(var):
	lst3 = list(var)
	if len(lst3) > 1: raise Exception('This Is Character type not Int, Float or String')
	return  ''.join(lst3)
def CharByte(var2):
	lst4 = list(str(var2))
	if len(lst4) > 1: raise Exception('This Is Character Byte type [from 1 to 9] not Int, Float or String')
	return int(''.join(lst4))
def SortStr(string):
    return ''.join(sorted(string))

def TakeChar(str3,c3):
	lst5 = list(str3)
	return ''.join(lst5[c3])
def Xrt(pw, rl):
	return pow(rl, 1/pw)
def cbrt(rl1):
	return pow(rl1, 1/3)
def str2ASCII(stri):
	for chim in stri:
		print(ord(chim),'',end='')
	print('')
def FindRplChar(string, replacein, replacewith):
	s = list(string)
	c = ""
	for cc in range(0, len(s)):
		if s[cc] == replacein:
			s[cc] = replacewith
		d = (''.join(s[cc]))
		c = c+d
	return c
	# print()
def ASCII2str(ASCII):
	ASCII1 = ASCII.split(',')
	for ASCII2 in ASCII1:
		chim = chr(int(ASCII2))
		print(chim, end='')
	print()

