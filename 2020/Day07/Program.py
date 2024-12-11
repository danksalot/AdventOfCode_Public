def findContainers(rules, bagDesc):
	containers = []
	for rule in rules:
		if bagDesc in rules[rule]:
			containers.append(rule)
			containers.extend(findContainers(rules, rule))
	return set(containers)

def findContents(rules, bagDesc):
	return sum([rules[bagDesc][childBagDesc] * findContents(rules, childBagDesc) for childBagDesc in rules[bagDesc]]) + 1

with open('Input') as inFile:
	lines = inFile.read().splitlines()

rules = {}
for line in lines:
	parts = line.split()
	rules[parts[0] + parts[1]] = {}
	if len(parts) >= 8:
		rules[parts[0] + parts[1]][parts[5] + parts[6]] = int(parts[4])
	if len(parts) >= 12:
		rules[parts[0] + parts[1]][parts[9] + parts[10]] = int(parts[8])
	if len(parts) >= 16:
		rules[parts[0] + parts[1]][parts[13] + parts[14]] = int(parts[12])
	if len(parts) >= 20:
		rules[parts[0] + parts[1]][parts[17] + parts[18]] = int(parts[16])

print('Part 1:', len(findContainers(rules, 'shinygold')))
print('Part 2:', findContents(rules, 'shinygold') - 1)






# def findContents_verbose(rules, bagDesc):
# 	total = 1
# 	for childBagDesc in rules[bagDesc]:
# 		multiplier = rules[bagDesc][childBagDesc]
# 		total += multiplier * findContents_verbose(rules, childBagDesc)
# 	return total