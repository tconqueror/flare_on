import sys
res = []
for i in range(14):
    res.append(0)
res[0] = 7
res[13] = 12
def find3():
    for i in range(77,87):
        for j in range(77,87):
            for k in range(77,87):
                for m in range(34,44):
                    if (i ** 3+j ** 3+k ** 3+m ** 3)&0xff == 191:
                        res[9]=i 
                        res[10]=j 
                        res[11]=k 
                        res[12]=m
                        
def find2():
    for i in range(52,62):
        for j in range(52,62):
            for k in range(52,62):
                for m in range(77,87):
                    if (i ** 3+j ** 3+k ** 3+m ** 3)&0xff == 107:
                        res[4]=i 
                        res[5]=j 
                        res[6]=k 
                        res[7]=m
                        find3()
def find1():
    for i in range(52,62):
        for j in range(52,62):
            for k in range(52,62):
                if (i **3+j **3+k **3)&0xff == 98:
                    res[1]=i 
                    res[2]=j 
                    res[3]=k 
                    find2()

find1()
find2() 
find3()
res[8]=0x4d
filein = open("output.png","rb")
buf = []
x = filein.read(0x1000)
while x!="":
    buf.append(x)
    x = filein.read(0x1000)
filein.close()

#######
for i in range(14):
    buf[i] = list(buf[i])
    buf[i][10]=chr(res[i])
    buf[i] =''.join(buf[i])
for i in range(7):
    if (ord(buf[i*2][0]) + ord(buf[i*2+1][0])) % 2 ==0:
        temp = buf[i*2]
        buf[i*2]= buf[i*2+1]
        buf[i*2+1]=temp
        print str(i*2) + str(i*2+1)

#######
fileout = open("data","wb")
for i in range(len(buf)):
    fileout.write(bytearray(buf[i]))
fileout.close()
