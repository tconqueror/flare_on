import sys
res = []
for i in range(14):
    res.append(0)
res[0] = 7
res[13] = 12
filein = open("output.png","rb")
buf = []
x = filein.read(0x1000)
while x!="":
    buf.append(x)
    x = filein.read(0x1000)
filein.close()
def tostr():
    bla = []
    for i in range(len(buf)):
        for j in range(len(buf[i])):
            bla.append(buf[i][j])
    return bla
def cal(k):
    t = 0x2fd2b4
    d = 0x66ec73
    for i in range(len(k)):
        t = t^(ord(k[i]) & 0xff)
        t = (t * 0x66ec73)&0xffffffffffffffff
    return t
def change():
    for i in range(14):
        buf[i] = list(buf[i])
        buf[i][10]=chr(res[i])
        buf[i] =''.join(buf[i])
def swap():
    for i in range(7):
        if (ord(buf[i*2][0]) + ord(buf[i*2+1][0])) % 2 ==0:
            temp = buf[i*2]
            buf[i*2]= buf[i*2+1]
            buf[i*2+1]=temp
def writefile():
    fileout = open("data","wb")
    for i in range(len(buf)):
        fileout.write(bytearray(buf[i]))
    fileout.close()
def flag(d):
    if (d&0xff)-125 ==ord('F'):
        if ((d>>8)&0xff) +124 == ord('l'):
            if ((d>>16)&0xff)-0x51 == ord('a'):
                if ((d>>24)&0xff) == ord('g'):  
                    return 1
    return 0
def find1():
    for res[1] in range(52,62):
        for res[2] in range(52,62):
            for res[3] in range(52,62):
                if (res[1] **3+res[2] **3+res[3] **3)&0xff == 98:
                    for res[4] in range(52,62):
                        for res[5] in range(52,62):
                            for res[6] in range(52,62):
                                for res[7] in range(77,87):
                                    if (res[4] ** 3+res[5] ** 3+res[6] ** 3+res[7] ** 3)&0xff == 107:
                                        for res[9] in range(77,87):
                                            for res[10] in range(77,87):
                                                for res[11] in range(77,87):
                                                    for res[12] in range(34,44):
                                                        if (res[9] ** 3+res[10] ** 3+res[11] ** 3+res[12] ** 3)&0xff == 191:
                                                            for res[8] in range(77,87):
                                                                change()
                                                                d = cal(tostr())
                                                                if flag(d)==1:
                                                                    print "Done"
                                                                    swap()
                                                                    writefile()
                                                                    sys.exit()
                                                                

#######
find1()
#writefile

