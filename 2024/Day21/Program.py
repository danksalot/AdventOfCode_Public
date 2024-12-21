import functools
import re

codes = [('279A','LUALUUARRADDDA'),('286A','LUAUUADRADDA'),('508A','LUUADDAUUUADDDRA'),('463A','UULLARRADADA'),('246A','LUALUARRADDA')]

arrowPadMap = {
    ('A','A'):'A',('A','U'):'LA',('A','R'):'DA',('A','D'):'LDA',('A','L'):'DLLA',
    ('U','A'):'RA',('U','U'):'A',('U','R'):'DRA',('U','D'):'DA',('U','L'):'DLA',
    ('L','A'):'RRUA',('L','U'):'RUA',('L','R'):'RRA',('L','D'):'RA',('L','L'):'A',
    ('D','A'):'URA',('D','U'):'UA',('D','R'):'RA',('D','D'):'A',('D','L'):'LA',
    ('R','A'):'UA',('R','U'):'LUA',('R','R'):'A',('R','D'):'LA',('R','L'):'LLA'
    }

@functools.lru_cache(maxsize=None)
def useArrowPad(code):
    code = 'A' + code # Start at A
    return ''.join([arrowPadMap[(code[i],code[i+1])] for i in range(len(code)-1)])

@functools.lru_cache(maxsize=None)
def pressesRequired(code, level):
    sequences = re.findall(r'[^A]*A', code)
    if level == 1:
        return sum([len(useArrowPad(sequence)) for sequence in sequences])
    else:
        return sum([pressesRequired(useArrowPad(sequence), level-1) for sequence in sequences])

print("Part 1:", sum(pressesRequired(code[1], 2) * int(code[0][:-1]) for code in codes))
print("Part 2:", sum(pressesRequired(code[1], 25) * int(code[0][:-1]) for code in codes))
