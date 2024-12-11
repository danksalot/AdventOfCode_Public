from itertools import combinations
from sympy import Symbol
from sympy import solve_poly_system

with open('Input') as inFile:
	lines = inFile.readlines()

hailstones = []
testMin = 200000000000000
testMax = 400000000000000

for line in lines:
	line = line.replace(' @', ',')
	parts = [int(x) for x in line.split(', ')]
	hailstones.append((int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4]), int(parts[5])))

collisions = 0
for pair in combinations(hailstones, 2):
	hail1 = pair[0]
	hail2 = pair[1]
	
	slope1 = hail1[4] / hail1[3]
	slope2 = hail2[4] / hail2[3]
	
	yIntercept1 = hail1[1] - slope1 * hail1[0]
	yIntercept2 = hail2[1] - slope2 * hail2[0]

	if slope1 == slope2:  # Parallel
		continue
	
	intersectX = (yIntercept2 - yIntercept1) / (slope1 - slope2)
	intersectY = slope1 * intersectX + yIntercept1
	
	hail1T = (intersectX - hail1[0]) / hail1[3]
	hail2T = (intersectX - hail2[0]) / hail2[3]
	
	if min(hail1T, hail2T) > 0 and testMin <= intersectX <= testMax and testMin <= intersectY <= testMax:
		collisions += 1

print('Part 1:', collisions)

# https://docs.sympy.org/latest/modules/solvers/solvers.html#sympy.solvers.polysys.solve_poly_system
rockX = Symbol('rockX')
rockY = Symbol('rockY')
rockZ = Symbol('rockZ')
rockDx = Symbol('rockDx')
rockDy = Symbol('rockDy')
rockDz = Symbol('rockDz')

equations = []
times = []

for hailstone in hailstones[:3]:
	hailX, hailY, hailZ, hailDx, hailDy, hailDz = hailstone
	id = str(hailX) + str(hailY) + str(hailZ)
	collisionTime = Symbol(id)  # Collision time for this particular hailstone
	
	equations.append(rockX + rockDx * collisionTime - hailX - hailDx * collisionTime)
	equations.append(rockY + rockDy * collisionTime - hailY - hailDy * collisionTime)
	equations.append(rockZ + rockDz * collisionTime - hailZ - hailDz * collisionTime)
	times.append(collisionTime)
	
throwPos = solve_poly_system(equations, *([rockX, rockY, rockZ, rockDx, rockDy, rockDz] + times))[0]
print('Part 2:', throwPos[0] + throwPos[1] + throwPos[2])