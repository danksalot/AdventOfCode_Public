import re
from collections import defaultdict

fabric = [[0 for i in range(1100)] for j in range(1100)]
claimIds = []
claimedCells = defaultdict(list)
overlappingClaims = []

with open('Input') as inFile:
	claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), inFile)
	for (claim, x1, y1, width, height) in claims:
		claimIds.append(claim)
		for x in range(x1, x1 + width):
			for y in range(y1, y1 + height):
				if claimedCells[(x,y)]:
					overlappingClaims.append(fabric[y][x])
					overlappingClaims.append(claim)
				claimedCells[(x,y)].append(claim)
				fabric[y][x] = claim

print('Part 1:', len([x for x in claimedCells if len(claimedCells[x]) > 1]))
print('Part 2:', [x for x in claimIds if x not in overlappingClaims][0])