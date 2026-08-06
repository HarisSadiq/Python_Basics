str=input("Enter a string : ")
freq={}
fr={}
ls=[]
for i in str:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

for key,value in freq.items():
    if value>1:
        fr[key]=value
        ls.append(key)

print(ls)
print(fr)
        


 