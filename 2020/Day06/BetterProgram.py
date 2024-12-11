# adapted from Peter200lx's solution here: https://github.com/Peter200lx/advent-of-code/blob/master/2020/day06.py
# Program.py was used to complete Day06, but I wanted to practice with this to work through using * operators and set functions

with open('Input') as inFile:
	groups = inFile.read().split("\n\n")

ANSWERS = [[{c for c in person} for person in group.split("\n")] for group in groups]

print(sum(len(set.union(*g)) for g in ANSWERS))
print(sum(len(set.intersection(*g)) for g in ANSWERS))