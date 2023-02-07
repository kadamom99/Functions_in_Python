""""""
"""
Function aliasing:
Q. What is function aliasing
giving a new name or a reference to already present function
-------------------------------------------
def add():
    print(20+30)

add()
# now will assign a new name
a = add
print(a)
print(add)
a()
a()
a()
---------------------------------------------
Nested function: function inside a function

def outer():
    print('Outer calling')
    def inner():
        print('Inner calling')

    inner()
outer()
------------------------
def outer():
    print('Outer calling')
    def inner():
        print('Inner calling')
    # rather than calling inner 
    # return inner reference
    return inner 

outer()
inner()
-------------------------------
return: we write return keyword inside a function
it returns the given object in front of it

# we use return to bring something from
# inside to outside the function
def sample():
    # 100 is inside the funct sample
    return 100
num = sample()
print(num)
----------------
Example 2

def test(a,b):
    result = (a +b)**2
    return result
result = test(10,20)
if result > 100:
    print('Perform some operation')
----------------------
Example 3

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
-----------------------------------
# when there is no return so its return value is None
------------------------------
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
-----------------------------

print(print('hi')) # print doesnt have return
print(id(10)) # id has return

--------------------------------
Now, if i want to fetch inner function outside
so i can call it multiple times
----------------------------------
def outer():
    print('Outer calling')
    def inner():
        print('Inner calling')
    # rather than calling inner
    # return inner reference
    return inner

inner = outer()
inner()
inner()
outer()
------------------------------
def omkar():
    print('I am Omkar')
    def shubham():
        print('I am Shubham')
    #shubham()
    return shubham #refer shubham outside via omkar calling
shubham = omkar()
print(shubham)
shubham()
shubham()
shubham()
-----------------------------------------
Q. What is significance of return in python?
- to bring inside objects, outside
===================================================
Anonymous function/Lambda function/ Nameless function:

Use: it is usd to write a function in short code
or
it gives u same operation with lesser lines of code

It is exactly same as that of normal function
except it has different syntax
it has default return present 
We can use lambda function directly as an input function 
to supply in higher order function

Syntax:
lambda parameter/s:expression

lambda is a keyword
we can supply 1 or many parameters
We can use only one expression
-------------------------------
lets see implementation of Squaring the number using normal 
function and lambda function
----------------------
# normal function
def sqr(num):
    return num**2
# if u want to see the output of a fucntion with return
# then use print function or take another variable to store the result
#and check it later
#out = sqr(10)
#print(out)
#----------------------
print(sqr(10))
------------------------------
# lambda function
sqr = lambda num:num**2
print(sqr(25))
print('lambda:',sqr)

def sqr(num):
    return num**2
print('normal:',sqr)
-------------------------------------
# Can we return multiple expressions


# in lambda function only one expression is allowed 
#sqr = lambda num:num**2,num+100,num*10
#print('lambda:',sqr(25))

# but we can use one trick to return multiple Expressions
sqr = lambda num:[num**2,num+100,num*10]
print('lambda:',sqr(25))
----------------------------------------
# in normal function we can return multiple values
def sqr(num):
    return num**2,num+100,num*10
print('normal:',sqr(25))
# unpacking
sq,add,mul = sqr(25)
print(sq)
print(add)
print(mul)
------------------------------------------
# we can use if else ONLY

def even(num):
    if num %2 == 0:
        return 'even'
    else:
        return 'odd'
print(even(10))
print(even(9))

# lambda function using ternary operator
test= lambda num: 'even' if num%2 == 0 else 'odd'
print(test(5))
print(test(20))
-----------------------------------------
"""
def show(name):
    return name.upper(),name.title(),name.capitalize()
#print(show('rimi chauhan'))
# unpacking
a,b,c = show('rimi chauhan')
print(a)
print(b)
print(c)

















































