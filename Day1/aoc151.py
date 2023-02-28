#	open file
f = open("aoc151.txt")
#	read file to str
str = f.read()
#	close file
f.close

#	initialize variables
floor = 0
position = 0
total = len(str)
#	Go trough str
while(len(str)):
	#	current char of str
	# Part 1
	current = str[0]
	# remove the first char of string
	str = str[1:]
	#	see if first char up or down a floor
	if(current == '('):
		floor += 1
	if(current == ')'):
		floor -= 1
	# When Santa originally enters the basement
	# Part 2
	if(floor == -1 and position == 0):
		position = total - len(str)
#	Part 1
print("Santa will end his run on floor:\t\t",floor)
#	Part 2
print("Santa will enter the basement on position:\t",position)
	

