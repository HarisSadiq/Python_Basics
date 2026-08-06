str=input("Enter a string :")
freq={}
for i in str:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(f"The frequency of each charater:\n {freq}")

for key,value in freq.items():
    if value==1:
        print(f"The first non repeating character in string:{str} is {key}")
        break

