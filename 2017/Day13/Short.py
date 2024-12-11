from itertools import count

lines = [line.split(': ') for line in open('Input').readlines()]
scanners = {int(pos): int(height) for pos, height in lines}

print 'Severity of starting at 0:', sum(layer * scanners[layer] for layer in scanners if not (layer % ((scanners[layer] * 2) - 2)))
print 'Coast is clear after delaying', next(delay for delay in count() if all(((layer + delay) % ((scanners[layer] * 2) - 2)) for layer in scanners)), 'picoseconds.'