
import md5

starter = "cxdnnyjw"
password = ""

for i in range(10000000):
    m = md5.new(starter)
    m.update("%d" % (i))
    hashed = m.hexdigest()
    if hashed.startswith("00000"):
        print "%s%d produces hash value: %s" % (starter, i, hashed)
        password += hashed[5:6]
        if len(password) >= 8:
            break;
        
print "Password:", password
# for i in range(10000000):
#     m = md5.new(starter)
#     m.update("%d" % (i))
#     hashed = m.hexdigest()
#     if hashed.startswith("000000"):
#         print "%s%d produces hash value: %s" % (starter, i, hashed)
#         break;