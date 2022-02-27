#Passing a mutable Type Value to a function - Making changes in place
def myFunc2(myList):
	print("\n\t Inside CALLED Function now")
	print("\t List received:", myList)
	myList[0] += 2
	print("\t List within called function, after changes :", myList)
	return
List1 = [1]
print("List before function call : ", List1)
myFunc2(List1)
print("\nList after function call : ", List1)