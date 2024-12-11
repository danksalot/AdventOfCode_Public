matrix = []
width = 515
height = 515
NORTH, SOUTH, WEST, EAST = (0, -1), (0, 1), (-1, 0), (1, 0)
turn_left = { NORTH: WEST, WEST: SOUTH, SOUTH: EAST, EAST: NORTH }

INPUT_VALUE = 265149

def counter(current, x, y):
    return current + 1

def sumOfNeighbors(current, x, y):
    return max(1, sum([matrix[y-1][x-1],matrix[y-1][x],matrix[y-1][x+1],matrix[y][x-1],matrix[y][x+1],matrix[y+1][x-1],matrix[y+1][x],matrix[y+1][x+1]]))

def greaterThanOrEqualToInput(value):
    return value >= INPUT_VALUE

def manhattanDistanceToCenter(cellValue, x, y):
    return abs(abs(x) - width // 2) + abs(abs(y) - height // 2)

def returnCellValue(cellValue, x, y):
    return cellValue

def spiral(newCellValueFunction, breakOutCondition, returnFunction):
    global matrix

    # Setup initial state of matrix and set position to center
    x = width // 2
    y = height // 2
    dx, dy = NORTH
    matrix = [[0] * width for n in range(height)]
    cellValue = 0

    # Visit cells in a spiral order
    while True:
        # Set new cell value, returning if the breakout condition is met
        cellValue = newCellValueFunction(cellValue, x, y)
        if (breakOutCondition(cellValue)):
            return returnFunction(cellValue, x, y)
        matrix[y][x] = cellValue

        # Turn left if we can
        new_dx, new_dy = turn_left[dx, dy]
        new_x = x + new_dx
        new_y = y + new_dy
        if (0 <= new_x < width and 0 <= new_y < height and matrix[new_y][new_x] == 0):
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy

        # Go straight if turning left is not an option
        else:
            x, y = x + dx, y + dy

print("Part 1:", spiral(counter, greaterThanOrEqualToInput, manhattanDistanceToCenter))
print("Part 2:", spiral(sumOfNeighbors, greaterThanOrEqualToInput, returnCellValue))