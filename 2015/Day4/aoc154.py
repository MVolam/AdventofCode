print('aoc154.py')
import hashlib

#	puzzle input
st = 'bgvyzdsv'
x = int(0)
Str = st + str(x)
# then sending to md5()
result = hashlib.md5(Str.encode())
#	translates from hex to decimal
zeros = (result.hexdigest())[:5]
#	goes trough each input until the value of zeros is '00000'
while(zeros != '00000'):
	# next increment
	x = x+1
	Str = st + str(x)
	result = hashlib.md5(Str.encode())
	zeros = (result.hexdigest())[:5]

#	the awnser of part 1
print(x)
print(Str,' \t ',zeros)

#	goes trough each input until the value of zeros is '000000'
while(zeros != '000000'):
	# next increment
	x = x+1
	Str = st + str(x)
	result = hashlib.md5(Str.encode())
	zeros = (result.hexdigest())[:6]

print(x)
print(Str,' \t ',zeros)

