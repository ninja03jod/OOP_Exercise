""""""
"""
# Assignment : solve 1-1 ex with 4 types of args

# 1) Positional args:
Ex.

class Add:
  def __init__(self,a,b):
    print('Addition is:',a+b)
Add(5,6)


class Oddeve:
  def __init__(self,num):
    if num %2 == 0:
      print(num,'is even number')
    else:
      print(num,'is odd numer')
num = int(input('enter number:'))
Oddeve(num)

class Test:
  def accept(self,maths,sci):
    self.maths = maths
    self.sci = sci
    print('I scored',self.maths,'in mathematics and',self.sci,'in science')
t = Test()
t.accept(95,89)

o/p - Addition is: 11
enter number:6
6 is even number
I scored 95 in mathematics and 89 in science

class Test:
  def accept(self,maths,sci):
    print('I scored',maths,'in mathematics and',sci,'in science')
t = Test()
t.accept(95,89)



class Check:
  def prime(self,num):
    for num in range(25,51):
      if num> 0:
        for i in range(2,num):
          if (num%i == 0):
            break
        else:
          print(num,'is prime number')
c = Check()
c.prime(7)

o/p:
I scored 95 in mathematics and 89 in science
29 is prime number
31 is prime number
37 is prime number
41 is prime number
43 is prime number
47 is prime number
-------------------------------------------------------
# 2) keywords args:

class Info:
  def __init__(self,name,age,salary):
    print('name is:',name)
    print('age is',age)
    print('salary',salary)
Info(age=22,salary=35000,name='saad')

o/p:name is: saad
age is 22
salary 35000

class Chk:
  def __init__(self,num1,num2):
    if (num1 % 5 == 0) and (num2 %2 == 0):
      print(num1,'&',num2,'is divisible by 5 and 2')
    else:
      print('numbers are nt divisible by 5 and 2 ')
Chk(num2=105,num1=328)
Chk(num2 = 88,num1 = 10)

o/p:numbers are nt divisible by 5 and 2 
10 & 88 is divisible by 5 and 2
--------------------------------------------------------
# 3) Default args:
class Test:
  def __init__(self,maths=85,PT='A grade'):
    print('i scored',maths,'in maths')
    print('I also got',PT,'in Physical education')
Test()
Test(PT='B grade')

o/p:
i scored 85 in maths
I also got A grade in Physical education
i scored 85 in maths
I also got B grade in Physical education

class Oddeve:
  def number(self,num=43):
    if num %2 == 0:
      print(num,'is even')
    else:
      print(num,'is odd')
n = Oddeve()
n.number()
n.number(44)

o/p:
43 is odd
44 is even

---------------------------------------------------
# 4) Variable args:
# variable length positional args:
class Test:
  def __init__(self,*a):
    print(a)
Test(69*8,5+6,8-9)

o/p:
(552, 11, -1)

# variable length keywords args:
class Check:
  def __init__(self,**a):
    print(a)
Check(name='saad',capital='mumbai',city='karad')

o/p:
{'name': 'saad', 'capital': 'mumbai', 'city': 'karad'}

"""