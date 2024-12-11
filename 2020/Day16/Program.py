myTicket = [127,83,79,197,157,67,71,131,97,193,181,191,163,61,53,89,59,137,73,167]

def findValidFields(value):
	valid = []
	if 31 <= value <= 201 or 227 <= value <= 951:
		valid.append('departure location')
	if 49 <= value <= 885 or 892 <= value <= 961:
		valid.append('departure station')
	if 36 <= value <= 248 or 258 <= value <= 974:
		valid.append('departure platform')
	if 37 <= value <= 507 or 527 <= value <= 965:
		valid.append('departure track')
	if 37 <= value <= 331 or 351 <= value <= 970:
		valid.append('departure date')
	if 38 <= value <= 370 or 382 <= value <= 970:
		valid.append('departure time')
	if 33 <= value <= 686 or 711 <= value <= 960:
		valid.append('arrival location')
	if 46 <= value <= 753 or 775 <= value <= 953:
		valid.append('arrival station')
	if 34 <= value <= 138 or 154 <= value <= 959:
		valid.append('arrival platform')
	if 26 <= value <= 167 or 181 <= value <= 961:
		valid.append('arrival track')
	if 43 <= value <= 664 or 675 <= value <= 968:
		valid.append('class')
	if 47 <= value <= 603 or 620 <= value <= 954:
		valid.append('duration')
	if 40 <= value <= 290 or 313 <= value <= 972:
		valid.append('price')
	if 37 <= value <= 792 or 799 <= value <= 972:
		valid.append('route')
	if 32 <= value <= 97 or 115 <= value <= 954:
		valid.append('row')
	if 25 <= value <= 916 or 942 <= value <= 966:
		valid.append('seat')
	if 39 <= value <= 572 or 587 <= value <= 966:
		valid.append('train')
	if 25 <= value <= 834 or 858 <= value <= 953:
		valid.append('type')
	if 48 <= value <= 534 or 544 <= value <= 959:
		valid.append('wagon')
	if 47 <= value <= 442 or 463 <= value <= 969:
		valid.append('zone')
	return valid

with open('justTickets') as inFile:
	lines = inFile.read().splitlines()

total = 0
validTickets = []
for i, line in enumerate(lines):
	vals = [int(x) for x in line.split(',')]
	invalid = sum([val for val in vals if findValidFields(val) == []])
	total += invalid
	if invalid == 0:
		validTickets.append(vals)

print('Part 1:', total)

possibles = []
for i, field in enumerate(zip(*validTickets)):
	p = ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time', 'arrival location', 'arrival station', 'arrival platform', 'arrival track', 'class', 'duration', 'price', 'route', 'row', 'seat', 'train', 'type', 'wagon', 'zone']
	for val in field:
		p = set(p).intersection(findValidFields(val))
	if p not in possibles:
		possibles.append(p)

# # Part 2 was done by manually using this to narrow down which fields are in which positions
# neededFields = ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time']
# while len(neededFields) > 0:
# 	# print(1)
# 	for i, p in enumerate(possibles):
# 		# print(p)
# 		if len(p) == 1:
# 			# print(p)
# 			current = p
# 			field = p.pop()
# 			possibles.remove(current)
# 			for m in possibles:
# 				if field in m:
# 					m.remove(field)
			
# 			if field.startswith('departure'):
# 				print('Index:', i, 'Field:', field)
# 				neededFields.remove(field)
# 			continue


# neededFields = ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time']
# while len(neededFields) > 0:
# 	for i, x in enumerate(possibles):
# 		if len(x) == 1:
# 			if x[0].startswith('departure'):
# 				print('Found', x[1], 'at index', i)
# 				neededFields.remove(found[1])


	# found = [x for x in possibles if len(x) == 1]
	# print(found)
	# exit()
	# if found[0].startswith('departure'):
	# 	print('Found', found[1], 'at index', found[0])
	# 	neededFields.remove(found[1])

print('Part 2:', 83*157*131*163*61*137)

