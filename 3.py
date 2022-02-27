#Program that receives two numbers in function and returns the results of all arithmetic operations (+, -, *, /, %) on these numbers.
def arcalc(x,y):
	return x+y, x-y, x*y, x/y, x%y
#__main__
num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
add, sub, mult, div, mod = arcalc(num1, num2)
print("Sum of given numbers : ", add)
print("Subtraction of given numbers : ", sub)
print("Product of given numbers : ", mult)
print("Division of given numbers : ", div)
print("Modulo of given numbers : ", mod)