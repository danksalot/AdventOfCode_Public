
with open('Input') as inFile:
	lines = [line.strip() for line in inFile.readlines()]

DIRS = [[0,1],[0,-1],[1,0],[-1,0]] # right, left, down, up
def findContiguousPlots(y, x):
	region = [[y, x]]
	i = 0
	while i < len(region):
		y, x = region[i]
		for dy, dx in DIRS:
			if y+dy < 0 or y+dy >= len(lines) or x+dx < 0 or x+dx >= len(lines[y]):
				continue
			if [y+dy, x+dx] in region:
				continue
			if lines[y+dy][x+dx] == lines[y][x]:
				region.append([y+dy, x+dx])
		i += 1
	return region

def calculateRegionPerimeter(region):
	perimeter = 0
	for y, x in region:
		for dy, dx in DIRS:
			if [y+dy, x+dx] not in region:
				perimeter += 1
	return perimeter

def countStraightSides(region):
	top = []
	bottom = []
	left = []
	right = []
	for y, x in region:
		if [y+0, x+1] not in region: # Right
			fence = [y, y+1, x]
			idxAbove = [idx for idx, vert in enumerate(right) if vert[1] == fence[0] and vert[2] == fence[2]]
			idxBelow = [idx for idx, vert in enumerate(right) if vert[0] == fence[1] and vert[2] == fence[2]]
			combined = False
			if idxAbove:
				right[idxAbove[0]][1] = fence[1]
				combined = True
			if idxBelow:
				right[idxBelow[0]][0] = fence[0]
				combined = True
			if not combined:
				right.append(fence)
		if [y+0, x-1] not in region: # Left
			fence = [y, y+1, x]
			idxAbove = [idx for idx, vert in enumerate(left) if vert[1] == fence[0] and vert[2] == fence[2]]
			idxBelow = [idx for idx, vert in enumerate(left) if vert[0] == fence[1] and vert[2] == fence[2]]			
			combined = False
			if idxAbove:
				left[idxAbove[0]][1] = fence[1]
				combined = True
			if idxBelow:
				left[idxBelow[0]][0] = fence[0]
				combined = True
			if not combined:
				left.append(fence)
		if [y+1, x+0] not in region: # Bottom
			fence = [y, x, x+1]
			idxLeft = [idx for idx, hor in enumerate(bottom) if hor[2] == fence[1] and hor[0] == fence[0]]
			idxRight = [idx for idx, hor in enumerate(bottom) if hor[1] == fence[2] and hor[0] == fence[0]]
			combined = False
			if idxLeft:
				bottom[idxLeft[0]][2] = fence[2]
				combined = True
			if idxRight:
				bottom[idxRight[0]][1] = fence[1]
				combined = True
			if not combined:
				bottom.append(fence)
		if [y-1, x+0] not in region: # Top
			fence = [y, x, x+1]
			idxLeft = [idx for idx, hor in enumerate(top) if hor[2] == fence[1] and hor[0] == fence[0]]
			idxRight = [idx for idx, hor in enumerate(top) if hor[1] == fence[2] and hor[0] == fence[0]]
			combined = False
			if idxLeft:
				top[idxLeft[0]][2] = fence[2]
				combined = True
			if idxRight:
				top[idxRight[0]][1] = fence[1]
				combined = True
			if not combined:
				top.append(fence)

	return len(top) + len(bottom) + len(left) + len(right)

regions = []
for y in range(len(lines)):
	for x in range(len(lines[y])):
		if any([y,x] in region for region in regions):
			continue
		regions.append(findContiguousPlots(y, x))

print("Part 1:", sum([len(region) * calculateRegionPerimeter(region) for region in regions]))
print("Part 2:", sum([len(region) * countStraightSides(region) for region in regions]))
