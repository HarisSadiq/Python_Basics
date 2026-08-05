str=input("Enter the string:")
#method 1 
from collections import Counter

freq=Counter(str)
print(f"The frequency of each character in the string {str} is: {freq}")

#method 2 
freq={}
for i in str:
     if i in freq:
          freq[i]+=1
     else:
          freq[i]=1
print(f"The frequency of each character in the string {str} is: {freq}")

