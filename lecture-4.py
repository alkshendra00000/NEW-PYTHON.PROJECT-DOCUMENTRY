#dictionary & set example
#dictionary example
"""info={
    "name":"alkshendra",
    "age":20,
    "gender":"male",
    "subjects":["python","java","c++"],
    "topics":["data structures","algorithms","database"],
    "is_adult":True,
    "marks":94
}

info["name"]="Alkshendra Kumar"
info["idealname"]="airtal"
print(info)
student={
    "name":"Alkshendra",
    "subjects":{
        "python":85,
        "java":90,
        "c++":88
    }
}
student.update({"age":20})
print(student)
#set example
collection=set()#empty set
collection.add(1)
collection.add(2)
collection.add(3)
collection.add("alkshendra")
collection.add((1,2,3))
collection.remove(3)

collection.pop()
print(collection)
collection={"hi","kaon","kiyuki"}
print(collection.pop())
print(collection.pop())
print(collection.pop())
print(collection.pop())#error because set is empty
#lets practice
mydict={
    "table":["a piece of furniture","list of facts or figures"],
    "cat":"a small animal"
}
print(mydict)
students={}
marks1=int(input("Enter marks of physics:"))
marks2=int(input("Enter marks of chemistry:"))
marks3=int(input("Enter marks of biology:"))
students.update({"physics":marks1})
students.update({"chemistry":marks2})
students.update({"biology":marks3})
print(students)
values={
    ("float",9.0),
    ("int",9)
}
print(values)
print(type(values))"""