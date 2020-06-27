# 1.	Write a program that calculates and prints the value according to 
# the given formula:
# Q= Square root of [(2*C*D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.

import math

C=50
D=int(input("enter a number: "))
H=30
x= (2*C*D)/H
Q= math.sqrt(x)
print(Q)

#2.         Define a class named Shape and its subclass Square.
#  The Square class has an init function which takes a length as argument. 
# Both classes have an area function which can print the area of the shape where 
# Shape’s area is 0 by default.

class Shape():
    def area(self, a,b):
        x= a*b
        print(x)



class Sqr():
    def __init__(self, length):
        self.length=  length*length    
        print(self.length)   

S= Shape()
sq=Sqr(3)

S.area(2,3)
sq



# 3.          Create a class to find the three elements that sum to
#  zero from a set of n real numbers.
# Input array: [-25,-10,-7,-3,2,4,8,10]
# Output: [[-10,2,8],[-7,-3,10]]


class ele():
    def sumtozero(self, arg, x):
        for i in range(0, x-2):       
            for j in range(i+1, x-1): 
                for k in range(j+1, x): 
                    if (arg[i] + arg[j] + arg[k] == 0): 
                        print(arg[i], arg[j], arg[k]) 
E=ele()
arg=[-25,-10,-7,-3,2,4,8,10]
E.sumtozero(arg, len(arg))    

# 4. What is the output of the following code? Explain your answer as well.


class Test:
    def __init__(self):
        self.x = 0

class Derived_Test(Test):
    def __init__(self):
        self.y = 1

def main():
    b = Derived_Test()
    print(b.x,b.y)
main()

# -> variables x and y are not defined in func arguments





class A:
    def __init__(self, x= 1):
        self.x = x
class der(A):
    def __init__(self,y = 2):
        super().__init__()
        self.y = y
def main1():
    obj = der()
    print(obj.x, obj.y)
main1()

#-> variables x and y are defined in constructor arguments

class A1:
    def __init__(self,x):
        self.x = x
    def count(self,x):
        self.x = self.x+1
class B1(A1):
    def __init__(self, y=0):
        A.__init__(self, 3)
        self.y = y
    def count(self):
        self.y += 1     
def main2():
    obj = B1()
    obj.count()
    print(obj.x, obj.y)
main2()

#-> here o/p are x= 3 and y= 1  because class B inherit class A where
#  value of x given in class B is 3, value of count function in class A changes as
#  it is also present in class b which gives value of y as 1



class X:
    def __init__(self):
        self.multiply(15)
        print(self.i)
 
    def multiply(self, i):
        self.i = 4 * i
class Y(X):
    def __init__(self):
        super().__init__()
 
    def multiply(self, i):
        self.i = 2 * i
obj = Y()

#-> value given to i is 15 which return output as 30



# 5 Create a Time class and initialize it with hours and minutes.


class Time():
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self,time1, time2):
        time3 = Time(0,0)
        if time1.minutes + time2.minutes > 60:
            time3.hours = (time1.minutes + time2.minutes)/60
        time3.hours = time3.hours + time1.hours + time2.hours
        time3.minutes = (time1.minutes + time2.minutes) - (((time1.minutes + time2.minutes)/60)*60)
        return time3

    def displayTime(self):
        print ("Present time =" , self.hours, "hours and" , self.minutes, "minutes")

    def DisplayMinute(self):
        print((self.hours * 60) + self.minutes, "minutes")

a = Time(5,40)
b = Time(11,30)
c = Time.addTime(a,b)
c.displayTime()
c.DisplayMinute()


# 6.Write a Person class with an instance variable, ,
#  and a constructor that takes an integer, , as a parameter. 
# The constructor must assign  to  after confirming the argument passed as  
# is not negative; if a negative argument is passed as , the constructor should set 
#  to  and print Age is not valid, setting age to 0.. 
# In addition, you must write the following instance methods:

class Person:
    def __init__(self,initialAge):
        if initialAge <0:
            self.age= 0
            print('Age is not valid, setting age to 0.')
        else:
            self.age=initialAge
    def amIOld(self):
        if self.age<13:
            print('You are young.')
        elif self.age>=13 and self.age<18:
            print('You are a teenager.')
        else:
            print('You are old.')
    def yearPasses(self):
        self.age+=1
y = int(input())
for i in range(0, y):
    age = int(input())         
    x = Person(age)  
    x.amIOld()
    for j in range(0, 3):
        x.yearPasses()       
    x.amIOld()
    print("")

