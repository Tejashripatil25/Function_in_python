""""""
"""
1) A simple Python function
def sample():
    print('hello')
    
for i in range(5):
    sample()
============================================================================================================
2)
def sample(y,x):
    print(x,y)

sample(10,20)
# y = 10 ,x=20
sample('java','python')
# y = java, x=python
===========================================================================================================
3)
def info(name,age):
    print('Name is', name, 'and age is', age)

info('Nikhil',21) #directly u can supply values
info(name,age) # u can refer vars. to supply values
==========================================================================================================
4)
def info(name,age,place):
    print(name,age,place)

# with positional args
info('Salman',45,'Mumbai')

# with keyword args
info(age=33,place='Kolhapur',name='Amar')
==========================================================================================================
5)
def add(x,y,z):
    print(x+y+z)
    
num1 = 10
num2 = 20
num3 = 40
add(num1,num2,num3)
add(x=num3,y = num2,z= num1)
x,y,z = 1,2,3 #packing
add(x=x,y=y,z=z)
===========================================================================================================
6)
# Machine config.
def test(name='Admin',size=8,HDD='1T'):
    print(name,size,HDD)

test()
test('Amit',16,'3T')
test(size=12,name='Ankit',HDD=4)
===========================================================================================================
7)
def sample(*a):
    print(a)
sample(10)
sample(1,2,3)
sample('Amit',23,45000,'Pune')
# we can supply n values
# it gives a tuple as an output
==========================================================================================================
8)
def sample(**n):
    print(n)

sample(a = 10,b=-10,c=30)
sample()
sample(name='Jyoti',age=33,salary=56000)

# **arg means var. len. keyword argument
# it can accept n number of keywword args
# output will be dict
==========================================================================================================
9)
# we use return to bring something from
# inside to outside the function
def sample():
    # 100 is inside the funct sample
    return 100
num = sample()
print(num)
==========================================================================================================
10)
def test(a,b):
    result = (a +b)**2
    return result
result = test(10,20)
if result > 100:
    print('Perform some operation')
=========================================================================================================
11)
def lab(temp):
    if temp>100:
        return '+ve'
    else:
        return '-ve'
report = lab(90)
print(report)
if report == '+ve':
    print('admit the patient')
else:
    print('Home isolation')
=======================================================================================================
12)
print('Without return')
def sample():
    a = 10

a = sample()
print(a)
print('------------------------')
print('With return')
def sample():
    a = 10
    return a
a = sample()
print(a)
=======================================================================================================
13)
def even(num):
    if num %2 == 0:
        return 'even'
    else:
        return 'odd'
print(even(10))
print(even(9))
=======================================================================================================
14)
#map will apply a func over each element from a sequence
sequence = [2,3,4,5]
def sqr(num):
    return num*num
print(map(sqr,sequence))

print(list(map(sqr,sequence)))
=======================================================================================================
15)
#uses a function to filter the values based on given condition
def filtr(num):
    if num < 0:
        return num
#print(filtr(45))
print(list(filter(filtr,d)))
========================================================================================================
16)
d = [-12,-3,45,6,-18,3,4,5,-6,35,21,25,49]
#PS: return only num divisible by 5 also 7
def check(num):
    if (num % 5==0) or (num % 7==0):
        return num
print(list(filter(check,d)))
=======================================================================================================
17)
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

# You will get correct output because
# argument is given in order
print("Case-1:")
nameAge("Suraj", 27)
# You will get incorrect output because
# argument is not in order
print("\nCase-2:")
nameAge(27, "Suraj")
======================================================================================================
18)
# Python code to illustrate the cube of a number
# using lambda function
def cube(x): return x*x*x

cube_v2 = lambda x : x*x*x

print(cube(7))
print(cube_v2(7))
======================================================================================================
19)
def square_value(num):
#This function returns the square
#value of the entered number
    return num**2
 
 
print(square_value(2))
print(square_value(-4))
==================================================================================================
20)
def add(num1: int, num2: int) -> int:
#Add two numbers.
        num3 = num1 + num2
 
    return num3

# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")
"""
