def prime(n):
    for i in range(2,n):
        if n%i==0:
            t=0
            break
        else:
            t=1
    if t==0:
        print("no bsdk")
    elif t==1:
        print ("bsdk")
a=int(input("enter a no"))
prime(a)           


