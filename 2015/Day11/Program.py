inputString = "hepxcrrq"

def containsThreeAscending(lst):
	for i in range(len(lst) - 2):
		if lst[i] + 2 == lst[i+1] + 1 == lst[i+2]:
			return True
	return False

def containsTwoPairs(lst):
	i = 0
	pairs = 0
	while i < len(lst) - 1:
		if lst[i] == lst[i+1]:
			pairs += 1
			i += 1
		i += 1

	return pairs >= 2

def incrementChar(lst, idx):
	if lst[idx] == ord('z'):
		lst[idx] = ord('a')
		return incrementChar(lst, idx - 1)
	else:
		lst[idx] += 1
		return lst

def incrementString(lst):
	return incrementChar(lst, len(lst) - 1)

def findNextPassword(password):
	passwordAsList = list(map(ord, password))
	passwordAsList = incrementString(passwordAsList)
	while not containsThreeAscending(passwordAsList) or not containsTwoPairs(passwordAsList):
		passwordAsList = incrementString(passwordAsList)
	return ''.join(map(chr, passwordAsList))

firstPassword = findNextPassword(inputString)
print('Part 1:', firstPassword)

secondPassword = findNextPassword(firstPassword)
print('Part 2:', secondPassword)

