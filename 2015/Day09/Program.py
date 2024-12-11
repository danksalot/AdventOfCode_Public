from collections import defaultdict
from itertools import permutations

distances = defaultdict(dict)

with open('Input') as inputFile:
    for line in inputFile:
    	parts = line.split()
    	distances[parts[0]][parts[2]] = int(parts[4])
    	distances[parts[2]][parts[0]] = int(parts[4])

possibleRoutes = permutations(distances.keys())

shortestDistance = None
longestDistance = None

for route in possibleRoutes:
    distance = sum(map(lambda x, y: distances[x][y], route[:-1], route[1:]))
    if shortestDistance is None or distance < shortestDistance:
        shortestDistance = distance
    if longestDistance is None or distance > longestDistance:
        longestDistance = distance

print('Part 1:', shortestDistance)
print('Part 2:', longestDistance)