'''
a,b=c=7,8
print(a)
print(b)
print(c)

a=b,c=4,2
print(a,b,c)

#----->swaping of variables
a=7
b=5


temp=a
a=b
b=temp
print(a,b)

Eg:2
a=a+b
b=a-b
a=a-b

print(a,b)

a,b=b,a
print(a,b)

a=a*b
b=a/b
a=a/b
print(int(a),int(b))

#id() -->used to find the memory address of the variable
a=7
b=8
print(id(a))
print(id(b))

#---> keywords
#keywords are reserved words which provides special meaning to compiler interpretor

import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
print(type(keyword.kwlist))

#To check if the string is keyword or not
print(keyword.iskeyword("sid"))

#if=8
print(if) #error coz if is a keyword


a=9
b=9
b=90
print(id(a))
print(id(b))

#! ---> Operators
Operators are symbols which is used to perform various operions
# ? between 2 or more operands

Arithmatic
logical
Relational
bitwise
Identity
membership
Assignment

#*--->Airthematic -->+,-,*,/,%,//,**
# Eg:1
a=8
b=6
c=9
print(a+b+c)

#input() --> used to get the run time input
#eval() --> used to get the runtime values of all datatypes


n1 = eval(input("Enter the value:"))
print(type(n1))

a=4
b=2
print(a/b)# is used to get the quotient value
print(a%b)# is used to get the remainder value

# ! assignment ---> +=,-=,/=,*=,//=,**=,&=,|=,
a=8
a+=2
print(a)

a=30
a=-5
print(a)

#! comparision ---> ==, >, <, !=,<=,>=
a=8
b=7
print(a==b)

# ! bitwise operator -->

a=7
b=4
print(a&b)

2^4 2^3 2^2 2^1 2^0
8    4   2   1

0    1   1   1  # --> 7
0    1   0   0  # --> 4&
 --------------
 0   1   0   0

 # <<, >>
 print(5>>1)
16>4

#! logical --> used to compare the expressions
and, or, not
a=6

#print(a>3 and  a<10)
#print(a>7 or a<30)
print(not(a>8 and a<10))

# identity operator
is,is not
a=8
b=8
print(a is b)
print(a==b)

a=[1,2,3]
b=[1,2,3]
print(a is not b)


# ! memebership operator
#in, not in
l1 = [7,8,9,0,6,5]
num = 5
print(num in l1)
print(num not in l1)

num = 678
print(8 in num) # error

# ! conditional statement
# if,elif,else

# Eg:1
#--->C syntax

if (condition){
    statement;
    statement;
    statement;
    }
# Python syntax
if condition:
    statement
    statement
    statement
#statement

#eg:1
    a=6
    if a:
        print("hello")
#eg:2
        
a=6
if a>3:
    print("yes")
else:
    print("no")
    
# eg:3

if 7>8:
    print("hello")


    print("no")
#eg:4
a=0
a=none
a=false
a=""
if a:
    print("yes")
else:
    print("no")

# a number is even or odd
n=int(input("enter the number:"))
if n %2==0:
    print(n,"is even")
else:
    print(n,"is odd")

nmae,age,nationality
18 above, indian
'''
name = input("enter the name:")
age= int(input("enter the age:"))
nationality=input("enter the nation:")

if age >18 and nationality=="Indian":
    print("eligible for vote")
else:
    print("not eligible")




























 


