s=input("enter the string:")
count=0
for ch in s:
    if ch in "aeiouAEIOU":
        count+=1
print("No of Vowels:",count)
