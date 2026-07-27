a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
if a>b and a>c:
    print(f"The largest number is: {a}")
elif b>a and b>c:
    print(f"The largest number is: {b}")
else:
    print(f"The largest number is: {c}")

#Method 2: Using max() function
largest=max(a,b,c)
print(f"The largest number using max() function is: {largest}")
