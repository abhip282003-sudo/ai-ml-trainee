#mini calculator
num1=int(input("enter a  first number to calculate:"))
num2=int(input("enter a second number to calculate: "))
print("select operartor:")
print("1,addition(+)")
print("2, substraction(*)")
print("3,multiplication(-)")
print("4,division(//)")
choice=int(input("enter a choice 1-4::"))
if choice==1:
    print("addition",num1+num2)
elif choice==2:
    print("substraction",num1-num2)
elif choice==3:
    print("multiplication",num1*num2)
elif choice==4:
    try:
        a=num1/num2
        print("divison",a)
    except ZeroDivisionError:
        print("zero dividession error")
    
else:
    print("invalid")