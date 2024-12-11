#################### METHODS FOR PART 1 ####################
# def MoveRight(position):
# 	if position == 3 or position == 6 or position == 9:
# 		return position
# 	else:
# 		return position + 1

# def MoveLeft(position):
# 	if position == 1 or position == 4 or position == 7:
# 		return position
# 	else:
# 		return position - 1

# def MoveUp(position):
# 	if position == 1 or position == 2 or position == 3:
# 		return position
# 	else:
# 		return position - 3

# def MoveDown(position):
# 	if position == 7 or position == 8 or position == 9:
# 		return position
# 	else:
# 		return position + 3

#################### METHODS FOR PART 2 ####################
def MoveRight(position):
	if position in [1,4,9,12,13]:
		return position
	else:
		return position + 1

def MoveLeft(position):
	if position in [1,2,5,10,13]:
		return position
	else:
		return position - 1

def MoveUp(position):
	if position in [1,2,4,5,9]:
		return position
	elif position in [3,13]:
		return position - 2
	else:
		return position - 4

def MoveDown(position):
	if position in [5,9,10,12,13]:
		return position
	elif position in [1,11]:
		return position + 2
	else:
		return position + 4

position = 5

with open("Input") as inputFile:
	lines = inputFile.readlines()
    
for line in lines:
	for indeposition, char in enumerate(line):
		if char == 'R' :
			position = MoveRight(position)
		elif char == 'L' :
			position = MoveLeft(position)
		elif char == 'U' :
			position = MoveUp(position)
		elif char == 'D' :
			position = MoveDown(position)

	print position
