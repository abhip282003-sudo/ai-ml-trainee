#Create a text file and write data into it
file = open("sample.txt", "w") 
file.write("Hello Abhishek\n i am aiml trainee ")
file.close()
print("data write succesfully in file")



#2
#Read data from a text file.
# file=open("sample.txt","r")
# data=file.read()
# print(data)
# file.close()

#Q3
# file=open("sample.txt","a")
# file.write("sagar is also aiml trainee")
# print("sucessfully added")
# data=file.read
# print(data)
# file.close()


#Q4
# file = open("sample.txt", "r")
# lines = file.readlines()
# print("Number of lines:", len(lines))
# file.close()

#Q5
# file = open("sample.txt", "r")
# data = file.read()
# print(data)
# words = data.split()
# print("Number of words:", len(words))
# file.close()


#Q6
# file = open("sample.txt", "r")
# data = file.read()
# print("Number of characters:", len(data))
# file.close()



#Q7
# file = open("sample.txt", "r")
# for line in file:
#     print(line.strip())
# file.close()



#Q8
# source = open("sample.txt", "r")
# destination = open("copy.txt", "w")
# destination.write(source.read())
# source.close()
# destination.close()
# print("File copied successfully.")




#Q9
# files = ["file1.txt", "file2.txt", "file3.txt"]
# with open("merged.txt", "w") as outfile:
#     for fname in files:
#         with open(fname, "r") as infile:
#             outfile.write(infile.read())
#             outfile.write("\n")
# print("Files merged successfully.")


#Q10
# from collections import Counter
# file = open("sample.txt", "r")
# data = file.read().lower()
# words = data.split()
# frequency = Counter(words)
# for word, count in frequency.items():
#     print(word, ":", count)
# file.close()




 # Q11 create a file 
# file = open("email.txt", "w")

# file.write("Please contact us at support@gmail.com for technical help.For HR queries, email hr.department@yahoo.com.You can also reach admin@company.in or info123@org.co.in.Some invalid emails:test@@gmail.comuser#mail.comThank you.team Management")
# file.write("This is a new file created using Python")
# file.close()
# print("File created and data written")
# import re
# with open("email.txt", "r") as file:
#     data = file.read()
# emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", data)
# print("Email Addresses Found:")
# for email in emails:
#     print(email)



#Q12
# import csv
# with open(r"C:\Users\ACER\OneDrive\เอกสาร\Abhishek prajapati\student.csv", "r") as file:
#     reader = csv.reader(file)
#     print("Student Records:\n")

#     for row in reader:
#         print(row)

#Q13
# import csv
# with open("students.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["RollNo", "Name", "Marks"])
#     n = int(input("Enter number of students: "))
#     for i in range(n):
#         roll = input("Enter Roll No: ")
#         name = input("Enter Name: ")
#         marks = input("Enter Marks: ")
#         writer.writerow([roll, name, marks])
# print("Records saved successfully.")








#14
FILE_NAME="student.txt"
def add_student():
    name=input("enter a name of student:")
    roll_no=int(input("enter a roll no of student:"))
    marks=int(input("enter a marks of student:"))
with open("FILE_NAME" ,"w")as file:
    file.write("f{name},{roll_no},{marks}\n")
    print("student is added:")

def display_student():
    try:
        with open(FILE_NAME,"r") as file:
            print("student is find")
            print(file.read())
    except FileNotFoundError:
        print("student not found")
def search_student():
    roll_search=int(input("enter a roll no to serach student"))
    found=False
    try:
        with open(FILE_NAME,"r") as file:
            for line in file:
                 roll_no, name, marks = line.strip().split(",")
                 if roll_no==roll_search:
                     print("name:",name)
                     print("roll:",roll_no)
                     print("mark:",marks)
                     found=True
                 if FileNotFoundError:
                     print("not found data")
    except FileNotFoundError:
        print("student is not found")

def del_student():
    roll_del=int(input("enter a roll no to delete"))
    found=False
    try:
         with open(FILE_NAME, "r") as file:
            lines = file.readlines()
         with open(FILE_NAME,"r") as file:
            for line in file:
                roll_no,name,marks=line.strip().split(",")
                if roll_no==roll_del:
                    file.write(lines)
                else:
                    found=True
                if found:
                    print("successfully deleted")
                else:
                    print("not found")
    except FileNotFoundError:
        print("not founded enter number")



while True:
    choice=int(input("enter a choice:1-5::"))
    print("student data")
    print("1, add student:")
    print("2,display student:")
    print("3,search student:")
    print("4,delte studet:")
    print("5,exit:")
    if choice==1:
       print("add student",add_student())
    elif choice==2:
        print("student display:",display_student())
    elif choice==3:
        print("student searching:",search_student())
    elif choice==4:
        print("student delted:",del_student())
    elif choice==5:
        print("exit system")
    break
else:
    print("invalid input")

    
                     

              







