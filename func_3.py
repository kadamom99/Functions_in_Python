""""""
"""
Types of Arguments:
- Positional 
- Keyword
- Default 
- Variable length args
1. Variable len. positional args

def sample(*a):
    print(a)
sample(10)
sample(1,2,3)
sample('Amit',23,45000,'Pune')
# we can supply n values
# it gives a tuple as an output
--------------------------------------

def test(*args):
    print(args)
test()
test(10,20)
test('A','B','C')
-------------------------------------
2. Variable len. keyword args

def sample(**n):
    print(n)

sample(a = 10,b=-10,c=30)
sample()
sample(name='Jyoti',age=33,salary=56000)

# **arg means var. len. keyword argument
# it can accept n number of keywword args
# output will be dict
--------------------------------
def test(**kwargs):
    print(kwargs)
test(x =1,y=2,z=3)
#------------------------------------------]
Q. What is difference between *args and **kwargs
*args                           **kwargs
tuple                          dict
positional args                 keyword args
*                                  **
Immutable                       mutable
------------------------------------------------
General questions
-------------------
a = 'nitin'
print(list(a))
print(list(reversed(a)))
if list(a) == list(reversed(a)):
    print('its palindrome')
#----------------------
if a == a[::-1]:
    print('palindrome')
------------------------------------
- Built in functions (print,id,len,type)
- User defines functions 
"""
# max,min
a = [1,29,30,100,0,-1]
print(max(a))
print(min(a))
print(list(enumerate(a)))
print(sorted(a)) # gives temp. output
print(a)
#IMP Q. sort vs sorted?????
print(list(reversed(a)))
#IMP Q. reverse vs reversed??

















































