import md5

starter = "iwrupvqb"

for i in range(1000000):
    m = md5.new(starter)
    m.update("%d" % (i))
    hashed = m.hexdigest()
    if hashed.startswith("00000"):
        print "%s%d produces hash value: %s" % (starter, i, hashed)
        break;
        
for i in range(10000000):
    m = md5.new(starter)
    m.update("%d" % (i))
    hashed = m.hexdigest()
    if hashed.startswith("000000"):
        print "%s%d produces hash value: %s" % (starter, i, hashed)
        break;
