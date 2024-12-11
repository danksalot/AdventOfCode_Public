from functools import reduce
import numpy as np

with open('Input') as inFile:
	lines = inFile.read().split('\n')

modules = {}
pulses = []
highCount = 0
lowCount = 0
TYPE, DESTS, MEM = 0, 1, 2 # Module Consts
FROM, ID, VAL = 0, 1, 2 # Pulse Consts

buttonPushNum = 0

def pressButton(numTimes = 1):
	global pulses, buttonPushNum
	for i in range(numTimes):
		buttonPushNum = i + 1
		
		pulses.append(('button', 'broadcaster', False))
		while len(pulses) > 0:
			processPulse(pulses.pop(0))
		if buttonPushNum == 1000:
			print('Part 1:', highCount * lowCount)

inputsToJq = { 'lr': None, 'nl': None, 'vr': None, 'gt': None }

def processPulse(pulse):
	global highCount, lowCount, pulses, inputsToJq, buttonPushNum
	if pulse[VAL]:
		highCount += 1
	else:
		lowCount += 1
	modId = pulse[ID]
	if modId not in modules:  # output / rx
		return
	if modId == 'jq':  # only input to rx
		if pulse[VAL] == True:
			inputsToJq[pulse[FROM]] = buttonPushNum
		if None not in list(inputsToJq.values()):
			print('Part 2:', reduce(lambda x, y: np.lcm(x, y, dtype=object), list(inputsToJq.values())))
			exit()
	module = modules[modId]
	if module[TYPE] == 'broadcaster':
		for dest in module[DESTS]:
			pulses.append((modId, dest, pulse[VAL]))
	elif module[TYPE] == '%': # Flip Flop
		if not pulse[VAL]:
			module[MEM] = not module[MEM]
			for dest in module[DESTS]:
				pulses.append((modId, dest, module[MEM]))
	elif module[TYPE] == '&': # Conjunction
		module[MEM][pulse[FROM]] = pulse[VAL]
		valToSend = not all(x for x in module[MEM].values())
		for dest in module[DESTS]:
			pulses.append((modId, dest, valToSend))

# Build modules
for line in lines:
	parts = line.split(' -> ')
	destinations = parts[1].split(', ')
	if parts[0] == 'broadcaster':
		modules[parts[0]] = ['broadcaster', destinations]
	elif parts[0][0] == '%':
		modules[parts[0][1:]] = [parts[0][0], destinations, False]
	elif parts[0][0] == '&':
		modules[parts[0][1:]] = [parts[0][0], destinations, {}]
	else:
		modules[parts[0]] = ['output', [], None]

# Find input modules to conjuntion types
for modId in modules:
	if modules[modId][TYPE] == '&':
		for fromMod in modules:
			if modId in modules[fromMod][DESTS]:
				modules[modId][MEM][fromMod] = False

pressButton(10000)
