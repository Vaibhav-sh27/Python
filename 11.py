#Program to create CSV file to store student data. Obtain data from user and write 5 records in file.
import csv
fh = open("Student.csv","w")
Stuwriter = csv.writer(fh)
Stuwriter.writerow(['Roll no.','Name','Marks'])
for i in range(5):
    print("\nStudent record",(i+1))
    roll_no = int(input("Enter Roll no: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    sturec = [roll_no,name,marks]
    Stuwriter.writerow(sturec)
fh.close()