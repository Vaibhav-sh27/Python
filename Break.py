#Break statement
a=b=c=0
for i in range(1,11):
	a=int(input("Enter number 1 :"))
	b=int(input("Enter number 2 :"))
	if b==0:
		print("Division by zero error ! Aborting ! ")
		break
	else:
		c=a/b
		print("Quotient =", c)
print("Program over !")