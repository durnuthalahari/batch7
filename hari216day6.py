'''
# 1.)
s1 = imput("enter string:")
fst = s1[0].upper()
ist = s1[-1].upper()
print(fst+s1[1:len(s1)-1]+lst)


n = 128
i = 0
while n!=0:
    rem = n%10
    print(rem)
    n = n/10


#n = 128
#for i in n:
#    print(i)


#n = 128
#while n!=0:
#    rem = n%10
#    print(rem)
#    n = n/10

#n = 128
#for i in str(n):
#    print(i)

n = 128678
temp = n
str1 = ""
while n!= 0:
    rem = n%10
    check = temp % n



n = 128678
temp = n
str1 = ""
while n!= 0:
    rem = n%10
    check = temp % rem
    if check==0:
        print("yes")
    n=n//10
       
n=128
temp=n
f1=0
while n!=0:
    rem=n%10
    check=temp%rem
    if check!=0:
        f1=1
        n=n//10
        
    if f1==0:
        print("yes")
    else:
        print("no")
'''
l1 = [8, 9, 0, 7]
l2 = [7, 6, 5, 4]

#print(l1[0]+l2[0], l1[1]+l2[1])
l3 = []
for val in range(len(l1)):
    ans = l1[val]+l2[val]
    l3.append(ans)
print(l3)

# Eg:1
#s1 = {9, 9, 89, 7.76, 8+7j, (8, 7, 5), "truck", 'e'}
#print(s1)

# * Eg:2
#s2 = {5, 8, 98, [9, 0]}
#print(s2) ----> error


# Eg: 4
# min(), max(), len()

# * Eg:
# ? to add element inside set

s1 = {8, 78, 67, 'u'}
#add
#s1.add(43)
print(s1)


# ? to delete element inside set
s1 = {8, 78, 67, 'u'}


# pop() # to delete one element randonly
# s1.pop()
# print(s1)

# remove()
s1.remove(78)
print(s1)

# discard()
s1.discard(8967)
print(s1)


# clear()
l1 = {}
print(type(l1)) ---- datatype is dict

s1 = set() # to creat empty set
print(type(s1))



# clear()
'''
l1 = {}
print(type(l1)) 
'''

'''
s1 = set() # --> to create empty set
print(type(s1))
'''

'''
s1 = {8,9,0}
s1.clear()
print(s1)
'''

'''
s1 = {8,9,0}
del s1
print(s1)
'''


s1 = {1,2,3,4,5}
s2 = {3,2,7,8,9}

for val in s1:
    if val in s2:
        str1 = "Its joint set"
print(str1)
RE 320 SHAIK ARSHAD BASHA
1:24 PM
1)

#* join the sets
s1 = (9, 0, 8}
s2 = (9.90, "card", 't', 56)
# union()---> to ambine 2 sets
s3 = s1.union(s2)
print (s3)

# * intersection()---> to get common elements inside set
s1 = (4, 5, 6)
s2 = (5, 6, 7, 8)
print(s1.intersection(s2))

# * difference()
s1 = {4, 5, 6,}
s2 = {5, 6, 7, 8}
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))


isdisjoit(), issubset(), issuperset()
s1 = (8, 9, 8)
s2 = (6, 7, 5, 8, 9, 0)

print(s1.issubset(s2))
print(s2.issupers

#1.)Python program to captilalize the first and last character of each word in a string
#2.)Input:128
#ouput:Yes
#128%1==0,128%2==0, and 128%8==0.
#3.)l1=[1,2,3,4],l2=[5,6,7,8]
#add both l1 and l2 and ans=[6,8,10,12]


n = 128
while n!=0:
    rem = n%10
    print (rem)
    n = n/10

s1 = input("enter string: ")
fst = s1[0].upper()
lst = s1[-1].upper()
print(fst+s1[1:len(s1)-1]+lst)

s1 = (8, 78, 67, 'u')
add()
s1.add(43)
print(s1)

update()
s1.update([9, 0])
print(s1)

s1 = set() # to create e
...................
ssv-hcbt-rgo


# ! ----> dictonary
# eg:1
mech = {
    "student1":{
        "name":"name1"
        "age":24,
        "mark":89,
  },
   "student2":{
        "name":"name2"
        "age":24,
        "mark":89,

  },
   "student3":{
        "name":"name3"
        "age":24,
        "mark":89,
suresh ganugapenta
1:39 PM
YARRA GUDDODA\\=.
\

# ? char of dictionary
# 1.) Have to be surrounded by{}
# 2.) It have to be in the form of key,value pair
# 3.) It is mutable
# 4.) Duplicate keys are not allowed,
# 5.) Duplicate values are allowed
# 6.) It is unidexed
# 7.) It is ordered
# 8.) Key does nat allow mutable datatypes
# 9.) Values allow mutable datatypes


d1={1:100,2:200,3:300,-4:400}
#to access elements in dictionary
print(d1)
#or
#to access the values
print(d1[-4])#---->o/p is 100

#some common functions
#len(),min(),max()
print(min(d1))
print(max(d1))

#to find min,max based on values
print(min(d1.values())


# ? delete element from dictionary
d1 = {1:100, 2:200, 3:300,4:400}
#pop item()
d1.popitem()
print(d1)

#pop()
#d1.pop(2) # ---> 2 is the key in dictionary
#print(d1)

# clear(),del

# join 2 dictionary
d1 = {1:100, 2:200, 3:300, 4:400}
d2 = {"a":"apple",



#pop()
#d1.pop(2) # ---> 2 is the key in dictionary
#print(d1)

# clear(),del

# join 2 dictionary
#update()
#d1 = {1:100, 2:200, 3:300, 4:400}
#d2 = {"a":"apple", "b":"boy", "g":"game"}
#d1.update(d2)
#print(d1)

# get()
d1 = {1:100, 2:200, 3:300, 4:400}



# Iterating dictionary
for val in d1:
    print(val)


# * Iterating dictionary
#for val in d1:
#    print(val)

#for val in d1.value():
#    print(val)

# to get both keys and values
for key, val in d1.items():
    print(key, val)



# ! Problem:1
# n = input()


#1.) swap elemwnts in string list
# The original list is :["Ggf", "best", "for", "geeks"]
# List after performing character swaps:]"efg", "is", "bBgst", "for", "eGGks"]


















