a = 5
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b) # float division 
print(a % b) # Remainder
print(a ** b) # a to the power b (a ^ b)

print(a == b)
print(a > b)





a = 20 
b = 40 

a += 10
print("a :", a)

b -= 5
print("b :", b)


#Implicit COnversion
a = 2 
b = 4.25 
sum = a + b  # 2.0 + 4.25 = 6.25
print(sum)

#type casting
a = "2"
b = 4.35
print(a + b)  # error 

a = int("2")
b = 4.35

print(type(a))
print(a + b)

a = float("vaishnavi")  # error -> cannot convert string to float 
b = 4.24

print(type(a))
print(a + b)

a = float("2")
b = 6.3

print(type(a))
print(a + b)

a = 3.14
a = str(a)
print(type(a))
