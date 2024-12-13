
with open('Input') as inFile:
	lines = [line.strip() for line in inFile.readlines()]

buttonACost = 3
buttonBCost = 1

def calcBestButtonPushes(machine, offset):
    prizeX = machine[4] + offset
    prizeY = machine[5] + offset
    aPresses = (machine[3] * prizeX - machine[2] * prizeY) // (machine[0] * machine[3] - machine[2] * machine[1])
    bPresses = (machine[1] * prizeX - machine[0] * prizeY) // (machine[2] * machine[1] - machine[0] * machine[3])    
    if machine[0] * aPresses + machine[2] * bPresses == prizeX and machine[1] * aPresses + machine[3] * bPresses == prizeY:
        return buttonACost * aPresses + buttonBCost * bPresses
    else:
        return 0

machines = [] # [ButtonA-X, ButtonA-Y, ButtonB-X, ButtonB-Y, PrizeX, PrizeY]
for i in range(0, len(lines), 4):
	buttonA = lines[i].split(', Y+')
	buttonB = lines[i+1].split(', Y+')
	prize = lines[i+2].split(', Y=')
	machines.append([int(buttonA[0].split('X+')[-1]), int(buttonA[1]), int(buttonB[0].split('X+')[-1]), int(buttonB[1]), int(prize[0].split('X=')[-1]), int(prize[1])])

print("Part 1:", sum([calcBestButtonPushes(machine, 0) for machine in machines]))
print("Part 2:", sum([calcBestButtonPushes(machine, 10000000000000) for machine in machines]))
