serialNum = 8561

def populateGrid():
    grid = [[0 for x in range(301)] for y in range(301)]
    for x in range(1, 301):
        for y in range(1, 301):
            power = ((((x + 10) * y + serialNum) * (x + 10) // 100) % 10) - 5
            grid[y][x] = power + grid[y-1][x] + grid[y][x-1] - grid[y-1][x-1]
    return grid

def calculateBestBySize(min, max):
    grid = populateGrid()
    bestX = 0
    bestY = 0
    bestSize = 0
    bestScore = 0
    for s in range(min, max+1):
        for y in range(s, 301):
            for x in range(s, 301):
                total = grid[y][x] - grid[y-s][x] - grid[y][x-s] + grid[y-s][x-s]
                if total > bestScore:
                    bestScore = total
                    bestX = x
                    bestY = y
                    bestSize = s
    return bestX, bestY, bestSize

bestX, bestY, bestSize = calculateBestBySize(3, 3)
print('Part 1: ' + str(bestX - bestSize + 1) + ',' + str(bestY - bestSize + 1))
bestX, bestY, bestSize = calculateBestBySize(1, 20)
print('Part 2: ' + str(bestX - bestSize + 1) + ',' + str(bestY - bestSize + 1) + ',' + str(bestSize))