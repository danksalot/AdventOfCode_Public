from collections import Counter

with open('Input') as inFile:
	lines = inFile.readlines()

rankValues = '23456789TJQKA'

def detectHandType(hand):
	res = Counter(hand)
	if res.most_common()[0][1] == 5:
		return 7
	if res.most_common()[0][1] == 4:
		return 6
	if res.most_common()[0][1] == 3 and res.most_common()[1][1] == 2:
		return 5
	if res.most_common()[0][1] == 3:
		return 4
	if res.most_common()[0][1] == 2 and res.most_common()[1][1] == 2:
		return 3
	if res.most_common()[0][1] == 2:
		return 2
	return 1
		
def compare(hand):
	return (detectHandType(hand), [rankValues.index(c) for c in hand])

hands = []

for line in lines:
	parts = line.split()
	hands.append([parts[0], int(parts[1])])

hands.sort(key=lambda hand: compare(hand[0]))

total = 0
for i in range(len(hands)):
	total += hands[i][1] * (i + 1)

print('Part 1:', total)

rankValues2 = 'J23456789TQKA'

def detectHandType2(hand):
	res = Counter(hand)
	jokers = res['J']
	if res.most_common()[0][1] == 5:
		return 7
	if res.most_common()[0][1] == 4:
		if jokers >= 1:
			return 7
		return 6
	if res.most_common()[0][1] == 3 and res.most_common()[1][1] == 2:
		if jokers >= 2:
			return 7
		return 5
	if res.most_common()[0][1] == 3:
		if jokers >= 1:
			return 6
		return 4
	if res.most_common()[0][1] == 2 and res.most_common()[1][1] == 2:
		if jokers >= 2:
			return 6
		if jokers == 1:
			return 5
		return 3
	if res.most_common()[0][1] == 2:
		if jokers >= 2:
			return 4
		if jokers == 1:
			return 4
		return 2
	if jokers >= 1:
		return 2
	return 1

def compare2(hand):
	return (detectHandType2(hand), [rankValues2.index(c) for c in hand])

hands.sort(key=lambda hand: compare2(hand[0]))

total = 0
for i in range(len(hands)):
	total += hands[i][1] * (i + 1)

print('Part 2:', total)
