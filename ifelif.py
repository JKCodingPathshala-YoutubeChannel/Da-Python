# year=int(input("Enter the year:"))

# if(year%400==0 or (year%4==0 and year%100!=0)):
#      print("Leap year")

# else:
#      print("Not leap year")


# marks=int(input("Enter the marks:"))

# if(marks>=95):
#   print("A+")
# elif(marks>=85):
#   print("A")
# elif(marks>=75):
#   print("B")
# elif(marks>=65):
#   print("c")
# elif(marks>=55):
#   print("d") 
# elif(marks>=45):
#   print("E")
# else:
#   print("Fail")

# num=int(input("Enter the number"))

# if(num%3==0 and num%5==0 ):
#   print("Number is divisble by 3 and 5")
# else:
#   print("Number is not divisble by 3 and 5")


# ch=input("Enter the char:")

# if ch in 'aeiouAEIOU':
#   print('vowel')

# else:
#   print('consonat')


# color=input("Enter the color:").lower()


# if color=='red':
#   print("Stop")
# elif color=='green':
#   print("go")
# elif color=='yellow':
#   print('ready')
# else:
#   print("invalid...")

# amount=int(input("Enter the amount:"))
# currbal=500

# if(amount>currbal):
#    print("Insufficient balance")
# else:
#    currbal=currbal-amount
#    print("withdraw sucessfully")
#    print("current balance:",currbal)


username=input("Enter the username: ")
password=input("Enter the password: ")


if(username=="admin" and password=="pass@123"):
   print("login successfully")
else:
    if(username!='admin'):
        print("invalid username")
    elif(password!='pass@123'):
        print('invalid password')
     
    print("inavlid login ")
        
   

