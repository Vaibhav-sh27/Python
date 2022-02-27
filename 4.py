#Program to sort a sequence uaing insertion sort.
aList = [15, 6, 13, 22, 3, 52, 2]
print("Original list is : ",aList)
for i in range(1,len(aList)):
	key = aList[i]
	j = i-1
	while j >=0 and key < aList[j]:
		aList[j+1] = aList[j]
		j = j-1
	else:
		aList[j+1] = key
print("List after sorting :", aList)