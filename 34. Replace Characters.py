s=input("enter the string:")
old=input("enter the  old character:")
new=input("enter the new character:")
result=""
for ch in s:
    if ch==old:
        result+=new
    else:
        result+=ch
print(result)
