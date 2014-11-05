#Kim Hewson
#09/10/14
#revision exercise #4

num=float(input("Enter a number between 10 and 20"))
while num<10 or num>20:
    print("The value you entered has not been accepted")
    num=int(input("Please enter another number"))
else:
    print("The number you entered has been accepted")
    
    
