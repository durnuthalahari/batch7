'''
# ! method riding
# * polymorphism in classes

# ? Eg:1

class bank:
    def ratio(self):
        print("All banks has rapo rate")

class SBI(bank):
    def ratio(self):
        print("SBI rate is 9%")

class IOB(bank):
    def ratio(self):
        print("IOB rate is 7.5%)

i = IOB()
i.ratio()

s = SBI()
s.ratio()


# ? Eg:2
class USA:
    def langauge(self):
        print("english")

    def capital(self):
        print("Washington DC")

class India(USA):
    def langauge(self):
        print("None")

    def capital(self):
        print("New delhi")


I = India()
I.langauge()
I.capital()

# E:3
# polymorphism using objects


c1,c2 --->c1 = print(c1),print(c2)
f1,f2

class c1:
    def f1(self):
        print("class 1")

class c2(c1):
    def f1(self):
        print("class 2")

obj = c2()
obj1.f1()

obj=c2()
obj2.f1()

# * Eg:4

class c1:
    def f1(self):
        print("class 1")

class c2(c1):
    def f1(self):
       
        print("class 2")


obj1 = c2()
obj = c1()


def display(a):
    a.f1()
display(obj1)
display(obj2)


# * changing the functionality of builtin functions
a=9
b=9
print(a+b)

# ! Encapsulationj1 n
# --->Eg:1
class car:
    _name = "BMW"
    print(_name)


class = car()

print(c1.name)
c1.name = "Audio"
print(c1.name)


# * --->Eg:2
# ? Accessing private data outside the class
class c1:
    _phone = '7842255098'

    def display(self):
        print(self._phone)

c = c1
print(c._phone)



# ? declare private method
class class1:
    def _m1(self):
        print("Iam private method")

    def _init_(self):
        self. _m1()
c=class1()
c. _m1()
'''

# ? nested class
class class1:
    class class2:
        name = "sidhu"

        def display(self):
            print(self.name)

obj = class1()


















