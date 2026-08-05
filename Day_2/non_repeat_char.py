str=input("Enter the string")
ls=[]
freq={}
for i in str:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

for j,k in freq.items():
    if k==1:
        ls.append(j)
print(ls)
    
