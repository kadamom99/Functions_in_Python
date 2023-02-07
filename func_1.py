
 """"""
"""
Function: it a unit which is used to combine an operations with a 
specific purpose
so we can declare it ones and call it multiple times
-----------------------
Traditional approach of a programming

num = -10
if num>0:
    print(num,'is +ve')
else: print(num,'is -ve')

num = 7
if num>0:
    print(num,'is +ve')
else: print(num,'is -ve')
-------------------------------------

Advantage of a function is: Code re-usability

It works on the principle of
declare/write ones and call multiple times

it contains 2 steps
1. declaration of a function
# syntax

def function_name():
    logic
    .
    .
    
2. Calling of a function
Syntax: 
function_name()

function_name can be like any valid identifier
----------------------------------------------
# declaration
def identify(num):
    if num > 0:
        print(num, 'is +ve')
    else:
        print(num, 'is -ve')

identify(11)
identify(-3)
identify(77)
identify(-22)
for i in range(4):
    print(i,end=' ')
print('------------------')
print('hello')
identify(0)
identify(99)
identify(-8)
----------------------------------------------
2 types of functions we have in python
- Built in function
a function provided by python itself
a function which is made available by python

Example:
print()
id()
len()
sorted()
min()
sum()

These are from python itself hence user cant use these names
to implement

-------------------
We cant use keywords as a function name
---------
def in():
    print('in function')
----------------------------------
- User defined functions
a function which is create by a user as per the requirement

in case of this
first we need to declare a function
then
we need to call that function to see the output
------------------------------
def sample():
    print('Hello all')
    print('Sample function')

    # to get output , calling is must AT THE SAME LEVEL
    # WHERE FUNCTION IS DECLARED
    #sample()
    #sample()

# calling must be outside
sample()
-----------------------------------------
We can use an empty function
or
 a function without arguments
------------
def sample(): # no arguments
    pass
sample()

def test(): # no arguments
    print('addition is:',400+100)
test()

# function without argument means declaration brackets() are empty

---------------------------
def sample():
    ...
sample()
---------------------------
s = 'hello anuj'
# can we add int to a string
'hello anuj10'
num= 10
print(s+str(num))
----------------------------
#print(help(str.format))
name = 'Ramesh'
age = 20
# format specifiers
# %d is for int
# %f is for float
# %s for string
print('name is {} age is {}'.format(name,age))

print('name is {} age is {}'.format(age,name))

print('name is {1} age is {0}'.format(age,name))

print(f'name is {name} age is {age}')
=================================================
"""
































