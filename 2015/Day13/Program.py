from itertools import permutations

scores = {}
bestScore = 0

def calculateScore(order):
    total = 0
    for i in range(len(order)):
        total += int(scores[order[i]][order[(i+1)%len(order)]])
        total += int(scores[order[i]][order[(i-1)%len(order)]])
    return total

with open("Input") as inFile:
    lines = inFile.readlines()

    for line in lines:
        parts = line.split()
        if parts[0] not in scores:
            scores[parts[0]] = {}
        scores[parts[0]][parts[10][:-1]] = parts[3] if parts[2] == 'gain' else int(parts[3]) * -1

    for perm in permutations(scores):
        score = calculateScore(perm)
        bestScore = max(score, bestScore)

    print("Part 1:", bestScore)

    scores["me"] = {}
    for score in scores:
        if score != "me":
            scores[score]["me"] = 0
            scores["me"][score] = 0

    bestScore = 0
    for perm in permutations(scores):
        score = calculateScore(perm)
        bestScore = max(score, bestScore)

    print("Part 2:", bestScore)