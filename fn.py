def fn(p,r,t):
    si=p*r*t/100
    return si
x=int(input("enter principle"))
y=int(input("enter rate"))
z=int(input("enter time"))
a=fn(x,y,z)
print(a)