with open('Input') as inFile:
	inventory = inFile.read()

elves = sorted([sum([int(c) for c in elf.split('\n')]) for elf in inventory.split('\n\n')])

print("Part 1:", elves[-1])
print("Part 2:", sum(elves[-3:]))