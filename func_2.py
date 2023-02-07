""""""
"""
Function
write ones and use/call multiple times

syntax:
Declaration
def func_name():
    .
    .
    .

func_name()
---------------------
def sample():
    print('hello')
    
for i in range(5):
    sample()
--------------------------------
Function with arguments:
4 types of arguments in Python
- Positional args
Sequence order matters
Means in declaration if we give a,b,c
and from calling if we supply values 1,2,3
then a = 1
b = 2
c = 3

#Example
def sample(y,x):
    print(x,y)

sample(10,20)
# y = 10 ,x=20
sample('java','python')
# y = java, x=python
--------------
#problem with positional args
name = 'akash'
age = 22

def info(name,age):
    print('Name is', name, 'and age is', age)

info('Nikhil',21) #directly u can supply values
info(name,age) # u can refer vars. to supply values

# sequence is important
info(20,'Rajendra')
# if we change the sequence then it will create a problem in 
#the output
-------------------------------------------------
- Keyword args
we are using args given in the  declaration
for exact reference


def info(name,age,place):
    print(name,age,place)

# with positional args
info('Salman',45,'Mumbai')

# with keyword args
info(age=33,place='Kolhapur',name='Amar')
-----------------------------------
for i in range(10):
    nm = input('Enter your name')
    if nm.isalpha():
        print('Name is:',nm)
    elif (nm.isalnum()== True) or (nm.isdigit()==True):
        print('Numbers are not allowed in name')
    else:
        print('Something wrong is there with name')
        print('Please re enter a name')
-------------------------------------------
def add(x,y,z):
    print(x+y+z)
    
num1 = 10
num2 = 20
num3 = 40
add(num1,num2,num3)
add(x=num3,y = num2,z= num1)
x,y,z = 1,2,3 #packing
add(x=x,y=y,z=z)
--------------------------------------------
- Default args
# default args are used in declaration to assign some fixed values
which user can change as per the need

def test(account='Guest'):
    print('You have',account,'account')

test() #with default value
test('Asif_admin') # new value
test('Pooja')
test(12)
--------------------------------------
# Machine config.
def test(name='Admin',size=8,HDD='1T'):
    print(name,size,HDD)

test()
test('Amit',16,'3T')
test(size=12,name='Ankit',HDD=4)
--------------------------------------

def test(name,size,HDD='1T'):
    print(name,size,HDD)

test('Swarnim',12)
------------------------------------------
- Variable length args
"""















































































