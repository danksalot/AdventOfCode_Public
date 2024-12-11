
class Group:
	def __init__(self, unitType, units, hitPoints, weaknesses, immunities, attackPower, attackType, initiative):
		self.units = units
		self.unitType = unitType
		self.hitPoints = hitPoints
		self.weaknesses = weaknesses
		self.immunities = immunities
		self.attackPower = attackPower
		self.attackType = attackType
		self.initiative = initiative
		self.target = None

	def selectTarget(self, groups):
		if groups:
			targetCandidate = max(groups, key=lambda g:g.calculateDamage(self.effectivePower(), self.attackType))
			target = [g for g in groups if g.initiative == targetCandidate.initiative][0]
			if target.calculateDamage(self.effectivePower(), self.attackType) > 0:
				self.target = target
				return target
		self.target = None
		return None

	def attackTarget(self, groups):
		if self.target:
			damage = self.target.calculateDamage(self.effectivePower(), self.attackType)
			numUnitsKilled = int(damage / self.target.hitPoints)
			self.target.units -= numUnitsKilled
			#print(self.unitType, 'group', self.initiative, 'attacks defending group', self.target.initiative, 'killing', numUnitsKilled, 'units with', damage, 'damage leaving', self.target.units, 'units')

	def calculateDamage(self, effectivePower, attackType):
		damage = effectivePower
		if attackType in self.weaknesses:
			damage *= 2
		if attackType in self.immunities:
			damage = 0
		return damage

	def effectivePower(self):
		return max(0, self.units * self.attackPower)

def resetGroups(immuneBonus):
	return [
		Group('Immune',   76,  3032, [],                   [],                            334 + immuneBonus, 'radiation',    7),
		Group('Immune', 4749,  8117, [],                   [],                             16 + immuneBonus, 'bludgeoning', 16),
		Group('Immune', 4044,  1287, [],                   ['radiation', 'fire'],           2 + immuneBonus, 'fire',        20),
		Group('Immune', 1130, 11883, ['radiation'],        [],                             78 + immuneBonus, 'radiation',   14),
		Group('Immune', 1698,  2171, ['slashing', 'fire'], [],                             11 + immuneBonus, 'bludgeoning', 12),
		Group('Immune',  527,  1485, [],                   [],                             26 + immuneBonus, 'bludgeoning', 17),
		Group('Immune', 2415,  4291, [],                   ['radiation'],                  17 + immuneBonus, 'cold',         5),
		Group('Immune', 3266,  6166, ['radiation'],        ['cold', 'slashing'],           17 + immuneBonus, 'bludgeoning', 18),
		Group('Immune',   34,  8390, [],                   ['cold', 'fire', 'slashing'], 2311 + immuneBonus, 'cold',        10),
		Group('Immune', 3592,  5129, ['radiation'],        ['cold', 'fire'],               14 + immuneBonus, 'radiation',   11),

		Group('Infection', 3748, 11022, ['bludgeoning'],         [],                           4, 'bludgeoning',  6),
		Group('Infection', 2026, 11288, ['fire', 'slashing'],    [],                          10, 'slashing',    13),
		Group('Infection', 4076, 23997, [],                      ['cold'],                    11, 'bludgeoning', 19),
		Group('Infection', 4068, 40237, ['slashing'],            ['cold'],                    18, 'slashing',     4),
		Group('Infection', 3758, 16737, ['slashing'],            [],                           6, 'radiation',    2),
		Group('Infection', 1184, 36234, ['bludgeoning', 'fire'], ['cold'],                    60, 'radiation',    1),
		Group('Infection', 1297, 36710, [],                      ['cold'],                    47, 'fire',         3),
		Group('Infection',  781, 18035, [],                      ['bludgeoning', 'slashing'], 36, 'fire',        15),
		Group('Infection', 1491, 46329, [],                      ['slashing', 'bludgeoning'], 56, 'fire',         8),
		Group('Infection', 1267, 34832, [],                      ['cold'],                    49, 'radiation',    9)
	]

def runGame(immuneBonus):
	groups = resetGroups(immuneBonus)
	previousUnits = sum([g.units for g in groups])
	while len(set([g.unitType for g in groups])) > 1:
		#print('Starting Round')
		targeted = []		
		groups.sort(reverse = True, key=lambda g:(g.effectivePower(), g.initiative))

		# Select targets
		for group in groups:
			target = group.selectTarget([g for g in groups if g.unitType != group.unitType and g not in targeted])
			if target:
				targeted.append(target)	

		# Attack
		groups.sort(reverse = True, key=lambda g:g.initiative)		
		for group in groups:
			group.attackTarget(groups)
		
		# Clean up
		if previousUnits == sum([g.units for g in groups]):
			return None
		else:
			previousUnits = sum([g.units for g in groups])
			groups = [g for g in groups if g.units > 0]

	return groups

groups = runGame(0)
print('Part 1:', sum([g.units for g in groups]))

bonus = 1
while True:
	groups = runGame(bonus)
	if groups and groups[0].unitType == 'Immune':
		print('Part 2:', sum([g.units for g in groups]))
		exit()
	bonus += 1