print('aoc155')

f = open("aoc155.txt")
File = f.read()
f.close

strings = File.split('\n')

nice = 0							# Nice strings
vowels = ['a','e','i','o','u']		# Vowels
notallow = ['ab','cd','pq','xy']	# String pathen that is not allowed

def three(string):					# Checks if there are atleast three vowels in string
	for j in range(len(string)):
		char = string[j]
		if char in vowels:
			global vowel
			vowel += 1
	if(vowel >= 3):
		return True
	return False

def double(string):					# Checks if string contains at least one letter that appears twice in a row
	for i in range(len(string)-1):
		if(string[i] == string[i+1]):
			return True
			break
	return False

def prohibit(string):				# Checks if prohibit strings are in string
	for j in range(len(string)-1):
		char = string[j]+string[j+1]
		if char in notallow:
			return False
	return True

'''
--Part One--
'''

for i in range(len(strings)):
	string = strings[i]
	vowel = 0
	if(three(string)):
		if(double(string)):
			if(prohibit(string)):
				nice += 1

print('The answer to Part One is','\u0332'.join(str(nice)),'.')

'''
--Part Two--
'''

def pair(string):					# Checks if string contains a pair of any two letters that appears at least twice
	for i in range(len(string)-1):
		j = i + 1
		try:
			pair = string[i]+string[j]
			newstring = string.replace(pair,'')
			stnum = len(string) - len(newstring)
			if stnum > 2:
				return True
		except IndexError:
			print(end='')
	return False

def iji(string):					# Checks if string contains at least one letter which repeats with exactly one letter between them
	for i in range(len(string)-2):
		try:
			if(string[i] == string[i+2]):
				return True
		except:
			print()
	return False
	
stnum = 0
num = 0

for i in range(len(strings)):
	string = strings[i]
	if (pair(string)):
		if(iji(string)):
			num += 1

print('The answer to Part Two is','\u0332'.join(str(num)),'.')

