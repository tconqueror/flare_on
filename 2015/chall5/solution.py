#2015.5.script
import sys
input = "wycdefghijklmnoprstuvwxyz012345678"

fbs = "flarebearstare"
des = "UDYs1D7bNmdE1o3g5ms1V6RrYCVvODJF1DpxKTxAJ9xuZW=="
base = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "/" ]
# 0 8 16 24 32
flag =[]
"""
for i in range(0,len(des),4):
    target = des[i:i+4]
    for x in range(0x1000000):
        if (base[(x >> 18)&0x3f] == target[0]):
            if base[(x>>12)&0x3f] == target[1]:
                if base[(x>>6) & 0x3f] == target[2]:
                    if base[x &0x3f] == target[3]:
                        flag.append((x>>16))  
                        flag.append(((x>>8)&0xff))
                        flag.append((x &0xff))
print flag
"""
bla = [185, 220, 146, 213, 222, 193, 156, 192, 222, 212, 237, 198, 228, 196, 181, 191, 170, 209, 201, 203, 213, 161, 216, 223, 213, 211, 215, 146, 213, 218, 143, 213, 212] 
print len(bla)
def subfbs(a):
    res = []
    d = 0
    for i in range(len(a)):
        if d==len(fbs):
            d=0
        res.append(chr(a[i]-ord(fbs[d])))
        d = d+1
    return res
print ''.join(subfbs(bla))        
 
