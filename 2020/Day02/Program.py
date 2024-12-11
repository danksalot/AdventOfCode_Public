with open('Input') as inFile:
	lines = inFile.read().splitlines()

validCount1 = 0
validCount2 = 0

for line in lines:
	parts = line.split(' ')
	bounds = parts[0].split('-')
	lower = int(bounds[0])
	upper = int(bounds[1])
	letter = parts[1].rstrip(':')
	password = parts[2]

	count = password.count(letter)
	if count >= lower and count <= upper:
		validCount1 += 1

	if (password[lower - 1] == letter or password[upper - 1] == letter) and password[lower - 1] != password[upper - 1]:
		validCount2 += 1

print('Part 1:', validCount1)
print('Part 2:', validCount2)
