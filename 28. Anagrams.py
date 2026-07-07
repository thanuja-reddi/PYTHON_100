s1=input("enter the first string:")
s2=input("enter the second string:")
if len(s1)!=len(s2):
    print("Not Anagrams")
else:
    count=0
    for ch in s1:
        if ch in s2:
            count+=1
    if count==len(s1):
        print("Anagrams")
    else:
        print("Not Anagrams")
            
