num=int(input("Enter the  number: "))
a=num
b=num
count=0
while b>0:
    count+=1
    b=b//10
    
total_dig=count
sum=0

while a>0:
    b=a%10
    sum=sum +(b**total_dig)
    a=a//10
    


if sum == num:
    print(f"{num} is an Armstrong number")
   