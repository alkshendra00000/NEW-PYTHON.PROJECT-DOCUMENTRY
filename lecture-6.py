"""#perform in function
#how to use function in python
def print_values(a,b):
    sum=a+b
    print("total sum is",sum)
    return sum
print_values(5,10)


#some more code
print_values(10,20)

#more code
print_values(100,200)
#average of 3 numbers
def cal_avg(a,b,c):
         sum=a+b+c
         avg=sum/3
         print("average is",avg)
         print(type(avg))
         return avg

cal_avg(10,20,30)
cal_avg(1,2,3)
cal_avg(21,31,41)

citiy=["delhi","mumbai","kolkata","chennai"]
chennal=["colors","sony","zee","star"]

def print_len(list):
    return len(list)

print(print_len(citiy))
print(print_len(chennal))
#q=2

def print_heros(n):
    fact=1
    for i in range(1,n+1):
        fact *= i
        print(fact)

print_heros(5)
#q=3
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "usd =", inr_val, "INR")
    return inr_val


converter(1)
#q=4
num = int(input("enter a number:"))
def evenodd(num):
    if num % 2 == 0:
        print("even number", num)
    else:
        print("odd number", num)


evenodd(num)
#recursion function
def show(n):
    if n == -1:
        return
    print(n)
    show(n - 1)
    print("end")


show(3)
#q=2 recursive function
def fact (n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n
print(fact(5))
#q=1 recursive function
herose=["thor", "shaktimaan", "hero" , "captain amerkica"]
def calc_sum(n):
    if n == 0:
        return 0
    return calc_sum(n - 1) + n


sum = calc_sum(5)
print(sum)

"""