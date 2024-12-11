import functools

with open('Input') as inFile:
	stones = inFile.read().split(' ')

@functools.lru_cache(maxsize=None)
def blink(stoneValue, iterations):
	if iterations == 0:
		return 1
	if stoneValue == '0':
		return blink('1', iterations - 1)
	elif len(stoneValue) % 2 == 0:
		return blink(str(int(stoneValue[:len(stoneValue) // 2])), iterations - 1) + blink(str(int(stoneValue[len(stoneValue) // 2:])), iterations - 1)
	else:
		return blink(str(int(stoneValue) * 2024), iterations - 1)

print("Part 1:", sum(blink(stone, 25) for stone in stones))
print("Part 1:", sum(blink(stone, 75) for stone in stones))
