#variable only can contain (a-z) and no.s(0-9) and underscore
#it cant start with numbers
#it can not contain other special characters
#it cannot be predefined functions
#/ is used to get float quotient
#// is used to get integer quotient it gives a flooring value
# * gives us product of numbers
# ** gives us exponent of the number
# e.x: 3*2 gives 6 while 3**2 gives 9 i.e. we get the square of the number
#+= adds the value into itself
#e.x: n = 10, n += n while give us 20 and re-running this will give 40, i.e. the n += n becomes n = n + n, and after first execution the number becomes 20 and after re-running the code gives us 40
# this way you can also use functions like -= , *= , /= , **=, //= ,  %=
#you can also have decrement or increament in number by using += or -= operation i.e you use i += 1     for i in range(1,100) print(i) this will add 1 in i for everytime a loop is performed
m = 0 
m += 1#you can also use other variable for this
#I take it as i still remember comparison operators < , > also for 'is equal to' == is used and for 'is not equal to' != is used i'm sure i'll forget this
for m in range(1,100):
    print(m)

    
z,x = "def" , 5.0
print(z,x) #you can define 2 variable at once like this
#del is used to delete vairable or functions
print("this is a print statement") #this is used to print a statement
input("input a statement") #this is used to take input from user
int(input("this turns string into integer value"))#this turns string into integer value
name = input("enter a statement")
result = len(name)#len() returns number of characters in a statement starting from  zero and also counts spaces as characters
print(f"this statements contains {result} characters")
var = input("enter a sentence")
re = var.find(" ")#var here is a variable and .find is a find command which returns value of first occurance of set character
#if occurance is zero then returned value is -1
print(re)
age = int(input("enter your age "))
print(f"your age is {age}")#if u add f before string in print statement you can call the varible in the string
#if else elif statement
#age varification
your_age = int(input("enter your age: :"))
if your_age >= 18:
    print("you are eligible")
else:
    print("you are not eligible")
#elif is used when u have more than one else sentence
enteer = input("enter your first name")
inf = enteer.find(" ")
if inf == -1:
    print(f"welcome {enteer}")
elif not enteer.isalpha():#isalpha gives true if string contains all alphabetic values and false if it contains non-alphabetic values
    print("your first name cannot have spaces in your name")
else:
    print("your name cannot contain non-alphabetic character")#this will ask you to enter your first name without spaces or numbers
for c in range(1,100):
    print(c)#for loop creates like the name suggests a for loop which will won't break unless a break
#statement is used and range creates a range
#here the statement the output would be numbers from 1 to 100
for d in reversed(range(100)):
    print(d)#the reversed statement will reverse the range and stop at 1 so u dont need to mention the ending point if it's 1/ only works in for loops
    #you can also used reverse statement to reverse a list
vic = int(input("enter a number for arithmetic operation"))#a basic calculator program starts from here 
tim = int(input("enter another number"))
def add():#def if used to create a function and : is needed
    print(f"addition of {vic} and {tim} is ", vic+tim)
def sub():
    print(f"substraction of {vic} and {tim} is ", vic-tim)
def multi():
    print(f"multiplication of {vic} and {tim} is ", vic*tim)
def divide():
    print(f"divison of {vic} and {tim} is ", vic/tim)
print("enter 1 for addition")
print("enter 2 for \substraction")
print("enter 3 for multiplication")
print("enter 4 for division")
choice = int(input("enter the choice"))
if (choice == 1):
    add()#to call the function simply write the name of the function, it doesn't require special notation to call
elif (choice == 2):
    sub()
elif (choice == 3):
    multi()
elif (choice == 4):
    divide()
else:
    print("invalide input ending the programme")
otp = "fffdfsd"
otp[0] = "B" #string becomes immutable when you add [0] infront of a variable
#immutable string is a string which can not be changed
#adv data types-
#List
#Tuple
#Dict
#Set
#1 List:
#[] this is used to define a list
#if can contain int,float,str,list....
#it ordered by default
#it is mutable
#tuple 
#this is ordered
#this is immutable -- you can not change any values
#() is used to create a tuple 
#it can contain int,float,str...
j = (23,35.33,"HELLO")
print(j)
print(type(j))
j[2] = 34
print(j)
l = [("this is a tuple"), [1,"this is a list"], 33 , "this is the main list"]
print(l[1][0])
print(l[1][1][-5:])
#this is how we can fetch data from a list which contains multiple data types
#we can also use this to change values of list (does not apply to tuple)
print(l)
l[1][1] = "this is a real list"
print(l)
t = [('he',['l','l',(89,50.0), 'o',2],8), [1,'PPLAB'],50.0, 'hello']
print(l[-1][-1][-1])
print(l)
p = [11,99,34,78,23.0]
p.sort()#sort is used to sort a list numbers get sorted according to their value, it can only sort integers and float values it does not sort str, tuple and numbers together
print(p)
lo = ["helo", "hi","ha","apple"]
lo.sort()
print(lo)#it can sort strings when list does not contain numbers
lo.pop(2)#pop removes value from the list and returns the list without the targeted value
print(lo)
lo.append("yo")#append adds value to the list at the end of the list
lo.insert(2, "yup")#insert can add value to the list at the given place here the string "yup" will be put at 2nd position
lo.extend('1')#You can use this statement to add string, tuple and list  to the list (you can not add number by themselves but u can add number by putting them in a list) you can convert string into a list
lo.clear#.clear() will empty the list
#dictionary
# it is declared by {}
#it is unordered
#the values in dictionary is in the format: {key:value,key:value,key:value....}
#the key will be immutable and unique
#value can be mutable, immutable and duplicates
#one key can have multiple values
#values can be called by key (key name)
di = {'name':'xyz','age':23,'phn':9345}
print(di['phn'])
print(lo.key())#this will return name of all keys
#lo.clear() will clear the dictionary
print(lo.items())#this will return all items in the dictionary
#you can not use same key twice, if use a key twice in a dictionary the latest given value of the key wil be updated for the first occurance
#although you can not use same key twice but you can use same item as many times as you want this is the duplicate property of dictionary
lo.fromkeys()#will create a dict with iterations and values (will not change the original dict)
#logical operator ---> and ,or, not
#and gives true value when both outcomes are true
#or operator gives true when atleast one outcomes is true 
#not operator : 'not true' == 'false' and 'not false' == 'true'
#non of this special operators are applicable for lists and tuples
#Identity operator ----> is , is not
var1 = 23
var2 = 10
print(var1 is var2)
print( var1 is not var2)
#membership operator ---> in , not in
print('s' in "string") #basically the same thing i used for checking first name
#conditional operators ---> if elif else
# i know how to use this i dont need to write it.
# if elif statement doesnot require () to enter condition
# i know how to use this i dont need to write it.
