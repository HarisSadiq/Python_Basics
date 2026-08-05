str=input("Enter a string")
# Reverse string

rev_str=str[::-1]
print(f"The reverse of the string {str} is: {rev_str}")

#Method 2

r_str=""
for i in str:
    r_str=i+r_str
print(f"The reverse of the string {str} is: {r_str}")

#Method 3
for i in range(len(str)-1,-1,-1):
    print(str[i],end="")

