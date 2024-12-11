paperSum = 0
ribbonSum = 0

with open("Input") as inputFile:
    boxes = inputFile.readlines()
    
for line in boxes:
    # Get side lengths and sort smallest to largest
    box = line.split('x')
    box = [int(x) for x in box]
    box.sort()
    
    # Add the paper needed for this box - small side area + middle side area + large side area
    paperSum += (2*box[0]*box[1]) + (2*box[1]*box[2]) + (2*box[2]*box[0])
    # Add the smallest side again for extra paper
    paperSum += box[0] * box[1]

    # Add the ribbon needed for this box - perimeter of smallest side
    ribbonSum += 2*(box[0]+box[1])
    # Add volume of this box for extra ribbon
    ribbonSum += box[0]*box[1]*box[2]

print ("Paper to order:", paperSum, "square feet")
print ("Ribbon to order:", ribbonSum, "feet")
