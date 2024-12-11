import md5

def findNewPaths(path):
	doors = md5.new(path).hexdigest()[:4]
	pathsToTry.remove(path)
	x, y = calculatePosition(path)

	if doors[0] in ['b', 'c', 'd', 'e', 'f'] and y != 0 and path + 'U' not in pathsToTry:
		pathsToTry.append(path + 'U')
	if doors[1] in ['b', 'c', 'd', 'e', 'f'] and y != 3 and path + 'D' not in pathsToTry:
		pathsToTry.append(path + 'D')
	if doors[2] in ['b', 'c', 'd', 'e', 'f'] and x != 0 and path + 'L' not in pathsToTry:
		pathsToTry.append(path + 'L')
	if doors[3] in ['b', 'c', 'd', 'e', 'f'] and x != 3 and path + 'R' not in pathsToTry:
		pathsToTry.append(path + 'R')

def calculatePosition(path):
	x = 0 + path.count('R') - path.count('L')
	y = 0 + path.count('D') - path.count('U')
	return x, y

def standingAtVault(path):
	x, y = calculatePosition(path)
	if x == 3 and y == 3:
		print "Vault Unlocked!!!  Path:", path[8:]
		return True
	else:
		return False 

pathsToTry = ["yjjvjgan"]
x = 0
y = 0
chosenPath = ""

while not standingAtVault(chosenPath) and len(pathsToTry) > 0:
	chosenPath = min(pathsToTry, key=len)
	findNewPaths(chosenPath)

