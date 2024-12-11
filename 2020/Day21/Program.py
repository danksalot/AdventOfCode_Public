from collections import defaultdict

with open('Input') as inFile:
	lines = inFile.read().splitlines()

ingredients = defaultdict(int)
allergenList = {}
for line in lines:
	parts = line[:-1].split(' (contains ')
	ingreds = parts[0].split()
	allergens = parts[1].split(', ')

	for a in allergens:
		if a in allergenList:
			allergenList[a] &= set(ingreds)
		else:
			allergenList[a] = set(ingreds)


	for i in ingreds:
		ingredients[i] += 1

risky = set([x for v in allergenList.values() for x in v])
# print(set([x for v in allergenList.values() for x in v]))
safe_words = [k for k in ingredients.keys() if k not in set(x for v in allergenList.values() for x in v)]
print('Risky', risky)
print('Safe', len(ingredients.keys() - risky))
# print(allergenList)

# print(allergenList)
# print(ingredients)
# print(safe_words)
# exit()