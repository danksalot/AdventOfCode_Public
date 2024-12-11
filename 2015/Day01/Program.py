string = open('Input', 'r').read()

current = 0
firstNeg = -1

for index, char in enumerate(string):
    if char == '(' :
        current += 1
    else :
        current -= 1
        if current < 0 and firstNeg == -1 :
            firstNeg = index
    
print "Part 1: ", current
print "Part 2: ", firstNeg + 1
