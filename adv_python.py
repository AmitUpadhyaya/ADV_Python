# 1. 	 Write a program to Python find the values which is not divisible 3 but 
# is should be a multiple of 7. Make sure to use only higher order function.

a=[i for i in range(100) if(i%3!=0) and (i%7==0)]
print(a)

#2. 	Write a program in Python to multiple the element of list by itself 
# using a traditional function and pass the function to map to complete the operation.

a= [1,2,3,4,5,6]
res= map(lambda i:i*i,a)
print(res)

#3. 	Write a program to Python find out the character in a string which is 
# uppercase using list comprehension.
b=[i for i in "ConSulTadd" if i.isupper() ]
print(b)

#4. 	Write a program to construct a dictionary from the two lists 
# containing the names of students and their corresponding subjects. 




#6. 	Write a program in Python using generators to reverse the string. 
# Input String = “Consultadd Training”

def rev_str(my_str):    
    for i in range(len(my_str)- 1, -1, -1):
        yield my_str[i]


# For loop to reverse the string
for char in rev_str("Consultadd Training"):
    print(char)

# 7. 	Write any example on decorators.

def deco(msg):
    print(msg)

def deco2(msg):
    print(msg)

deco("awesome function")

deco2 = deco
deco2(" with great features")



#8. 	Write a program to handle an error if the user entered the number more than
#four digits it should return “Please length is too short/long !!! 
# Please provide only four digits”


try:
    data= int(input("Enter a no. : "))
    if data>9999:
        print("Please length is too short/long !!! ")
    else:
        print("number is ok")    
except:
    print("please provide number not digits or alphanumeric letter")

#9. 	Create a login page backend to ask user to enter the UserEmail and password.
# Make sure to ask Re-Type Password and if the password is incorrect give chance to
# enter it again but it should not be more than 3 times.

# user=input("enter a useremail: ")
# pas=input("enter a password: ")
# repas=input("enter your password again: ")

# count=0
# while True:
#     for i in pas:
#         if i==repas:
#             print("yes")
#         else:
#             repas=input("enter your password again: ")
#     break    

count=0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='amit123' and username=='consultadd':
        print('Access granted')
        break
    else:
        print('Access denied. Try again.')
        count += 1

    


