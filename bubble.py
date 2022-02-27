a=[15,16,75,93,42,2]
print("list is ",a)
tesu=len(a)
for i in range(tesu):
    for j in range (0,tesu-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print ( "list after sorting:",a)