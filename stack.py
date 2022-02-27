l=[23,45,7]
print("original list",l)
def Push(lst, item):
    lst.append(item)

def Pop(lst):
    lst.pop(0)
a=input("p or po")
if a=='p':
    d=int(input("enter no."))
    Push(l,d)
else:
    Pop(l)
print(l)
