# Creating a dictionary in python 

info = {
    "key" : "value",
    "name" : "Vaishnavi",
    "subjects" : ["Python" , "Java" , "C++"],   # List
    "topics" : ("dict" , "set"),   # Tuple
    "age" : 25,
    "is_adult" : True,
    12.99 : 78.9   # Key can be a floating point number.
    # A key can be anything except a List and dictionary as they
    # are mutable i.e. Changeable.

    # A key can be an integer, floating point number, string, (all primitive data types)
    # dictionary or a tuple.

}

null_dict = {}  # empty dictionary (Null dictionary)
null_dict["name"] = "XYZ"
print(null_dict)

print(type(info))

print(info["name"])
print(info["subjects"])
print(info["topics"])
print(info["age"])
#print(info["surname"])   # error 
info["name"] = "Vaishnavi"
info["name"] = 23
info["surname"] = "Helwatkar"
print(info)


#nested dictionary
student = {
    "name" : "rahul kumar",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

print(student)
print(student["subjects"])
print(student["subjects"]["math"])


print(student.keys())   # Outer layer keys are returned in the form of list.
print(list(student.keys()))  # Type casting keys to a list.
print(len(student))   # length of dictionary (Total no. of keys)
print(len(list(student.keys())))

print(list(student.values()))  

print(student.items())      # key value pairs in tuples form 

print(list(student.items()))

pairs = list(student.items())
print(pairs[0])    # Key value tuple pair
print(pairs[1])

print(student["name"])
print(student.get("name"))

#print(student["name2"])  # error -> output
print(student.get("name2"))  # None -> output

print("BEFORE")
#print(student["name2"])  # Error 
print("AFTER")   # This will not get executed as because of the error in the above line.


student.update({"city" : "Delhi"})
print(student)

new_dict = {"name" : "Neha Kumar", "age" : 16}
student.update(new_dict)
print(student)