rec=[]
import pickle
def school():
    db=open("dominics.dat","ab")
    stdno=int(input("enter roll"))
    sname=input("enter student name")
    fname=input("enter fathers name")
    address=input("enter address")
    dob=input("enter dob")
    rec=[stdno,sname,fname,address,dob]
    pickle.dump(rec,db)
    db.close()
def records():
    db=open("dominics.dat","rb")
    try:
        while True:
            rc=pickle.load(db)
            print(rc)
    except:
        db.close()
school()
records()        

