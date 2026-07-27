a=int(input("Enter the starting number: "))
b=int(input("Enter the ending number: "))

prime=[]

for i in range (a,b+1):
    count=0
   
    


    for j in range(1,i+1):
        if i%j ==0:
            count+=1
    if count==2:
        prime.append(i)
             
     
print(f"The prime numbers between {a} and {b} are: {prime}")
        
