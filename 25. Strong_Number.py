num=int(input("enter the number:"))
sum=0
temp=num
while num>0:
    digit=num%10
    fact=1
    for i in range(1,digit+1):
        fact*=i
    sum+=fact
    num=num//10
if sum==temp:
    print(temp,"is a strong number")
else:
    print(temp,"not a strong number")
    
    
