a=int(input("Enter the first:"))
b=int(input("Enter the second:"))
c=input("Enter the operator(+,-,*,/,%,**,//):")


if(c=='+'):
   print(f"add={a+b}")

elif(c=="-"):
   print(f"sub={a-b}")

elif(c=="*"):
   print(f"mul={a*b}")
elif(c=="/"):
   print(f"div={a/b}")
elif(c=="%"):
   print(f"rem={a%b}")   
elif(c=="//"):
   print(f"fdiv={a//b}")
else:
   print(f"exp={a**b}")