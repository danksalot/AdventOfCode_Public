import copy

def processRounds(monkeys, rounds, reduction):
	for i in range(rounds):
		for m in range(len(monkeys)):
			while len(monkeys[m][0]) > 0:
				monkeys[m][5] += 1
				worry = eval(str(monkeys[m][0].pop(0)) + monkeys[m][1])
				worry = eval(str(worry) + reduction)
				if eval(str(worry) + monkeys[m][2]):
					monkeys[monkeys[m][3]][0].append(worry)
				else:
					monkeys[monkeys[m][4]][0].append(worry)
	
	top2 = sorted(monkeys.items(), key=lambda x: x[1][5], reverse=True)[:2]
	topScores = [m[1][5] for m in top2]
	return topScores[0] * topScores[1]

inputMonkeys = {
	0: [[89, 73, 66, 57, 64, 80], " * 3", " % 13 == 0", 6, 2, 0],
	1: [[83, 78, 81, 55, 81, 59, 69], " + 1", " % 3 == 0", 7, 4, 0],
	2: [[76, 91, 58, 85], " * 13", " % 7 == 0", 1, 4, 0],
	3: [[71, 72, 74, 76, 68], " ** 2", " % 2 == 0", 6, 0, 0],
	4: [[98, 85, 84], " + 7", " % 19 == 0", 5, 7, 0],
	5: [[78], " + 8", " % 5 == 0", 3, 0, 0],
	6: [[86, 70, 60, 88, 88, 78, 74, 83], " + 4", " % 11 == 0", 1, 2, 0],
	7: [[81, 58], " + 5", " % 17 == 0", 3, 5, 0]
}

leastCommonMultiple = 13 * 3 * 7 * 2 * 19 * 5 * 11 * 17
print('Part 1:', processRounds(copy.deepcopy(inputMonkeys), 20, " // 3"))
print('Part 2:', processRounds(copy.deepcopy(inputMonkeys), 10000, " % " + str(leastCommonMultiple)))
