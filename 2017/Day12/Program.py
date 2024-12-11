connectionDocs = {}
groups = []
checked = []

with open('Input') as inFile:
	for line in inFile:
		line = line.split()
		connectionDocs[int(line[0])] = [int(x.rstrip(',')) for x in line[2:]]

def findConnections(current, group):
	checked.append(current)
	for conn in connectionDocs[current]:
		if conn not in group:
			group.append(conn)
		if conn not in checked:
			findConnections(conn, group)
	return group

for i in range(len(connectionDocs)):
	for group in groups:
		if i in group:
			break
	
	else:
		groups.append(findConnections(i, [i]))

print "Programs in 0's group:", len(groups[0])
print "Independent groups:", len(groups)
