from collections import deque

ELF_ATTACK_POWER = 3

DIRECTIONS = [
    (-1,  0), #UP
    ( 0, -1), #LEFT
    ( 0,  1), #RIGHT
    ( 1,  0), #DOWN    
]

ELF_UNIT_TYPE = 'E'

class CombatEnds(Exception):
    pass

class ElfDies(Exception):
    pass

class Board:
    def __init__(self, grid, raiseElfDies):
        self.grid = grid
        self.size = len(grid)
        self.raiseElfDies = raiseElfDies
        self.units = {}
        self.ignore = {}

    def playGame(self):
        size = len(self.grid)
        for y in range(size):
            for x in range(size):
                if self.grid[y][x] in 'GE':
                    self.units[(y, x)] = Unit((y, x), self.grid[y][x])
                    self.grid[y][x] = '.'

        turns = 0
        while True:
            try:
                self.playTurn()
            except CombatEnds:
                break
            turns += 1
        
        return turns * sum(u.HP for u in self.units.values())

    def playTurn(self):
        sortedUnits = sorted(self.units.keys())
        elfDies = False
        for unitCoords in sortedUnits:
            if unitCoords in self.units:
                newUnit = self.moveUnit(self.units[unitCoords])
                self.attackWithUnit(newUnit)

        if not self.units:
            raise CombatEnds()

        return elfDies

    def moveUnit(self, unit):
        enemies = [u for u in self.units.values() if u.unitType != unit.unitType]
        otherUnits = set(self.units.keys()) - {unit.coords}

        if len(enemies) == 0:
            raise CombatEnds()

        inRange = []
        for enemy in enemies:
            inRange.extend(self.getNeighbors(enemy.coords, otherUnits))

        pathGraph = self.allShortestPaths(unit, otherUnits)
        shortestPaths = []
        for candidate in inRange:
            if candidate in pathGraph:
                path = pathGraph[candidate]
                shortestPaths.append((len(path), candidate, path))

        if len(shortestPaths) == 0:
            newUnit = unit

        else:
            bestLength, bestCandidate, bestPath = min(shortestPaths)

            if len(bestPath) == 1:
                assert bestPath[0] == unit.coords
                newUnit = unit

            else:
                self.units[bestPath[1]] = self.units[unit.coords]
                del self.units[unit.coords]
                newUnit = self.units[bestPath[1]]
                newUnit.coords = bestPath[1]

        return newUnit

    def getNeighbors(self, coords, ignore):
        y, x = coords
        neighbors = [(y + dy, x + dx) for dy, dx in DIRECTIONS]
        return [coords for coords in neighbors if self.isValidMove(coords, ignore)]

    def isValidMove(self, coords, ignore):
        y, x = coords
        return 0 <= y < self.size and 0 <= x < self.size and self.grid[y][x] == '.' and (y,x) not in ignore

    def allShortestPaths(self, unit, ignore):
        visited = {}
        q = deque()

        q.append(unit.coords)
        visited[unit.coords] = [unit.coords]

        while q:
            cur = q.popleft()
            neighbors = self.getNeighbors(cur, ignore)
            for nbr in neighbors:
                if nbr not in visited:
                    q.append(nbr)
                    visited[nbr] = visited[cur] + [nbr]

        return visited

    def attackWithUnit(self, unit):
        targets = []
        for nbr in self.getNeighbors(unit.coords, []):
            if nbr in self.units:
                neighborUnit = self.units[nbr]
                if neighborUnit.unitType != unit.unitType:
                    targets.append(neighborUnit)

        if len(targets) > 0:
            target = min(targets, key=lambda t:t.HP)
            target.HP = target.HP - unit.AP

            if target.HP <= 0:
                del self.units[target.coords]

                if target.unitType == ELF_UNIT_TYPE and self.raiseElfDies:
                    raise ElfDies()
            else:
                self.units[target.coords] = target

class Unit:
    def __init__(self, coords, unitType):
        self.coords = coords
        self.unitType = unitType
        self.AP = 3 if unitType == 'G' else ELF_ATTACK_POWER
        self.HP = 200

with open('Input') as inFile:
    lines = inFile.read().splitlines()
    board = Board([list(line) for line in lines], False)

    print('Part 1:', board.playGame())

    p = 4
    while True:
        try:
            ELF_ATTACK_POWER = p
            board = Board([list(line) for line in lines], True)
            result = board.playGame()
        except ElfDies:
            p += 1
        else:
            print('Part 2:', result)
            break
