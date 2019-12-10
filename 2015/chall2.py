base = [0xa8, 0x9a, 0x90, 0xb3, 0xb6, 0xbc, 0xb4, 0xab, 0x9d, 0xae, 0xf9, 0xb8, 0x9d, 0xb8, 0xaf, 0xba, 0xa5, 0xa5, 0xba, 0x9a, 0xbc, 0xb0, 0xa7, 0xc0, 0x8a, 0xaa, 0xae, 0xaf, 0xba, 0xa4, 0xec, 0xaa, 0xae, 0xeb, 0xad, 0xaa, 0xaf]
flag =  []
stack = []
import sys
def split_reg(reg):
    reg8h = reg >> 8
    reg8l = reg & 0xFF
    return (reg8h,reg8l)
def make_reg16(reg8h,reg8l):
    return reg8h*256 | reg8l 
def rol(val, rbit, maxbit = 8):
    return (val << rbit%maxbit) & ((1<<maxbit) - 1) | ((val & ((1<<maxbit) - 1)) >> (maxbit - (rbit%maxbit)))
bx = 0
cx = 0x25
ax = 0xff84
dx = 0
for c, i in enumerate(base):
    sax = ax
    sbx = bx
    scx = cx 
    sdx = dx
    for char in range(255):
        dx = bx 
        (dh,dl) = split_reg(dx)
        
        dx = dx & 0x3
        (dh,dl) = split_reg(dx)
        
        ax = 0x1c7
        (ah,al) =split_reg(ax)
        
        stack.append(ax)
        
        cf = 1
        
        al = char 
        ax = make_reg16(ah,al)
        
        al = al ^ 0xc7
        ax = make_reg16(ah,al)
        
        sdx = dx 
        dx = cx
        cx = sdx 
        (ch,cl) = split_reg(cx)
        (dh,dl) = split_reg(dx)
        
        ah = rol (ah,cl)
        ax = make_reg16(ah,al)
        
        al = al + ah+cf
        ax = make_reg16(ah,al)
        
        sdx = dx 
        dx = cx
        cx = sdx 
        
        (ch,cl) = split_reg(cx)
        (dh,dl) = split_reg(dx)
        
        dx = 0
        (dh,dl) = split_reg(dx)
        
        ax = ax & 0xff
        (ah,al) = split_reg(ax)
        
        bx = bx + ax 
        (bh, bl) = split_reg(bx)
        if ax == base[c]:
            #sys.stdout.write(chr(ch))
            flag.append(char)
            ax = stack.pop()
            cx-=1
            break
        else:
            #print "[KO], trying next letter..."
            # Roll back registers
            ax = sax
            bx = sbx
            cx = scx
            dx = sdx
print ''.join([chr(i) for i in flag])
