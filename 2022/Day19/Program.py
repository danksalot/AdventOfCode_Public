from collections import deque
import re

with open('Input') as inFile:
	lines = inFile.read().splitlines()

blueprints = []

ID = 0
ORE_ORE = 1
CLAY_ORE = 2
OBS_ORE = 3
OBS_CLAY = 4
GEO_ORE = 5
GEO_OBS = 6
GEODES = 7

for line in lines:
	blueprintId, oreBot_ore, clayBot_ore, obsBot_ore, obsBot_clay, geoBot_ore, geoBot_obsidian = map(int, re.findall(r'\d+', line))
	blueprints.append([blueprintId, oreBot_ore, clayBot_ore, obsBot_ore, obsBot_clay, geoBot_ore, geoBot_obsidian, 0])

def bfs(blueprint, timelimit):
	kyew = set()
	kyew.add((1,0,0,0,0,0,0,0))
	
	maxGeodes = 0
	for t in range(timelimit):
		nextIteration = set()
		maxGeodes = 0
		maxPossible = 0
	
		while kyew:
			oreBots, clayBots, obsBots, geoBots, ore, clay, obsidian, geodes = kyew.pop()
			newOre = ore + oreBots
			newClay = clay + clayBots
			newObs = obsidian + obsBots
			newGeodes = geodes + geoBots
			maxGeodes = max(newGeodes, maxGeodes)
			maxPossible = max(maxPossible, newGeodes + geoBots * (timelimit - 1 - t))

			nextIteration.add((oreBots, clayBots, obsBots, geoBots, newOre, newClay, newObs, newGeodes))
			if ore >= blueprint[ORE_ORE] and oreBots < max(blueprint[CLAY_ORE], blueprint[OBS_ORE], blueprint[GEO_ORE]):
				nextIteration.add((oreBots+1, clayBots, obsBots, geoBots, newOre-blueprint[ORE_ORE], newClay, newObs, newGeodes))
			if ore >= blueprint[CLAY_ORE] and clayBots < blueprint[OBS_CLAY] and obsBots < blueprint[GEO_OBS]:
				nextIteration.add((oreBots, clayBots+1, obsBots, geoBots, newOre-blueprint[CLAY_ORE], newClay, newObs, newGeodes))
			if ore >= blueprint[OBS_ORE] and clay >= blueprint[OBS_CLAY] and obsBots < blueprint[GEO_OBS]:
				nextIteration.add((oreBots, clayBots, obsBots+1, geoBots, newOre-blueprint[OBS_ORE], newClay-blueprint[OBS_CLAY], newObs, newGeodes))
			if ore >= blueprint[GEO_ORE] and obsidian >= blueprint[GEO_OBS]:
				nextIteration.add((oreBots, clayBots, obsBots, geoBots+1, newOre-blueprint[GEO_ORE], newClay, newObs-blueprint[GEO_OBS], newGeodes))

		if t < timelimit - 1:
			for state in nextIteration:
				oreBots, clayBots, obsBots, geoBots, ore, clay, obsidian, geodes = state
				if geodes + geoBots * 2 * (timelimit - 1 - t) >= maxPossible:
					kyew.add(state)
	return maxGeodes

for i in range(len(blueprints)):
	blueprints[i][GEODES] = bfs(blueprints[i], 24)

print('Part 1:', sum([b[ID] * b[GEODES] for b in blueprints]))

for i in range(3):
	blueprints[i][GEODES] = bfs(blueprints[i], 32)

print('Part 2:', blueprints[0][GEODES] * blueprints[1][GEODES] * blueprints[2][GEODES])