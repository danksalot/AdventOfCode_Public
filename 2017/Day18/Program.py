import collections
from multiprocessing import pool, Queue

with open('Input') as inFile:
    instructions = map(str.rstrip, inFile.readlines())

def runProgram(ident, inbox, outbox):
    regs = { 'a': 0, 'b': 0, 'i': 0, 'f': 0, 'p': ident }

    def getValue(v):
        try:
            return int(v)
        except ValueError:
            return regs[v]

    current = 0
    program1SendCount = 0
    played = None

    while 0 <= current < len(instructions) - 1:
        parts = instructions[current].split()
        if parts[0] == 'snd':
            played = getValue(parts[1])
            if outbox:
                outbox.put(getValue(parts[1]))
            program1SendCount += 1
        elif parts[0] == 'set':
            regs[parts[1]] = getValue(parts[2])
        elif parts[0] == 'add':
            regs[parts[1]] += getValue(parts[2])
        elif parts[0] == 'mul':
            regs[parts[1]] *= getValue(parts[2])
        elif parts[0] == 'mod':
            regs[parts[1]] %= getValue(parts[2])
        elif parts[0] == 'rcv':
            if inbox:
                regs[parts[1]] = inbox.get()
            elif regs[parts[1]] != 0:
                return played
        elif parts[0] == 'jgz':
            if getValue(parts[1]) > 0:
                current += getValue(parts[2])
                continue
        current += 1

    return program1SendCount


print 'Part1:', runProgram(0, None, None)

threadPool = pool.ThreadPool(processes=2)

queue0 = Queue()
queue1 = Queue()

result0 = threadPool.apply_async(runProgram, (0, queue0, queue1))
result1 = threadPool.apply_async(runProgram, (1, queue1, queue0))

result0.get()
print 'Part2:', result1.get()