import re

def validate(key, value):
	if key == 'byr': return value.isdigit() and 1920 <= int(value) <= 2002
	if key == 'iyr': return value.isdigit() and 2010 <= int(value) <= 2020
	if key == 'eyr': return value.isdigit() and 2020 <= int(value) <= 2030
	if key == 'hcl': return re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', value)
	if key == 'ecl': return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	if key == 'pid': return value.isdigit() and len(value) == 9
	if key == 'hgt':
		measure = value[-2:]
		if measure == 'cm': return 150 <= int(value[0:-2]) <= 193
		if measure == 'in': return 59 <= int(value[0:-2]) <= 76
		return False
	return True


reqFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

with open('Input') as inFile:
	lines = inFile.read().splitlines()

passports = []
tempPassport = {}
for line in lines:
	if len(line) == 0:
		passports.append(tempPassport)
		tempPassport = {}
		continue

	for pair in line.split(' '):
		kvPair = pair.split(':')
		tempPassport[kvPair[0]] = kvPair[1]

validCount1 = 0
validCount2 = 0
for passport in passports:
	if all(x in passport for x in reqFields):
		validCount1 += 1
		if all(validate(key, passport[key]) for key in passport.keys()):
			validCount2 += 1

print('Part 1:', validCount1)
print('Part 2:', validCount2)

