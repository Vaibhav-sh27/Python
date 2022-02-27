#Inserting an element in a sorted array using algorithm.
def findpos(AR, item):
    size = len(AR)
    if item < AR[0]:
        return 0
    else:
        pos = -1
    for i in range(size-1):
        if (AR[i]<= item and item < AR[i+1]):
            pos = i+1
            break
    if (pos == -1 and i<= size-1):
        pos = size
    return pos
def shift(AR, pos):
    AR.append(None)
    size = len(AR)
    i = size-1
    while i>= pos:
        AR[i] = AR[i-1]
        i=i-1
#__main__
myList = [10, 20, 30, 40, 50, 60, 70]
print("The list is sorted in ")
print(myList)
Item = int(input("Enter new to be inserted "))
position = findpos(myList, Item)
shift(myList, position)
myList[position] = Item
print("The list after inserting item is ")
print(myList)