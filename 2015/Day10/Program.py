from itertools import groupby

def LookAndSay(string, iterations):
	for i in range(iterations):
		groups = groupby(string)
		result = [(char, sum(1 for c in group)) for char, group in groupby(string)]
		string = "".join("{}{}".format(count, label) for label, count in result)
	return string

print('Part 1', len(LookAndSay('3113322113', 40)))
print('Part 2', len(LookAndSay('3113322113', 50)))