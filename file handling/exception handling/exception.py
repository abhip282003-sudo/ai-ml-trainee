# # Q1 division
# a=int(input("enter a first number:"))
# b=int(input("enter a second number"))
# print("divison using exception handling")
# try:
#     divison=a/b
#     print("divsion is",divison)
# except ZeroDivisionError:
#     print("zerodivisionerror")
      



# #Q2Handle invalid input exception while taking integer input.
# try:
#     a=int(input("enter a integer:"))
# except ValueError:
#     print("it is not accepted")

#Q3eHandle file not found exception

# try:
#     file=open("sample.txt","r")
#     data=file.read()
#     file.close()
# except FileNotFoundError:
#     print("file is not found")
# finally:
#     print("continue program")
      
    
#Q4Handle multiple exceptions in a single program
# try:
#     a=int(input("enter a intheger"))
#     b=int(input("enter a second integer"))
#     result=a/b
#     print("divioson",result)
# except ValueError:
#     print("it in not a integre enter only integer")
# except ZeroDivisionError:
#     print("not divisible by zero")



#Q5Use finally block to close file properly.
# try:
#     file=open("sample.txt","r")
#     data=file.read()
#     print(data)
# except FileNotFoundError:
#     print("not found file")
# finally:
#     file.close()
#     print("continue program")



#Q6Create custom exception for invalid age input.
# class Invalidage(Exception):
#    pass
# age=int(input("enter a age"))
# try:
#     if age>0 and age>120:
#      raise Invalidage("Age must be between 0 and 120")
#     print("valid age",age)
# except Invalidage as e:
#    print("error",e)




#Q7Create Custom Exception for Insufficient Bank Balance
# class Insufficient(Exception):
#     pass
# # balance=int(input("enter a balance amount:"))
# try:
#     balance=int(input("enter a balance amount:"))
#     withdraw=int(input("enter amount to withdraw:"))
#     if withdraw>balance:
#         raise Insufficient("there is no balance ")
#     balance-=withdraw
#     print("reamining=",balance)
# except Insufficient as i:
#     print("not enough balance to withdr",i)




#Q8Handle index out of range exception in list operations.
# number=[12,32,34,54,32]
# try:
#     index=int(input("enter number to chcek range:"))
#     print("index is",number[index])
# except IndexError:
#     print("out of range")



#Q9Handle key error exception in dictionary acces
# student = {
#     "name":["abhishek","ram","rohan"],
#     "age":[11,12,32]
# }
# try:
#     key=input("enter a key:")
#     print(student[key])
# except KeyError:
#     print("index eroor")





#10Handle ValueError in Type Conversion
# try:
#     i=int(input("enter a number:"))
#     print("input number is:",i)
# except ValueError:
#     print("enter only integer:")






# #Q11Create login system with exception handling
# class Invalid_user(Exception):
#     pass
# username="admin"
# password=1234
# try:
#     user=input("enter a username:")
#     pas=input("enter a password:")
#     if user==username or pas==password: 
#      raise Invalid_user("invalid user and password:")
#      print("login successfully")

# except ValueError as v:
#           print("value eror",v)
# except Invalid_user as v:
#       print("user is not find",v)
# finally:
#     print("login process compleate")




#Q12Raise exception if password is too weak.
# class Weak_pass(Exception):
#     pass

# while True:
#     try:
#         password=input("enter a password:")
#         if len(password)>8:
#             raise Weak_pass("password is at least 8 digit:")
        
#         if not any(char.isdigit()for char in password):
#             raise Weak_pass("contain atleast one digit")
        
#         if not any(char.isupper()for char in password):
#             raise Weak_pass("contain atleast  one upper character")
        

#         print("password is to strong:",password)
#         break
        
#     except Weak_pass as e:
#      print("password is weak",e)





#13 Build safe file reader using try-except-finally.
# file = None
# try:
#     file = open("data.txt", "r")
#     data = file.read()
#     print("File Content:\n")
#     print(data)

# except FileNotFoundError:
#     print("Error: File not found")
# finally:
#     if file:
#         file.close()
#         print("\nFile closed successfully")





#Q14Create ATM system with proper exception handling.

# class InsufficientBalanceError(Exception):
#     pass

# balance = 10000

# while True:
#     try:
#         print("\n===== ATM MENU =====")
#         print("1. Check Balance")
#         print("2. Deposit Money")
#         print("3. Withdraw Money")
#         print("4. Exit")

#         choice = int(input("Enter your choice: "))

#         if choice == 1:
#             print("Your balance is:", balance)

#         elif choice == 2:
#             amount = int(input("Enter deposit amount: "))

#             if amount <= 0:
#                 raise ValueError("Amount must be positive")

#             balance += amount
#             print("Money deposited successfully")
#             print("Updated balance:", balance)

#         elif choice == 3:
#             amount = int(input("Enter withdrawal amount: "))

#             if amount <= 0:
#                 raise ValueError("Amount must be positive")

#             if amount > balance:
#                 raise InsufficientBalanceError("Insufficient balance")

#             balance -= amount
#             print("Withdrawal successful")
#             print("Remaining balance:", balance)

#         elif choice == 4:
#             print("Thank you for using ATM")
#             break

#         else:
#             print("Invalid choice")

#     except ValueError as e:
#         print("Input Error:", e)

#     except InsufficientBalanceError as e:
#         print("ATM Error:", e)

#     except Exception as e:
#         print("Unexpected Error:", e)




#Implement nested try-except blocks in a real-world program.
class InvalidLoginError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

correct_username = "admin"
correct_password = "1234"
balance = 100004
try:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username != correct_username or password != correct_password:
        raise InvalidLoginError("Invalid login credentials")

    print("Login successful!\n")
    try:
        print("1. Check Balance")
        print("2. Withdraw Money")
        choice = int(input("Enter choice: "))
        if choice == 1:
            print("Your balance is:", balance)
        elif choice == 2:
            amount = int(input("Enter amount: "))
            if amount > balance:
                raise InsufficientBalanceError("Not enough balance")
            balance -= amount
            print("Withdrawal successful")
            print("Remaining balance:", balance)
        else:
            print("Invalid ATM option")
    except ValueError:
        print("ATM Error: Enter valid numeric input")
    except InsufficientBalanceError as e:
        print("ATM Error:", e)

except InvalidLoginError as e:
    print("Login Error:", e)

except Exception as e:
    print("Unexpected Error:", e)

finally:
    print("\nSession ended")
    