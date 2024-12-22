
with open('Input') as inFile:
	lines = [line.strip() for line in inFile.readlines()]

iterations = 2000
buyers = [x for x in map(int, lines)]
buyerSequences = []

def mix(value, secret):
	return value ^ secret

def prune(secret):
	return secret % 16777216

def evolve(secret):
	secret = prune(mix(secret, secret * 64))
	secret = prune(mix(secret, int(secret / 32)))
	secret = prune(mix(secret, secret * 2048))
	return secret

total = 0
for buyer in buyers:
	secret = buyer
	for i in range(iterations):
		secret = evolve(secret)
	total += secret

print('Part 1:', total)

for i, buyer in enumerate(buyers):
	sequences = {}
	secrets = [buyer]
	secrets.append(evolve(secrets[-1]))
	secrets.append(evolve(secrets[-1]))
	secrets.append(evolve(secrets[-1]))
	secrets.append(evolve(secrets[-1]))

	for j in range(iterations - 3):
		diffs = (secrets[1] % 10 - secrets[0] % 10, secrets[2] % 10 - secrets[1] % 10, secrets[3] % 10 - secrets[2] % 10, secrets[4] % 10 - secrets[3] % 10)
		if diffs not in sequences:
			sequences[diffs] = secrets[-1] % 10
		secrets.append(evolve(secrets[-1]))
		del secrets[0]

	buyerSequences.append([i, sequences])

def countBananas(sequence):
	return sum(bs[1][sequence] for bs in buyerSequences if sequence in bs[1])

best = 0
checkedSequences = set()
for bs in buyerSequences:
	for sequence in bs[1]:
		if sequence in checkedSequences:
			continue
		checkedSequences.add(sequence)
		bananas = countBananas(sequence)
		if bananas > best:
			best = bananas

print('Part 2:', best)
