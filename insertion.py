a=eval(input("Enter list to be sorted: "))
print ("original list is ",a)
n=len(a)
for i in range (1,n):
    key=a[i]
    j=i-1
    while j>=0 and key<a[j]:
        a[j+1]=a[j]
        j=j-1
    else:
        a[j+1]=key
print("list after sorting:",a)            
