grid = ['' for x in range(40)]
safeTiles = 0

with open("Input") as inputFile:
	grid[0] = "." + inputFile.readlines()[0] + "."
    
for i in range(1, 40):
	grid[i] += "."
	for j in range(1, 101):
		grid[i] += ''.join('.' if grid[i-1][j-1] == grid[i-1][j+1] else '^')
	grid[i] += "."

for row in grid:
	safeTiles += row[1:-1].count('.')

print safeTiles