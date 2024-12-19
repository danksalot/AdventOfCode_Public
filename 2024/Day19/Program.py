import functools

with open('Input') as inFile:
	lines = [line.rstrip() for line in inFile.readlines()]

towels = sorted(lines[0].split(', '), key=len, reverse=True)
patterns = lines[2:]

@functools.lru_cache(maxsize=None)
def canMakePattern(pattern):
    if not pattern:
        return True
    return any([canMakePattern(pattern[len(towel):]) for towel in towels if pattern.startswith(towel)])

@functools.lru_cache(maxsize=None)
def countOptions(pattern):
    if not pattern:
        return 1
    return sum([countOptions(pattern[len(towel):]) for towel in towels if pattern.startswith(towel)])

print('Part 1:', sum([1 for pattern in patterns if canMakePattern(pattern)]))
print('Part 2:', sum([countOptions(pattern) for pattern in patterns]))
