s=input("enter the string:")
for ch in s:
    if s.count(ch)==1:
        print(ch)
        break
else:
    print("no non repeating character")
