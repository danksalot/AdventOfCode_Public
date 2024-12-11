import functools
import heapq

@functools.lru_cache(maxsize=None)
def calculateErosion(y, x):
    if (y, x) in [(0, 0), target]:
        index = 0
    elif y == 0:
        index = (x * 16807)
    elif x == 0:
        index = (y * 48271)
    else:
        index = calculateErosion(y - 1, x) * calculateErosion(y, x - 1)
    return (index + depth) % 20183

def getRegion(position):
    y, x = position
    return calculateErosion(y, x) % 3

def getAdjacentNodes(position):
    y, x = position
    adjacentNodes = [(y - 1, x),(y + 1, x),(y, x - 1),(y, x + 1)]
    return [
        (newY, newX) for newY, newX in adjacentNodes
        if newY >= 0 and newX >= 0
    ]

def getNeighbors(node):
    position, tool = node
    neighbors = []

    for newRegion in getAdjacentNodes(position):
        nregion = getRegion(newRegion)
        if nregion != tool:
            neighbors.append((1, (newRegion, tool)))

    for newTool in range(3):
        if newTool != tool and newTool != getRegion(position):
            neighbors.append((7, (position, newTool)))

    return neighbors

def dijkstra(source, goal):
    visited = {}
    q = []
    heapq.heappush(q, (0, source))

    while q:
        cost, cur = heapq.heappop(q)
        if cur in visited:
            continue
        visited[cur] = cost
        if cur == goal:
            break
        for edgeCost, next in getNeighbors(cur):
            newCost = cost + edgeCost
            if next not in visited:
                heapq.heappush(q, (newCost, next))

    return visited[goal]

depth = 7305
targetX = 13
targetY = 734
target = (targetY, targetX)
cost = 0

for y in range(targetY+1):
    for x in range(targetX+1):
        cost += getRegion((y, x))

print('Part 1', cost)

source = ((0, 0), 1)
goal = (target, 1)
cost = dijkstra(source, goal)

print('Part 2', cost)
