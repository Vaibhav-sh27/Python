#To append student records to the file created.
fileout = open("Marks.det", "a")
for i in range(2):
    print("Enter details for Student", (i+1), "below: ")
    rollno = int(input("Rollno: "))
    name = input("Name: ")
    marks = float(input("Marks: "))
    rec = str(rollno) + "," + name + "," + str(marks) + '\n'
    fileout.write(rec)
fileout.close()
