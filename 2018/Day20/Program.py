import networkx

DIRECTIONS = [
    (-1,  0), #UP
    ( 0, -1), #LEFT
    ( 0,  1), #RIGHT
    ( 1,  0), #DOWN    
]

graph = networkx.Graph()

with open('Input') as inFile:
    instructions = inFile.read()[1:-1]

openSet = {0}
groups = []
heads = {0}
tails = set()

for c in instructions:
    if c == '|':
        # an alternate: update possible ending points, and restart the group
        tails.update(openSet)
        openSet = heads
    elif c in 'NESW':
        # move in a given direction: add all edges and update our current positions
        direction = {'N': 1, 'E': 1j, 'S': -1, 'W': -1j}[c]
        graph.add_edges_from((n, n + direction) for n in openSet)
        openSet = {n + direction for n in openSet}
    elif c == '(':
        # start of group: add current positions as start of a new group
        groups.append((heads, tails))
        heads, tails = openSet, set()
    elif c == ')':
        # end of group: finish current group, add current positions as possible tails
        openSet.update(tails)
        heads, tails = groups.pop()

# find the shortest path lengths from the starting room to all other rooms
shortestPathLengths = networkx.algorithms.shortest_path_length(graph, 0)

print 'part 1:', max(shortestPathLengths.values())
print 'part 2:', sum(1 for length in shortestPathLengths.values() if length >= 1000)