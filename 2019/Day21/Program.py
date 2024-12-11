from myIntcode import IntcodeProcessor
from collections import deque

instructions = [int(x) for x in open("Input").read().split(',')]

outputString = ""
inputString = ""
inputString += "NOT C J\n"
inputString += "AND D J\n"
inputString += "NOT A T\n"
inputString += "OR T J\n"
inputString += "WALK\n"

def reset():
	global outputString, inputString
	outputString = ""
	inputString = ""

Q = deque(ord(x) for x in inputString)
def localInput():
	return Q.popleft()

def localOutput(value):
	global outputString
	outputString += chr(value) if value < 128 else str(value)

vm1 = IntcodeProcessor(instructions.copy(), 'vm1')
vm1.debug = False
vm1.input = localInput
vm1.output = localOutput
vm1.suppressOutput = False
vm1.run()

print(outputString)

reset()

inputString += "NOT C J\n"
inputString += "AND D J\n"
inputString += "NOT H T\n"
inputString += "NOT T T\n"
inputString += "OR E T\n"
inputString += "AND T J\n"
inputString += "NOT A T\n"
inputString += "OR T J\n"
inputString += "NOT B T\n"
inputString += "NOT T T\n"
inputString += "OR E T\n"
inputString += "NOT T T\n"
inputString += "OR T J\n"
inputString += "RUN\n"

Q = deque(ord(x) for x in inputString)

vm2 = IntcodeProcessor(instructions.copy(), 'vm2')
vm2.debug = False
vm2.input = localInput
vm2.output = localOutput
vm2.suppressOutput = False
vm2.run()

print(outputString)