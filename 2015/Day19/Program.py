
with open('Input') as inFile:
	lines = inFile.readlines()

replacements = []
for line in lines:
    if line.find(" => ") != -1:
        replacements.append([line.split(" => ")[0], line.split(" => ")[1].strip()])
    elif line != "\n":
        molecule = line.strip()

molecules = set()
for replacement in replacements:
    for i in range(len(molecule)):
        if molecule[i:i+len(replacement[0])] == replacement[0]:
            newMolecule = molecule[:i] + replacement[1] + molecule[i+len(replacement[0]):]
            molecules.add(newMolecule)

print('Part 1:', len(molecules))

steps = 0
while molecule != 'e':
    for replacement in replacements:
        if molecule.find(replacement[1]) != -1:
            molecule = molecule.replace(replacement[1], replacement[0], 1)
            steps += 1
            break

print('Part 2:', steps)
