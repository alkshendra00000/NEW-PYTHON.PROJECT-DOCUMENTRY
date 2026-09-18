#loops
"""i=1
while i<=100000:
    print("This will print forever until you stop it.", i)
    i += 1
    print(i)
#lets practice
i=1
while i<=10:
    print(5 * i)
    i += 
tuple=(1,4,16,25,36,49,64,81,100)
x=36
i=0
while i<len(tuple):
    if( tuple[i]==x):
        print("Found",x,"at index",i)
        break
    else:
     print("finding...")
    i += 1
i=1
while i<=10:
    if(i%2!=0):
        i += 1
        continue
    print(i)
    i += 1
str="hello world"
for i in str:
    print(i)
else:
 print("thanks for coding")
#for loop practice
tuple=[1,4,16,25,36,49,64,81,100]
x=36
for i in tuple:
    if(i==x):
        print("Found",x ,"value of i is",i)
        
    else:
        print("finding...")
#range function

for i in range(2,101,2):
    print(i)
#let,s practice
for i in range(1,11):
    print(5*i)"""
n=5
sum=1
for i in range(3,n+1):
    sum *= i
print("total sum factorial of",sum)