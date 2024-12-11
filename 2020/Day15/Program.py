starters = [5,2,8,16,18,0,1]
nums = {}

for i, x in enumerate(starters[:-1]):
	nums[x] = i + 1

prev = starters[-1]
current = 0
for i in range(1 + len(starters), 30000005):
	current = 0 if prev not in nums else i - 1 - nums[current]		
	nums[prev] = i - 1
	prev = current

	if i == 2020:
		print('Part 1:', current)
	if i == 30000000:
		print('Part 2:', current)
