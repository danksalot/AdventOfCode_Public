
with open('Input') as inFile:
	lines = inFile.readlines()

list1 = sorted([int(line.split('   ')[0]) for line in lines])
list2 = sorted([int(line.split('   ')[1]) for line in lines])
print("Part 1:", sum([abs(list1[i] - list2[i]) for i in range(len(list1))]))
print("Part 2:", sum([x * list2.count(x) for x in list1]))
