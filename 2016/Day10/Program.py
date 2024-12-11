import sys

sys.setrecursionlimit(1500)

def initBot(bots, botId, value):
	if bots[botId]['chip1'] == 0:
		bots[botId]['chip1'] = value
	else:
		bots[botId]['chip2'] = value

def setValue(bots, outputs, type, Id, value):
	if type == "output":
		outputs[Id] = value
	elif bots[Id]['chip1'] == 0:
		bots[Id]['chip1'] = value
	else:
		bots[Id]['chip2'] = value
		GiveChips(bots, outputs, Id)

def setDownstream(bots, outputs, botId, lowType, lowReceiver, highType, highReceiver):
	bots[botId]["lowType"] = lowType
	bots[botId]["low"] = lowReceiver
	bots[botId]["highType"] = highType
	bots[botId]["high"] = highReceiver

def GiveChips(bots, outputs, giverId):
	giver = bots[giverId]
	if giver['chip1'] in [17, 61] and giver['chip2'] in [17, 61]:
		print "First bot to compare chips 17 and 61 was bot", giver['id']
	if giver['chip1'] < giver['chip2']:
		setValue(bots, outputs, giver['lowType'], giver['low'], giver['chip1'])
		setValue(bots, outputs, giver['highType'], giver['high'], giver['chip2'])
	else:
		setValue(bots, outputs, giver['lowType'], giver['low'], giver['chip2'])
		setValue(bots, outputs, giver['highType'], giver['high'], giver['chip1'])
	bots[giverId]['chip1'] = 0
	bots[giverId]['chip2'] = 0

bots = [{'id':x, 'chip1':0, 'chip2':0, 'highType':"", 'high':0, 'lowType':"", 'low':0} for x in range(210)]
outputs = [0 for x in range(21)]

with open("Input") as inputFile:
	lines = inputFile.readlines()
    
for line in lines:
	parts = line.split()
	if parts[0] == "value":
		initBot(bots, int(parts[5]), int(parts[1]))
	else:
		setDownstream(bots, outputs, int(parts[1]), parts[5], int(parts[6]), parts[10], int(parts[11]))

GiveChips(bots, outputs, 13)
print "Outputs:", outputs
