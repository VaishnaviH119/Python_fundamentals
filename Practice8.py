# Write a program to find the greatest of 3 numbers entered by the user.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if(a >= b and a >= c):
    print("First number is largest", a)
elif(b >= c):
    print("Second number is largest", b)
else:
    print("Third number is largest", c)



# WAP to find the greatest of 4 numbers entered by the user.

# a , b , c , d -> 10, 15, 20 ,5 

# 10 < 15 < 20 > 5

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("ENter fourth number: "))

if(a >= b and a >= c and a >= d):
    print("First number is largest", a)
elif(b >= c and b >= d):
    print("Second number is largest", b)
elif(c >= d):
    print("Third number is largest", c)
else:
    print("Fourth number is largest", d)