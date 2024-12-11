targetY = [y for y in range(-105,-56)]
targetX = [x for x in range(206, 251)]

# TEST
# targetY = [y for y in range(-10,-4)]
# targetX = [x for x in range(20, 31)]
# TEST

def step(vX, vY, x, y):
	x += vX
	y += vY
	if vX > 0:
		vX -= 1
	elif vX < 0:
		vX += 1
	vY -= 1

	return vX, vY, x, y

posX = 0
posY = 0
highestYToHitTarget = 0
workingCount = 0

for velocityY in range(-150, 150):
	for velocityX in range(300):
		vX = velocityX
		vY = velocityY
		posX = 0
		posY = 0
		highestY = 0
		while 1 == 1:			
			vX, vY, posX, posY = step(vX, vY, posX, posY)
			if posY > highestY:
				highestY = posY
			if posX in targetX and posY in targetY:
				# print('Made it to target! velocityX:', velocityX, 'velocityY:', velocityY)
				workingCount += 1
				if highestY > highestYToHitTarget:
					highestYToHitTarget = highestY
				break
			if posX > max(targetX) or posY < min(targetY):
				break

print('Part 1:', highestYToHitTarget)
print('Part 2:', workingCount)