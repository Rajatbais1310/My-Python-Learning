#Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
print("Faulty Calcuator Devoloped By Rajat Bais")


while(True):
    opr = input("Which Kind of Operation Do You Want to Perform\n"
                "Press + for Addition and Press Enter\n"
                "Press - for Substraction and Press Enter\n"
                "Press * for Multiplication and Press Enter\n"
                "Press / for Division and Press Enter\n"
                "Press % for Modulous and Press Enter\n")
    no1=int(input("Enter Your First Number and Press Enter\n"))
    no2=int(input("Enter Your Second Number and Press Enter\n"))
# Addition
    if opr=="+":
        if no1==56 and no2==9:
            print("56+9 = 77")
        else:
            result=no1 + no2
            print("Addition is :",+result)
#Substraction
    if opr=="-":
        if no1==0 and no2==0:
            print("Error")
        else:
            result=no1-no2
            print("Substraction is :",+result)
#Multiplicttion
    if opr=="*":
        if no1==45 and no2==3:
            print("45 * 3 = 555")
        else:
            result=no1*no2
            print("Multiplication is :",+result)
#Division
    if opr=="/":
        if no1==56 and no2==6:
            print("56/6 = 4")
        else:
            result=no1/no2
            print("Division is :",+result)
#Modulous
    if opr=="%":
        if no1==0 or no2==0:
            print("Not Defined")
        else:
            result=no1%no2
            print(result)
    else:
        print("Do You Want to Perform Operation Again Y/N?\n")
        z=input()
        if z=="y":
            continue
        if z=="n":
            break

