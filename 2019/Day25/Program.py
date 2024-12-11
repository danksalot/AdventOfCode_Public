from myIntcode import IntcodeProcessor
from collections import deque

outputString = ""
inputString = ""
inputString += "south\n"
inputString += "south\n"
inputString += "south\n"
inputString += "south\n"
inputString += "take festive hat\n"
inputString += "north\n"
inputString += "north\n"
inputString += "north\n"
inputString += "take whirled peas\n"
inputString += "north\n"
inputString += "north\n"
inputString += "take coin\n"
inputString += "north\n"
inputString += "north\n"
inputString += "west\n"
inputString += "south\n"
inputString += "west\n"
inputString += "take mutex\n"
inputString += "west\n"
inputString += "south\n"
inputString += "east\n"
instructions = [int(x) for x in open("Input").read().split(',')]

getUserInput = lambda: input(">> ") + '\n'

Q = deque(ord(x) for x in inputString)
def localInput():
	global Q, outputString
	if len(Q) == 0:
		outputString = ""
		Q = deque(ord(x) for x in getUserInput())
	return Q.popleft()

def localOutput(value):
	global outputString
	outputString += chr(value) if value < 128 else str(value)
	# if chr(value) == "?":
	if "Analysis complete" in outputString:
		print(outputString)

vm1 = IntcodeProcessor(instructions.copy(), 'vm1')
vm1.debug = False
vm1.input = localInput
vm1.output = localOutput
vm1.suppressOutput = False
vm1.run()
