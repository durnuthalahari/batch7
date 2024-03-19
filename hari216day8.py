'''
def profile(name, age, place):
    txt = "My name is {}. I am {} years old. I am from {}."
    print(txt.format(name, age, place))
profile("Shashank", 21,"KSRM")

def f1(a,b):
    c=a*b
    return c
print(f1(6,8))
obj=f1(6,8)
obj1=f1(4,6)


def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)


def palindrome(n):
    string=str(n)
    rev=str(n)[::-1]
    if string==rev:
        print(n,"palindrome")
    else:
        print("Not palindrome")
a=int(input("Enter the value:"))
palindrome(a)


# ? based on the decleration of parametrs and args
# ? funtions are divided in to 5 categories

#Positional args
#keyword args
#default args
#variable length args
# keyword variable length args
# Positional args 


# * position args
# Eg:1
def profile(name,phone,mark):
    txt="my name is{}.my phone number is{}.i got{} marks."
    print(txt.format(name,phone,mark))

profile(7842255098,"sidhu",97)


# * keyword args
# ! Eg:1
# ? to overcome the disadvantages of position args,we use keyword args
def profile(name,phone,mark):
    txt="my name is{}.my phone number is{}.i got{} marks."
    print(txt.format(name,phone,mark))


profile(name="sid", mark=96,phone=1235647820)


# * default args
# ! Eg:1


def profile(name,phone,place="kadapa"):
    txt="my name is{}.my phone number is{}.i am from{}."
    print(txt.format(name,phone,place))


profile("sid", 7842255098,"Guntur")

Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’. 
The length of the string is variable. The task is to find the minimum number of ‘*’ 
or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ 
and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
Note : The output will be a positive or negative integer based on number of ‘*’ 
and ‘#’ in the input string.

(*>#): positive integer
(#>*): negative integer
(#=*): 0



# ! Eg:2
 def profile(*name, age):
     for val in name:
         print("My name is",val, "my age is", age)
profile("sid", 'name2', 'name3', 28)


 def profile(*name, age):
     for val in name:
         print("My name is",val, "my age is", age)
profile(28, "sid", 'name2', 'name3')


# * Keyword variable length args
# ! Eg:1
def price(price_list):
    price(price_list)

print(shirt=1000, iphone=80000)


# n = int(input("Enter the number: "))
def dict1(n):
    d1 = {}
    for val in range(1, n+1):
        d1[val] = val**2
    print(d1)
dict(5)


# d1 = {"a":100, "b":200, "c":300}
# d1 = dict(a=100, b=200, c=3 00)
# print(d1)

'''

# ! ---> object oriented programming

# The panadigms of objects oriented progarmming are


# class
# objects
#inheritance
#polymorphism
#abstraction
# encapsulation

# ! Class is a blue print of an object1


l1 = [1,2,3,4,56]


# ? Eg:1
class c1:
    name = "sidhu"
    print(name1)

# ? Eg:2
class person()
nmae = "sidhu"

c = person()
print(c.name)


# ? Eg:3
#create of method
#When the function is created with a class is called as method

class person:
    def display():
        print("Hello welcome to classes")

p = person()
p.display()
































