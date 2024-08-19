print('aoc154.py')
import hashlib

st = 'bgvyzdsv'
x = int(0)
Str = st + str(x)
# then sending to md5()
result = hashlib.md5(Str.encode())
first5 = (result.hexdigest())[:5]
while(first5 != '00000'):
	x = x+1
	Str = st + str(x)
	result = hashlib.md5(Str.encode())
	first5 = (result.hexdigest())[:5]
#	print(Str,' \t ',first5)

print(x)
print(Str,' \t ',first5)

while(first5 != '000000'):
	x = x+1
	Str = st + str(x)
	result = hashlib.md5(Str.encode())
	first5 = (result.hexdigest())[:6]
#	print(Str,' \t ',first5)

print(x)
print(Str,' \t ',first5)





