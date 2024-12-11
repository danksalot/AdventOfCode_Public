import re

lenStrings = lenLiterals = lenEncodeds = 0

with open('Input') as inputFile:
    for line in inputFile:
        string = line.strip()
        lenLiterals += len(string)
        lenStrings += len(eval(string))
        lenEncodeds += len('"%s"' % re.escape(string))

print("Part 1:", lenLiterals - lenStrings)
print("Part 2:", lenEncodeds - lenLiterals)