"""
str1="Hello, World!"
str2="Python is fun."
str3=str1+" "+str2
print(len(str3))
str4= "Python is a programming language.\t It is widely used for web development, data analysis, artificial intelligence, and more."
print(str4)
str1="Hello, World!"

print(str1[5])
str1="apna college"
ch=str1[5:len(str1)]
print(str1[1])
print(ch)
str=" apna college"
print(str[:6])#[0:6]
print(str[6:])#[6:12]
str = "apna college"
print(str[-7:-1])#[-7:-1]

str="tow are fake"
str=str.capitalize()
print(str)
print(str.endswith("ki"))

str = "you are fake"
print(str.replace("fake","cute"))
print(str.count("you"))

#let's practice
str=input("enter your frist name:")
print("this is your frist name length",len(str))
str = "this is my first '$' rupees "
print(str.find("$"))

age=16

if(age >= 18):
    print("you can vote and apply for licence")

age=16
if(age >= 18):
    print("yes you are adult . and you can vote now")
else:
    print("you are not adult yet . you can not vote now")
"""

"""
light = "green"
if(light == "red"):
    print("you can go stop")
elif(light == "yellow"):
        print("you can go look")
elif(light == "green"):
        print("you can go now")

marks=int(input("enter your marks:"))
if(marks >= 90):
    grade="A"
elif(marks >= 80 and marks < 90):
    grade="B"
elif(marks >= 70 and marks < 80):
    grade="C"
else:
    grade="f"
print(" grade of your student ->",grade)

age=int(input("enter your age:"))
if(age >= 18):
    if(age >= 80):
        print("you can not drive")
    else:
      print("you can drive ")
else:
    print("you can not drive")

num=int(input("enter your number:"))
if(num%2==0):
    print("this is even number") 
else:
    print("this is odd number")
    
num1=int(input("enter your first number:"))
num2=int(input("enter your second number:"))
num3=int(input("enter your third number:"))
if(num1>=num2 and num1>=num3):
    print("num1 is the largest",num1)
elif( num2>=num3):
    print("num2 is the largest",num2)
else:
    print("num3 is the largest",num3)
    """
num=int(input("enter your number:"))
if(num%7==0):
    print("this number is divisible by 7:",num)

else:
    print("this number is not divisible by 7:",num)