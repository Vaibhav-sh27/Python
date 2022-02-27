def search(a,n,key):
    flag=0
    for i in range(n):
        if (a[i]==key):
            flag=1
            pos=i
            break
    if(flag==1):
        print("value found at",pos+1,"position")
    else:
        print("value not found")
n=int(input("Enter size"))
a=[]
for i in range(n):
    val=int(input("Enter no."))
    a.append(val)
key = int(input("Enter no. to search"))
search(a,n,key)
