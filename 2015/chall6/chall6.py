prime = 0x2214
mapp = 0x5004

def getprime(a):
    return Word(prime + a*2)

flag = []
for i in range(23):
    offset = Dword(mapp+i*4)
    #print hex(offset)
    res = 1
    for j in range(3476):
        if Word(j*2+offset)!= 0:
            res= res * (getprime(j) ** Word(j*2+offset))
    print res
    flag.append(chr(res >> 8))
    flag.append(chr(res & 0xff))
print ''.join(flag)

