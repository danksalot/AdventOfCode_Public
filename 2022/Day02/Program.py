with open('Input') as inFile:
	lines = inFile.read().splitlines()

playScore = {'rock': 1, 'paper': 2, 'scissors': 3}
resultScore = {'lose': 0, 'draw': 3, 'win': 6}
wins = [['rock', 'paper'], ['paper', 'scissors'], ['scissors', 'rock']]
playMap = {'A': 'rock', 'B': 'paper', 'C': 'scissors', 
           'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}

score = 0
for line in lines:
	parts = line.split(' ')

	oppPlay = playMap[parts[0]]
	myPlay = playMap[parts[1]]

	score += playScore[myPlay]
	if [oppPlay, myPlay] in wins:
		score += resultScore['win']
	elif oppPlay == myPlay:
		score += resultScore['draw']

print("Part 1:", score)

resultMap = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}
calcPlay = {('rock', 'lose'):     'scissors', ('rock', 'draw'):  'rock', ('rock', 'win'): 'paper', 
            ('paper', 'lose'):    'rock', ('paper', 'draw'):     'paper', ('paper', 'win'): 'scissors', 
            ('scissors', 'lose'): 'paper', ('scissors', 'draw'): 'scissors', ('scissors', 'win'): 'rock'}

score = 0
for line in lines:
	parts = line.split(' ')
	
	oppPlay = playMap[parts[0]]
	result = resultMap[parts[1]]	
	myPlay = calcPlay[tuple([oppPlay, result])]

	score += resultScore[result]
	score += playScore[myPlay]

print("Part 2:", score)
