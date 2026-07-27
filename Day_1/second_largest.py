a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
d=int(input("Enter the fourth number: "))
lis=[a,b,c,d]
lis.sort()
num=lis[-2]
print(f"The second largest number is: {num}")

#Method2
largest=max(lis)
print(f"The largest number is: {largest}")
second_lergest=lis[0]
if second_lergest>largest:
    largest=second_lergest
for i in lis:
    if i >= second_lergest and i< largest:
        second_largest=i
print(f"The second largest number is: {second_largest}")

