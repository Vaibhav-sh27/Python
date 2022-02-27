#Passing an Immutable Type Value to a function.
def myFunc1(a):
	print("\t Inside myFunc1()")
	print("\t Value recived in 'a' as", a)
	a=a+2
	print("\t Value of 'a' now changes to", a)
	print("\t Returning from myFunc1()")

#__main__
num = 3
print("Calling myFunc1() by passing 'num' with value", num)
myFunc1(num)
print("Back from myFunc(). Value of 'num' is", num)