with open('Input') as inFile:
	lines = [line.rstrip() for line in inFile.readlines()]

networks = {}
for line in lines:
	pair = line.split('-')
	if pair[0] not in networks:
		networks[pair[0]] = set()
	networks[pair[0]].add(pair[1])
	if pair[1] not in networks:
		networks[pair[1]] = set()
	networks[pair[1]].add(pair[0])

trios = set()
for network in networks:
	if network[0] != 't':
		continue
	for second in networks[network]:
		for third in networks[network].intersection(networks[second]):
			trios.add(tuple(sorted([network, second, third])))

print('Part 1:', len(trios))

parties = []
for node in networks:
	nodeParties = [[node, second] for second in networks[node]]
	for nodeParty in nodeParties:	
		found = True
		while found == True:
			found = False
			prevPartySize = len(nodeParty)
			additional = []
			for cpu in nodeParty:
				if cpu == node:
					additional = networks[cpu]
				else:
					additional = [x for x in additional if x in networks[cpu]]
			for toAdd in additional:
				if toAdd not in nodeParty and all(toAdd in networks[member] for member in nodeParty):
					nodeParty.append(toAdd)
					found = True
	
	for party in nodeParties:
		parties.append(sorted(party))	

largestSize = 0
largest = ""
for party in parties:
	if largestSize <= len(party):
		largestSize = len(party)
		largest = ','.join(party)
		
print('Part 2:', largest)
