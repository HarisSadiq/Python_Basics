a=int(input("Enter the Integer to create a reverse of it (ex:1234): "))

while a>0:
    b=a%10
    print(b,end="")
    a=a//10

