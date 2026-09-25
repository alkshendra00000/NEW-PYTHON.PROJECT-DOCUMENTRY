"""with open("practice.text","r") as f:
    data = f.read()
new_data =data.replace ("python","java")
print(new_data)   

with open("practice.text","w") as f:
    f.write(new_data)
word="twlearning"
with open("practice.text","r") as f:
    data=f. read()
    if data.find(word) != -1:
        print("found",word)
    else:
        print("not found",word)
    
def check_for_line():
    word = "restarting"
    data = True
    line_no = 1

    with open("practice.text", "r") as f:
        while data:
            data = f.readline()

            if word in data:
                print(line_no)
                return

            line_no += 1

    return -1


print(check_for_line())

with open("practice.text", "r") as f:
    data = f.read()
    print("coming", data)
    num = ""

    for i in range(len(data)):
        if data[i] == ",":
            if num:
                print(int(num))
            num = ""
        else:
            num += data[i]

    if num:
        print(int(num))"""
count = 0

with open("practice.text", "r") as f:
    data = f.read()
    nums = data.split(",")

    for val in nums:
        if int(val) % 2 == 0:
            count += 1

print("Count value:", count)