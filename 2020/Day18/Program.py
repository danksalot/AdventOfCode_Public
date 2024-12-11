import re

class Hack:
	def __init__(self, value):
		self.value = value
	def __add__(self, other):
		return Hack(self.value + other.value)
	def __sub__(self, other):
		return Hack(self.value * other.value)
	def __mul__(self, other):
		return Hack(self.value + other.value)

with open('Input') as inFile:
	lines = inFile.read().splitlines()

total = 0
for line in lines:
	line = re.sub(r'(\d)', r'Hack(\1)', line)
	line = line.replace('*', '-')
	total += eval(line, {'Hack': Hack}).value

print('Part 1:', total)

total = 0
for line in lines:
	line = re.sub(r'(\d)', r'Hack(\1)', line)
	line = line.replace('*', '-')
	line = line.replace('+', '*')
	total += eval(line, {'Hack': Hack}).value

print('Part 2:', total)