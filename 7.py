#Passing a Mutable Type Value to a function - Adding/deleting items to it.
def myFunc3(myList):
    print("\n\t Inside CALLED Function now")
    print("\t List received: ", myList)
    myList.append(2)
    myList.extend([5,1])
    print("\t List after adding some elements : ", myList)
    myList.remove(5)
    print("\t List within called function, after all changes : ",myList)
    return
List1 = [1]
print("List before function call : ", List1)
myFunc3(List1)
print("\nList after fuction call : ", List1)