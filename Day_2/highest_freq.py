str=input("Enter a string:")
# Count the frequency of each character in the string
freq={}
for i in str:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(f"The frequency of each character in the string {str} is: {freq}")

#maximum frequency character
max_key=max(freq.keys(), key=freq.get)

print(f"The character with the highest frequency in the string {str} is: {max_key} with frequency: {freq[max_key]}")





