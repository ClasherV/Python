"""
print("Hello World")

## O/p: Hello World
"""

"""
print('Hello World')

## O/p: Hello World
"""

"""
print()

## O/p: 
"""

"""
### Coding Exercise on print()

print("First Program - Python print function")
print("It is declared like this:")
print("print('What to print')")

## O/p: First Program - Python print function
##      It is declared like this:
##      print('What to print')
"""

"""
print("Hello World\nHello World\nHello World")

## O/p: Hello World
##      Hello World
##      Hello World
"""

"""
print("Hello"+"Jenny")

## O/p: HelloJenny
"""

"""
print("Hello "+"Jenny")

## O/p: Hello Jenny
"""

"""
print("Hello"+" Jenny")

## O/p: Hello Jenny
"""

"""
print("Hello"+" "+"Jenny")

## O/p: Hello Jenny
"""

"""
### String Manipulation

print("String Manipulation Exercise")
print('String Concatenation is done with "+" sign')
print('eg. print("Hello"+"Jenny")')
print("New lines can be created with a backslash and n")

## O/p: String Manipulation Exercise
##      String Concatenation is done with "+" sign
##      eg. print("Hello"+"Jenny")
##      New lines can be created with a backslash and n
"""

"""
input("What is Your Name: ")

## O/p: What is Your Name: Vaibhav #Enter Your Name here
"""

"""
print("Hello"+" "+input("What is Your Name: "))

## O/p: What is Your Name: Vaibhav
##      Hello Vaibhav
"""

"""
### input() function in Python

print("Hey"+" "+input("What is Your Name: ")+", "+"how are You?")
print("Hey "+input("What is Your Name: ")+",how are You?")

## O/p: What is Your Name: Vaibhav
##      Hey Vaibhav, how are You?
##      What is Your Name: Vaibhav
##      Hey Vaibhav,how are You?
"""

"""
name=input("What is Your Name: ")
print(name)

## O/p: What is Your Name: Vaibhav
##      Vaibhav
"""

"""
a=1
b="Vaibhav"
print(a)
print(b)

## O/p: 1
##      Vaibhav
"""

"""
name="Jenny"
print(name)
name="Jiya"
print(name)

## O/p: Jenny
##      Jiya
"""

"""
print(len("Vaibhav"))

## O/p: 7
"""

"""
name=input("What is Your Name: ")
length=len(name)
print(length)

## O/p: What is Your Name: Vaibhav
##      7
"""

"""
name=input("What is Your Name: " )
print(name)
name="Jiya"
print(name)

## O/p: What is Your Name: Vaibhav
##      Vaibhav
##      Jiya
"""

"""
name=input("What is Your Name: ")
a="Vaibhav"
print(name+a)

## O/p: What is Your Name: Vaibhav
##      VaibhavVaibhav
"""

"""
### Swap 2 Numbers

a=input("Enter the Value of a: ")
b=input("Enter the Value of b: ")
print("\nValue of a before Swapping: "+a,"\nValue of b before Swapping: "+b)
temp=a
a=b
b=temp
print("\nValue of a after Swapping: "+a,"\nValue of b after Swapping: "+b)

## O/p: Enter the Value of a: 10
##      Enter the Value of b: 5
##      
##      Value of a before Swapping: 10
##      Value of b before Swapping: 5
##      
##      Value of a after Swapping: 5
##      Value of b after Swapping: 10
"""

"""
var_1=3
print(type(var_1))

## O/p: <class 'int'>
"""

"""
var_1=12345678901234567890
print(var_1)
print(0b10)
print(0o10)
print(0x10)
print(0o123)
print(0x123)

## O/p: 12345678901234567890
##      2
##      8
##      16
##      83
##      291
"""

"""
var_1=123
var_2=10.1
print(var_1+1)
print(var_2+1)
print(var_1+var_2)
print(type(var_1))
print(type(var_2))

## O/p: 124
##      11.1
##      133.1
##      <class 'int'>
##      <class 'float'>
"""

"""
var_1=0o123
var_2=0x123
var_3=123
print(var_1)
print(type(var_1))
print()
print(var_2)
print(type(var_2))
print()
print(var_3)
print(type(var_3))

## O/p: 83
##      <class 'int'>
##      
##      291
##      <class 'int'>
##      
##      123
##      <class 'int'>
"""

"""
name="Vaibhav Raikwar"
print(type(name))
print(name[0])
print(name[7])

## O/p: <class 'str'>
##      V
"""

"""
name_1="123"
name_2="1"
print(name_1+name_2)
print("123"+"1")

## O/p: 1231
##      1231
"""

"""
print("Jenny\'s \"Lectures\"")
print("Jenny\'s\n\"Lectures\"")
print("Jenny\'s\\n\"Lecture\"")

## O/p: Jenny's "Lectures"
##      Jenny's
##      "Lectures"
##      Jenny's\n"Lecture"
"""

"""
print("Jenny\'s \"Lectures\"")
print("Jenny\'s\n\"Lectures\"")
print(5*"Jenny\'s\\n\"Lecture\"\n")

## O/p: Jenny's "Lectures"
##      Jenny's
##      "Lectures"
##      Jenny's\n"Lecture"
##      Jenny's\n"Lecture"
##      Jenny's\n"Lecture"
##      Jenny's\n"Lecture"
##      Jenny's\n"Lecture"
"""

"""
var=True
print(var)
print(type(var))

## O/p: True
##      <class 'bool'>
"""

"""
a=1
b=2
var=a<b
print(var)
print(type(var))

## O/p: True
##      <class 'bool'>
"""

"""
length=len("Vaibhav Raikwar")
print("Your name has "+str(length)+" characters")
new_length=str(length)
print(type(length))
print(type(new_length))

## O/p: Your name has 15 characters
##      <class 'int'>
##      <class 'str'>
"""

"""
print(int("10")+int("5"))
print(10+float("10"))

## O/p: 15
##      20.0
"""

"""
name="123"
print(10+int(name))

## O/p: 133
"""

"""
### Take 2 Numbers Input from the User and then add them

First_Number=input("Enter the First Number: ")
Second_Number=input("Enter the Second Number: ")
Sum=int(First_Number)+int(Second_Number)
print(Sum)

## O/p: Enter the First Number: 10
##      Enter the Second Number: 5
##      15
"""

"""
### Program to add digits of a Number

Num=input("Enter a two digit Number: ")
Sum=int(Num[0])+int(Num[1])
print(Sum)

## O/p: Enter a two digit Number: 12
##      3
"""

"""
a=4
b=2
print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a/b)
print(a//b)
print(a%b)

## O/p: 6
##      2
##      8
##      16
##      2.0
##      2
##      0
"""

"""
print(5+2*3)
print(5+2*3-1+10/5)
print(5+2*(3-1)+10/5)

## O/p: 11
##      12.0
##      11.0
"""

"""
### Calculate BMI ==> BMI=Weigth(in kg as int)/(Height(in m as float)**2)

Weight=int(input("What is Your Weight (in kg): "))
Height=float(input("What is Your Height (in m): "))
BMI=Weight/(Height**2)
print("Your BMI is",BMI)

## O/p: What is Your Weight (in kg): 48
##      What is Your Height (in m): 1.43
##      Your BMI is 23.47303046603746
"""

"""
a=5
a=a+2
a+=2
print(a)
a=a-2
a-=2
print(a)
b=10
b=b*2
b*=2
print(b)
b=b/2
b/=2
print(b)
c=4
c=c**2
c**=2
print(c)
c=c%2
c%=2
print(c)
d=7
d=d//2
d//=2
print(d)
a,b,c=1,2,3
print(a,b,c)

## O/p: 9
##      5
##      40
##      10.0
##      256
##      0
##      1
##      1 2 3
"""

"""
a=5
print(a<5)
print(a==5)

## O/p: False
##      True
"""

"""
a,b=4,3
c=a+b
a+=2
c+=a
print(c)
c-=a
c/=a
print(c)
c*=a
c//=a
print(c)

## O/p: 13
##      1.1666666666666667
##      1.0
"""

"""
a,b=1,2
c=a+b
print(c)
c+=a
print(c)
c%=b
print(c)
c//a
print(c)

## O/p: 3
##      4
##      0
##      0
"""

"""
a=5
print(a<5,a>5,a>6)
print(a<=5,a>=5,a>=6)
print(a==5,a!=5,a!=6)
print((a+1)!=6)

## O/p: False False False
##      True True False
##      True False True
##      False
"""

"""
a,b=5,4
print(a>4 and b<10)
print(a>4 and b<3)
print(a>4 or b<10)
print(a<4 or b<3)
print(a<4 or b<13)
print(not(a))
"""

"""
a,b=4,3
c=True
print(a<3 and b==3)
print(a<3 or b==3)
print(not(a))
print(not(c))
print(a<=4 and c)
print(a<4 and c)
print(a<4 or c)
"""

"""
a=5
b=4
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<2)
print(a>>2)
"""


