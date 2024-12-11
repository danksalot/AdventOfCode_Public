import sys
import md5

starter = "cxdnnyjw"
password = ["_","_","_","_","_","_","_","_"]
print ''.join(password), "\r",
sys.stdout.flush()

for i in range(100000000):
    m = md5.new(starter)
    m.update("%d" % (i))
    hashed = m.hexdigest()
    if hashed.startswith("00000"):
        if hashed[5:6] in ['0','1','2','3','4','5','6','7']:
            if password[int(hashed[5:6])] == "_":
                password[int(hashed[5:6])] = hashed[6:7]
                print ''.join(password), "\r",
                sys.stdout.flush()
                if "_" not in password:
                    break;
        
print "Password:", ''.join(password)
