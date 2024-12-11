import re

with open('Input') as inFile:
	lines = inFile.readlines()

digits = {
	"0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", 
	"6": "6", "7": "7", "8": "8", "9": "9", "one": "1", "two": "2", 
	"three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", 
	"eight": "8", "nine": "9"
}

total = 0
for line in lines:
	foundDigits = re.findall(r'\d', line)
	total += int(foundDigits[0] + foundDigits[-1])

print("Part 1:", total)

total = 0
for line in lines:
	foundDigits = [(line.find(digit), digit) for digit in digits]
	foundDigits = [d for d in foundDigits if d[0] != -1]
	foundDigits = sorted(foundDigits, key=lambda x: x[0])
	firstDigit = foundDigits[0][1]

	foundDigits = [(line.rfind(digit), digit) for digit in digits]
	foundDigits = [d for d in foundDigits if d[0] != -1]
	foundDigits = sorted(foundDigits, key=lambda x: x[0])
	lastDigit = foundDigits[-1][1]

	total += int(digits[firstDigit] + digits[lastDigit])

print("Part 2:", total)
