#Deletion of an element from a sorted linear list.
def Bsearch(AR, item):
    beg = 0
    last = len(AR)-1
    while(beg<= last):
        mid = (beg+last)//2
        if (item == AR[mid]):
            return mid
        elif (item>AR[mid]):
            beg = mid+1
        else:
            last = mid-1
    else:
        return False
#__main__
myList = [10, 20, 30, 40, 50, 60, 70]
print("The list in sorted is ")
print(myList)
item = int(input("Enter element to be deleted "))
position = Bsearch(myList, item)
if position:
    del myList[position]
    print(myList)
else:
    print("No search of such element ")