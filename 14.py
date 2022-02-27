#To make use of insertion sort.
def tesu(l):
    for a in range(0, 5):
        for b in range(a+1, 5):
            if l[a]>l[b]:
                t = l[a]
                l[a]=l[b]
            l[b]=t
        return(l)
#__main__
list = [62, 7, 9, 81, 34]
print("the elements of list are ", list)
k=tesu(list)
print("The sorted list is ", k)