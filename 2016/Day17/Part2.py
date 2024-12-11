import md5

def findNewPaths(path):
	doors = md5.new(path).hexdigest()[:4]
	x, y = calculatePosition(path)

	if doors[0] in ['b', 'c', 'd', 'e', 'f'] and y != 0 and path + 'U' not in pathsToTry and path + 'U' not in successfulPaths:
		pathsToTry.append(path + 'U')
	if doors[1] in ['b', 'c', 'd', 'e', 'f'] and y != 3 and path + 'D' not in pathsToTry and path + 'D' not in successfulPaths:
		pathsToTry.append(path + 'D')
	if doors[2] in ['b', 'c', 'd', 'e', 'f'] and x != 0 and path + 'L' not in pathsToTry and path + 'L' not in successfulPaths:
		pathsToTry.append(path + 'L')
	if doors[3] in ['b', 'c', 'd', 'e', 'f'] and x != 3 and path + 'R' not in pathsToTry and path + 'R' not in successfulPaths:
		pathsToTry.append(path + 'R')

def calculatePosition(path):
	x = 0 + path.count('R') - path.count('L')
	y = 0 + path.count('D') - path.count('U')
	return x, y

def checkForLongerPath(champion, challenger):
	if len(challenger) > len(champion):
		return challenger
	else:
		return champion

def standingAtVault(path):
	x, y = calculatePosition(path)
	if x == 3 and y == 3:
		successfulPaths.append(path)
		return True
	else:
		return False

pathsToTry = ["yjjvjgan"]
successfulPaths = []
longestPath = ""
chosenPath = ""
x = 0
y = 0

while len(pathsToTry) > 0:
	chosenPath = min(pathsToTry, key=len)
	if standingAtVault(chosenPath):
		longestPath = checkForLongerPath(longestPath, chosenPath)
	else:
		findNewPaths(chosenPath)
	print "Longest path length:", len(longestPath[8:]), "Paths left to check:", len(pathsToTry)
	pathsToTry.remove(chosenPath)
	
print "Longest path that ends at vault:", longestPath[8:]
print "Longest path length:", len(longestPath[8:])
