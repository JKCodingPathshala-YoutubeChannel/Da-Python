num=int(input("Enter the number:"))

count=0
x=num
while x!=0:
   x=x//10
   count+=1

y=num
sum=0
while y!=0:
   d=y%10
   sum=sum+d**count
   y=y//10
  
if sum==num:
   print("AN")
else:
   print("nan")
  



