def Turn(orientation, direction):
	if direction == "R":
		orientation += 1
	if direction == "L":
		orientation -= 1
	if orientation == -1:
		orientation = 3
	if orientation == 4:
		orientation = 0
	return orientation

def VisitHorizontal(oldX, newX, Y, map):
	for X in range(oldX+1, newX+1):
		if map[X][Y] == 1:
			print "Found a repeat!  X:", X, " Y:", Y
		else:
			map[X][Y] = 1

def VisitVertical(X, oldY, newY, map):
	for Y in range(oldY+1, newY+1):
		if map[X][Y] == 1:
			print "Found a repeat!  X:", X, " Y:", Y
		else:
			map[X][Y] = 1

def Move(X, Y, orientation, distance, route):
	if orientation == 0:
		VisitHorizontal(X, X+distance, Y, route)
		X += distance
	if orientation == 1:
		VisitVertical(X, Y, Y+distance, route)
		Y += distance
	if orientation == 2:
		VisitHorizontal(X, X-distance, Y, route)
		X -= distance
	if orientation == 3:
		VisitVertical(X, Y, Y-distance, route)
		Y -= distance

	return X, Y

CurrentX = 0
CurrentY = 0
CurrentOrientation = 0
route = [[0 for x in range(300)] for y in range(300)] 
route[0][0] = 1

inputArray = open('Input', 'r').read().split(", ")

for instruction in inputArray:
	CurrentOrientation = Turn(CurrentOrientation, instruction[0][0])
	CurrentX, CurrentY = Move(CurrentX, CurrentY, CurrentOrientation, int(instruction[1:]), route)

print "Manhattan Distance from start to end:", abs(CurrentX) + abs(CurrentY)
