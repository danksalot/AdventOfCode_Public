from itertools import count

lines = [line.split(': ') for line in open('Input').readlines()]
scanners = {int(pos): int(height) for pos, height in lines}

def hidden(scannerRange, layer, delay):
	return (layer + delay) % ((scanners[layer] * 2) - 2)

print 'Severity of starting at 0:', sum(layer * scanners[layer] for layer in scanners if not hidden(scanners[layer], layer, 0))
print 'Coast is clear after delaying', next(delay for delay in count() if all(hidden(scanners[layer], layer, delay) for layer in scanners)), 'picoseconds.'