
n= 3512
with open("numero1.dat","wb") as f:
    f.write(n.to_bytes(4, byteorder="little"))

with open("numero2.dat","wb") as f:
    f.write(n.to_bytes(4, byteorder="big"))
    
    
s= "Ciao"   
with open("numero3.dat","w") as f:
    f.write(s)
    
    
    
print(format(s,'2'))



def s2n(na):
    tot= 0
    for c in na:
        tot = (tot << 8)|ord(c)
    return tot


print(s2n("ciao"))