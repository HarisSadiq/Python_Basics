num=int(input("Enter the number for fibonachi series: "))

if num<=1:
        print(num)
else:
        a=0
        b=1
        print(a)
        print(b)
       

        for i in  range (1,num+1):
            c=a+b
            print(c)
            a=b
            b=c
            

            