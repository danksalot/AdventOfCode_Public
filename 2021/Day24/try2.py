I[0] + 7 == I[13]
I[1] - 8 == I[12]
I[2] - 4 == I[11]
I[3] + 1 == I[6]
I[4] - 7 == I[5]
I[7] + 2 == I[8]
I[9] + 5 == I[10]

inp = provideInput()
for i in range(maxInput, 0, -1):
	if str(i).count('0') > 0:
		# print('Skipping number', i)
		continue

	currentNum = i
	if currentNum % 999 == 0:
		print('Testing number', currentNum)
	inp = provideInput()
	for instruction in instructions:		
		third = inp if len(instruction) < 3 else instruction[2]
		operation(instruction[0], instruction[1], third)
	if registers['z'] == 0:
		print('Found a valid model number:', currentNum)
		break