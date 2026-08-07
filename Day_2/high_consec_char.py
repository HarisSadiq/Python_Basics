str=input("Enter the string:")
count=1
dict={}

for i in range(0,len(str)-1):
    if str[i]==str[i+1]:
        count+=1
    else:
        count=1
    if count>1:
        dict[str[i]]=count
max_key=max(dict.keys(),key=dict.get)
print(f"The character with the highest consecutive occurrence is:{max_key} with consecutive occurrence of: {dict[max_key]}")
    
    
    
        


    
    

