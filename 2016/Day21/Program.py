def swapPosition(string, a, b):
	lst = list(string);
	lst[a], lst[b] = lst[b], lst[a]
	return ''.join(lst)

def swapLetters(string, a, b):
	d = {a:b, b:a}
	return ''.join(d[s] if s in d else s for s in string)

def rotate(string, direction, distance):
	if direction == "right":
		distance = -distance
	return string[distance:] + string[:distance]

def rotateByPosition(string, char):
	index = string.index(char)
	distance = 1 + index
	if index >= 4:
		distance += 1
	distance = distance % len(string)
	return rotate(string, "right", distance)

def reversePositions(string, start, end):
	return string[:start] + ''.join(reversed(string[start:end+1])) + string[end+1:]
	
def moveChar(string, start, end):
	char = string[start]
	string = string.replace(char, '')
	return string[:end] + char + string[end:]

string = "abcdefgh"
string = "ebcda"
print string

lines = ["swap position 4 with position 0","swap letter d with letter b","reverse positions 0 through 4","rotate left 1 step","move position 1 to position 4","move position 3 to position 0","rotate based on position of letter b","rotate based on position of letter d"]

# with open("Input") as inputFile:
# 	lines = inputFile.readlines()
    
for line in lines:
	print line
	line = line.split()
	if line[1] == "based":
		string = rotateByPosition(string, line[6])
	elif line[1] == "letter":
		string = swapLetters(string, line[2], line[5])
	elif line[0] == "move":
		string = moveChar(string, int(line[2]), int(line[5]))
	elif line[0] == "reverse":
		string = reversePositions(string, int(line[2]), int(line[4]))
	elif line[1] == "positions":
		string = swapPosition(string, line[2], line[5])
	elif line[0] == "rotate":
		string = rotate(string, line[1], int(line[2]))
	print string

print string