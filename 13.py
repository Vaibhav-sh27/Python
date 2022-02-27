#To search Linear list using binary approach.
count = int(input("How many students are there in the class ?"))
fileout = open("Marks.det", "w")
for i in range(count):
    print("Enter details for student", (i+1), "below:")
    rollno = int(input("Rollno:"))
    name = input("Name: ")
    marks = float(input("Marks: "))
    rec = str(rollno) + "," + name + "," + str(marks) +'\n'
    fileout.write(rec)
fileout.close()