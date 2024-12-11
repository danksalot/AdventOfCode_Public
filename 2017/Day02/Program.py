checksum1 = 0
checksum2 = 0

with open('Input') as inFile:
	for line in inFile:
		elements = sorted([int(x) for x in line.split('\t')], reverse = True)
		
		# Part 1
		checksum1 += max(elements) - min(elements)

		# Part 2
		for index, dividend in enumerate(elements):
			for divisor in elements[index + 1:]:
				if dividend % divisor == 0:
					checksum2 += dividend / divisor
					break
			else:
				continue
			break

print "Part 1:", checksum1
print "Part 2:", checksum2