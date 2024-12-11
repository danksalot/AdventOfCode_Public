rules = []
allowed = 0

with open("Input") as inputFile:
	lines = inputFile.readlines()
    
for line in lines:
	lower, upper = map(int, line.split('-'))
	rules.append([lower, upper])

rules.sort()

ip = 0
while ip <= 4294967295:
	test = [rule for rule in rules if ip >= rule[0] and ip <= rule[1]]
	if len(test) == 0:
		allowed += 1
		print "Adding IP address", ip, "Currently allowed ip's:", allowed
		ip += 1
	else:
		ip = test[0][1] + 1	

print allowed