# # Variable in Python
# a = 34 #integer
# # b = "harry" #string
# # c = 45.5 #float
# # print(a + c)
# a = "31"
# a = int(a) #type casting
# typeA = type(a)
# print(typeA)
# print(a + 2)


#String

name = "Amrit"
# print(name[index])
# print(name[3:5]) string slicing
# print(name.strip()) trim spaces
# print(len(name)) length of string
# var = name.lower()
# print(var)
# var = name.replace("i", "t")  replace in string
# print(var)

str = "Raj"
# print(name + str) string concat
# temp = "This is {} {} Maurya".format(name,str)
temp = f"This is {name} {str} Maurya"
# print(temp)

# More Operators
# 1. ** Exponential Operator
# 2. // floor division operator
# 3. % modulo operator
# print(2**3)

'''
Python Collections:
1. List
2. Tupple
3. Set
4. Dictionary
'''

# LIST (Modify Items)
# lst = [1,2,3,4,5,6]
# var = type(lst)
# var2 = lst[0]
# lst[4] = 90
# lst.append(100) #append at last
# lst.insert(1,300) #insert at 1 index
# lst.remove(300)
# lst.pop()
# del lst[3] #delete
# lst.clear() #clear
# print("Length : ", len(lst))
# print(lst,var,var2)


#TUPPLE (can't change items) we can type cast it
# a = ("Amrit", "Sampriti", "Mk")
# var = a
# var = type(a)
# a[0] = "Sagrika" can't change from tupple
# print(a, var)

# SET
# s1 = {23,34,3,2,2,2,54,34,2,1,5,6}
# s1.add(4444)
# s1.update([1,23,23,12,434])
# print(len(s1))
# s1.remove(1)
# s1.discard(1000)
# .pop .clear .del .insersection .union
# print(s1)

# Dictionary (key -> value)
# amritDict = {
#     "Name" : "Amrit",
#     "Class" : "Btech",
#     "CGPA" : "8.3"
# }
# print(amritDict)
# amritDict["CGPA"] = "9"
# .pop, .clear, update, del
# print(amritDict["CGPA"])



# age = input("Enter Your Age : ") #yaha jo v input lega wo string ke format me hota hai
# age = int(age)
# print(type(age))

# if(age > 18):
#     print("You can drive a car")
# elif(age == 18):
#     print("You are an awesome team")
# else:
#     print("You cannot drive")


# LOOPS
# print 1 to 100
# for i in range(0,51):
#     print(i)

li = [1,2,43,"This"]
# for items in li:
#     print(items)


# i = 0
# while(i < 10):
#     print(i+1)
#     if(i == 5):
#         break
#     if(i == 8):
#         continue
#     i = i + 1


# Functions
def greet():
    print("Good Morning sir!")

def sum(a,b):
    return a + b

def getList(li):
    print(li)
# we can also pass defult argument as a = 9 or b = 20
# print(sum(3,4))
# greet()
# getList(li)

# OOP

class Person:
    def __init__(self,name):
        self.name = name

    def say_hi(self):
        print("Hello, My name is ",self.name)

p = Person('Amrit')
p.say_hi()

class Employee:
    company = "Google"
    a = 23
    b = 43
    salary = 400 #class variable

    def getSalary(self):
        print(f"Salary is {self.salary} of {self.company}")
    @staticmethod   #then we don't need to pass self argument
    def greet():
        print("Good Morning sir!")

harry = Employee()
amrit = Employee()
# print(harry.company)
# print(harry.a + harry.b)
# harry.a = 34
# print(harry.a + harry.b)
harry.salary = 45 #instance Variable
amrit.salary = 334 #instance variable
#for printing first check if instance attribute is present or not if not then check class attribute
# instance variable have high priority over class attribute during assignment and retrival
print(harry.salary)
print(amrit.salary)
harry.getSalary()
harry.greet()

