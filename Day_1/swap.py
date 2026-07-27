a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(f"Before swapping: a = {a}, b = {b}")
#Method 1: Using a temporary variable
temp=a
a=b
b=temp
print(f"After swapping using temporary variable: a = {a}, b = {b}")

#Method 2
a , b = b , a
print(f"After swapping using tuple unpacking: a = {a}, b = {b}")

#Method 3: Using arithmetic operations
a=a+b
b=a-b
a=a-b
print(f"After swapping using arithmetic operations: a = {a}, b = {b}")




                                                            