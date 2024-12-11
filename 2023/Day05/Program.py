import re

with open('Input') as inFile:
	lines = inFile.readlines()

seeds = [int(s) for s in lines[0].strip().split(': ')[1].split(' ')]

def extractMap(mapLines):
	return [[int(x) for x in mapLine.strip().split(' ')] for mapLine in mapLines]

seed_to_soil = extractMap(lines[3:35])
soil_to_fertilizer = extractMap(lines[37:72])
fertilizer_to_water = extractMap(lines[74:101])
water_to_light = extractMap(lines[103:120])
light_to_temperature = extractMap(lines[122:164])
temperature_to_humidity = extractMap(lines[166:203])
humidity_to_location = extractMap(lines[205:244])

def mapToDestination(source, map):
	for m in map:
		if source >= m[1] and source <= m[1] + m[2]:
			return source + (m[0] - m[1])
	return source

def mapSeedToLocation(seed):
	soil = mapToDestination(seed, seed_to_soil)
	fertilizer = mapToDestination(soil, soil_to_fertilizer)
	water = mapToDestination(fertilizer, fertilizer_to_water)
	light = mapToDestination(water, water_to_light)
	temperature = mapToDestination(light, light_to_temperature)
	humidity = mapToDestination(temperature, temperature_to_humidity)
	return mapToDestination(humidity, humidity_to_location)

closest = [None, 99999999999]
for seed in seeds:
	location = mapSeedToLocation(seed)
	if location < closest[1]:
		closest = [seed, location]

print('Part 1:', closest[1])

closest = [None, 99999999999]
# for seedIdx in range(0, len(seeds), 2):
for seedIdx in range(10, 11):
	# for seed in range(seeds[seedIdx], seeds[seedIdx] + seeds[seedIdx + 1] + 1, 100):
	# for seed in range(seeds[seedIdx], seeds[seedIdx] + seeds[seedIdx + 1] + 1, 10):
	for seed in range(4042213707, 4042213727):
		location = mapSeedToLocation(seed)
		if location < closest[1]:
			closest = [seed, location]

print('Part 2:', closest[1])
