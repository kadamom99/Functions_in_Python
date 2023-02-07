""""""
"""
Lambda function:
lambda parameter:expression

n number of parameters we  can supply
only 1 expression is allowed
-----------------------------------
Q. What is lambda function
Q. What is syntax
Q. why it is anonymous/nameless
Q. how its different from normal function
Q. Similarity between normal function and lambda function
------------------------
s = lambda x,y,z: x+y+z
print(s('C','B','A'))
#using keyword args
print(s(z='C',y='B',x='A'))
------------------------

s = lambda msg,acnt='Guest':msg+' '+acnt
print(s('Good evening'))
print(s('Hello','Salman'))
-----------------------------
Assignment: use variable length args in lambda
------------------------------------------
VVVIMP:Higher order function
========================================
Are functions which require another function as an input
to perform further operations
It has 3 different functions:
1. map(func,iterable/sequence)
- map will apply a func over each element from a sequence
- map has return statement inside
Example:
sequence = [2,3,4,5] funct: square ==> [4,9,16,25]
Solution:-

sequence = [2,3,4,5]
def sqr(num):
    return num*num
print(map(sqr,sequence))

print(list(map(sqr,sequence)))
----------------------------------
#using lambda function

sequence = [2,3,4,5]
sqr = lambda num:num*num
print(map(sqr,sequence))
print(list(map(sqr,sequence)))
----------------------------------
sequence = [2,3,4,5]
print(map(lambda num:num*num,sequence))
print(list(map(lambda num:num*num,sequence)))
--------------------------------------------
d = [-12,-3,45,6,-18,3,4,5,-6]
# PS: Add 100 to -ve numbers
fun = lambda num:num+100 if num<0 else 'positive'
print(list(map(fun,d)))
-------------------------------------------------
nm = ['siddhi','vinayak','ganesh','mandir']

#PS: convert names given into upper case

print(list(map(lambda n: n.upper(),nm)))

print([i.upper() for i in nm])
-----------------------------------
2. filter(function,iterable)
- uses a function to filter the values 
based on given condition
- filter will return only those values,for whom condition is True

d = [-12,-3,45,6,-18,3,4,5,-6]
# PS: filter -ve numbers
def filtr(num):
    if num < 0:
        return num
#print(filtr(45))
print(list(filter(filtr,d)))
-------------------------------
#using lambda
d = [-12,-3,45,6,-18,3,4,5,-6]
# PS: filter -ve numbers
print(list(filter(lambda x:x<0,d)))
----------------------------------------

d = [-12,-3,45,6,-18,3,4,5,-6,35,21,25,49]
#PS: return only num divisible by 5 also 7
def check(num):
    if (num % 5==0) or (num % 7==0):
        return num
print(list(filter(check,d)))
#0--------------------------
print(list(filter(lambda num:num%5==0 or num %7==0,d)))
#----------------------------------------------
fn = lambda num:num%5==0 or num %7==0
print(list(filter(fn,d)))
---------------------------------------------------------
Q. map() vs filter()???
---------------------------------

d = [-12,-3,45,6,-18,3,4,5,-6,35,21,25,49]
fn = lambda num:num%5==0 or num %7==0
# listification gives an iterable list
#result = list(filter(fn,d))
#print(result)

#for loop gives separate element
for val in filter(fn,d):
    print(val)
---------------------------------------------------
3. reduce(function,sequence)
- it not directly availble like map and filter
- it is present in functools module
- it is used to reduce a sequence into a single number/object
- reduce doesnt need typecasting to se the final output
------------------------------------------------
from functools import reduce
d = [-12,-3,45,6,-18,3,4,5,-6,35,21,25,49]
# PS: need sum of all numbers using reduce
# cumulative summation
fn = lambda x,y:x+y
print(reduce(fn,d))

print(sum(d))
-----------------------------------------
"""
d = [-12,-3,45,6,-18,3,4,5,-6,35,21,25,49]
# PS: find out max number from a sequence using reduce
from functools import reduce
print(reduce(lambda x,y:max(x,y),d))



























