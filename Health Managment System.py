#Hospital Managment System Devoloped By Rajat Bais
import datetime
def HealthManager():
    """ Hospital Managment System """
namedict={1:"Rajat",2:"Aashay",3:"Ashish"}
actiondict={1:"Log",2:"Retrive"}
activitydict={1:"Food",2:"Health Status",3:"Medicines"}
def gettime():
    return datetime.datetime.now()
print(HealthManager.__doc__)
while(True):
    try:
        for key,value in namedict.items():
            print("Press ",key," for ",value, "\n", end="")
        name=int(input("Type Here...\n"))
        for key,value in actiondict.items():
            print("Press ",key," for ",value,"\n",end="")
        action=int(input("Type Here...\n"))
        for key,value in activitydict.items():
            print("Press ",key," for ",value, "\n", end="")
        activity=int(input("Type Here...\n"))

        if name==1 and action==1 and activity==1:
            value = input("Type Here....\n")
            with open("Rfood.txt", "a") as Rf:
                Rf.write(str([str(gettime())]) + ": " + value + "\n")
                print("successFully Written\n")
        elif name==1 and action==1 and activity==2:
            value=int(input("Type Here....\n"))
            with open("RHStatus.txt", "a") as Rhs:
                Rhs.write(str([str(gettime())])+ ":" +value +"\n")
                print("SuccessFully Written\n")
        elif name==1 and action==1 and activity==3:
            value=int(input("Type Here....\n"))
            with open("Rmed.txt", "a") as Rmd:
                Rmd.write(str([str(gettime())])+ ":"+value+"\n")
                print("SuccessFully Written\n")
        elif name==1 and action==2 and activity==1:
            with open("Rfood.txt", "r") as Rf:
                a=Rf.read()
                print(a)
        elif name==1 and action==2 and activity==2:
            with open("RHStatus.txt", "r") as Rhs:
                a=Rhs.read()
                print(a)
        elif name==1 and action==2 and activity==3:
            with open("Rmed.txt", "a") as Rmd:
                a=Rmd.read()
                print(a)
        elif name==2 and action==1 and activity==1:
            with open("Afood.txt","a") as Af:
                Af.write(str([str(gettime())])+":"+value+"\n")
                print("SuccessFully Written\n")
        elif name==2 and action==1 and activity==2:
            with open("Ahstatus.txt","a" )as Ahs:
                Ahs.write(str([str(gettime())])+":"+value+"\n")
                print("SuccessFully Written\n")
        elif name==2 and action==1 and activity==3:
            with open("Amed.txt","a") as Amd:
                Amd.write(str([str(gettime())])+":"+value+"\n")
                print("SuccessFully Written\n")
        elif name==2 and action==2 and activity==1:
            with open("Afood.txt", "r") as Af:
                a=Af.read()
                print(a)
        elif name==2 and action==2 and activity==2:
            with open("Ahstatus.txt","r") as Ahs:
                a=Ahs.read()
                print(a)
        elif name==2 and action==2 and activity==3:
            with open("Amed.txt", "r") as Amd:
                a=Amd.read()
                print(a)
        elif name==3 and action==1 and activity==1:
            with open("Asfood.txt","a") as Asf:
                Asf.write(str([str(gettime())])+":"+value+"\n")
                print("SuccessFully Written\n")
        elif name == 3 and action == 1 and activity == 2:
            with open("Ashstatus.txt", "a") as Ashs:
                Ashs.write(str([str(gettime())]) + ":" + value + "\n")
                print("SuccessFully Written\n")
        elif name == 3 and action == 1 and activity == 3:
            with open("Asmed.txt", "a") as Asmd:
                Asmd.write(str([str(gettime())]) + ":" + value + "\n")
                print("SuccessFully Written\n")
        elif name==3 and action == 2 and activity==1:
            with open("Ashstatus.txt", "a") as Ashs:
                a=Ashs.read()
                print(a)
        elif name == 3 and action == 2 and activity == 2:
            with open("Asmed.txt", "a") as Asmd:
                a=Asmd.read()
                print(a)
        elif name ==3 and action== 2 and activity==3:
            with open("Asmed.txt", "a") as Asmd:
                a=Asmd.read()
                print(a)

        z=int(input("Do You Want Do it Again Y/N?"))
        if z=="y":
            continue
        if z=="n":
            break

        else:
            print("Illogical Value")
    except Exception as e:
        print("something went wrong")
