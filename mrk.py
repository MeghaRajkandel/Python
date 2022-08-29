from cmath import e
from pickletools import read_int4
from re import I
from tokenize import Name
from unicodedata import name

"""my_string = "python is Awesome  "
print(my_string.capitalize().strip()) #space hatauni aani captial garauni 
print(my_string.index("i")) # 0 dekhi 6 vayo aani 7 mah i ko position vayo , failure mah valueerror (exception) return garcha
print(my_string.find("i")) #same index jastai kaam garcha , failure mah -1 return garcha 
#for input of season and print the message
weather = input("What it the season like right now?: (winter or summer?)")
if weather == "summer":
    print("This is too hot for me")
elif weather == "winter":
    print("This is too cold for me")
else:
    print("I expect you to enter summer or winter")

i = 0
while i<5: # 0 dekhi 4 samma vaneko 5 loops samma garcha 
    print("Hello WOrld!")
    i = i + 1

#Wap to calculate the percentage from given marks.
maths = int(input("Enter the marks obtained in maths"))
science = int(input("Enter the marks obtained in science"))
nepali = int(input("Enter the marks obtained in nepali"))
social = int(input("Enter the marks obtained in social"))
health = int(input("Enter the marks obtained in health"))
total_obtained = maths + science + nepali + social + health
full_marks = 500
percentage = (total_obtained / full_marks)*100
print (percentage)
if percentage >=80:
    print("Distinction")
elif percentage >=70:
    print("First Division")
elif percentage >=60:
    print("Second Division")
elif percentage >=50:
    print("Third Division")
else:
    print("You failed")

 
for i in range(0,10): #0 dekhi 9 print garcha 
    print(i)

for i in range(0,10,2): # 0 dekhi 10 samma lai 2 ko gap ma print garcha
    print(i)

#list data structure
l_fruits = ["Mango", "Orange", "Guava", "Dragonfruit", "Litchi", "Pineapple"] 
a_fruits = [] #empty list 
l_fruits.append("cycle") #add garni list mah 
print(l_fruits)
l_fruits.pop()#paxadi batwa remove garcha 
print(l_fruits)

#Dictionary
employee = {
    "name": "Sujan",
    "address":"Lanku,Bharatpur"
}
employee["salary"] = 25000
print(employee.get("name"), employee.get("salary"))
#example number 2
#WAP that stores students information (studentID,name,address,contact) in dictionary format and print them.
student = {
    "studentID" : 210006,
    "name" : "Anuj",
    "address":"Shantichowk,Chitwan",
    "contact":9865206191
}
for i in student.values():   #values matra ligcha .values le 
    print(i)

#set -->duplicate print gardaina , python ko hack /  feature ho  
set_of_fruits = {"apple","mango","pineapple","guava"} #list [] jastai tara {} use garni for set 
print(type(set_of_fruits))
set_of_fruits.add("litchi") #litchi add vayo 
print(set_of_fruits) #change garesi -mutation- huni 
set_of_fruit={"apple","mango"}
intersected_data = set_of_fruits.intersection(set_of_fruit) #common data ligeko for both set 
print("Fruits both of them like :",intersected_data)
all_fruits = set_of_fruit.union(set_of_fruits) #union vayo duitai set ko 
print("All fruits are:",all_fruits)

#WAP that accepts user input to enter three employee's details
#(name, employeeid, salary). 
#And store those information in a list. then, the name of all the 3 employees.

#take input from the user 
#store the information in dictionary 
#append the information to a list
#display the value of name key of all the elements in the list
employees = []
for i in range(3):
    Name  = input(f"Enter the name {i+1} of employee") #string interpulation--{} bhitra ko value ligna lagi
    employee_id=int(input(f"Enter the {i+1} employee id"))
    salary = int(input("Enter the salary"))
employee_data={
    "Name": Name,
    "employee_id":employee_id,
    "salary":salary
    }

employees.append(employee_data)
print("====================\nEmployees are:")
for employee_data in employees:
    print(employee_data.get("Name"))

def printer():
    print("I am a printer")
printer()
#error for zero division
num=8
division = num/0 #zerodivisionerror -exception dinxa aani exit garcha
#exception handling 
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    division = num1/num2  
    print(division)
except ZeroDivisionError:
    print("Second number cannot be 0")
except KeyboardInterrupt:
    print("DAMN !! You exited")
except Exception as e:
    print("Unknown Error:", str(e))
else:
    print("This might be your required result")
finally:
    print("The program 'try except' is finished")

#JSON = Java Script Object Notation

import json
x = { 
    "name":"John",
    "age":30, 
    "city":"New York",
    "address":None
}
y = json.dumps(x) #converts python into json

# the result is a Python dictionary that is converted to json
print(y)
#loads() ko lagi single quote ' ' bhitra rakhni aani string convert hunxa 

#array ko lagi [] rakhni aani dherai rakhna painxa 
import json
college_data = {
    "students":[              #[] le garda diff dictionary for many students ko data rakhna payo
    { 
    "name":"John",
    "age":30, 
    "city":"New York",
    "address":None
    },
    {
    "name":"David",
    "age":30, 
    "city":"London",
    "address":None
    } 
    ],                    
"faculty": [                 
    {
    "name": "sujan kandel",
    "address": "lanku"
    }
    ]
}
college = json.dumps(college_data)
print(college)

#f = open("./hello.txt","w")
#f.write("Hello world! My name is sujan kandel")
#f.close()
f = open("./hello.txt","r")
print(f.read(4))
f.close()"""
import json
employee_data = {
    "employee":[             
    { 
    "name":"John",
    "ID":3, 
    "city":"New York",
    "address":None,
    "salary":25000
    },
    {
    "name":"David",
    "ID":4, 
    "city":"London",
    "address":None,
    "salary":25000
    } 
    ]
}
employee_json = json.dumps(employee_data)
f = open("./employee.json","w")
f.write(employee_json)
f.close()


