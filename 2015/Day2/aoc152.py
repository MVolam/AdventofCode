# Open file to File
f = open("aoc152.txt")
File = f.read()
f.close

# Enter File data split at new line
data = File.split('\n')

# initialize variables
paper = 0
ribbons = 0
value = 0

# smallest value of the three inputs
def min(lw,wh,hl):
	if(lw < wh):
		if(lw < hl):
			return lw;
		else:
			return hl;
	else:
		if(wh < hl):
			return wh;
		else :
			return hl;

# largest value of the three inputs
def max(l,w,h):
	if(l > w):
		if(l > h):
			return l;
		else:
			return h;
	else:
		if(w > h):
			return w;
		else :
			return h;

#Part 1
def wrapping(a):
	#	l = a[0],	w = a[1],	h = a[2]
	lw = int(a[0]) * int(a[1])
	wh = int(a[1]) * int(a[2])
	hl = int(a[2]) * int(a[0])
	minD = min(lw,wh,hl)
	sum = 2*(lw+wh+hl) + minD
	global paper
	paper = paper + sum

#Part 2
def ribbon(a):
	l = int(a[0])
	w = int(a[1])
	h = int(a[2])
	maxD = max(l,w,h)
	paper = 2*((l+w+h)-maxD)
	b = l*w*h
	global ribbons
	ribbons = ribbons+(paper+b)

for q in data:
	a = q.split('x')
	if(value==len(data)-2):
		break
	value = value+1
	wrapping(a)
	ribbon(a)

#	Answers are underlined
print("The elves need to buy","\u0332".join(str(paper)),"square feet of wrapping paper.")
print("The elves need to buy","\u0332".join(str(ribbons)),"square feet of wrapping paper.")


