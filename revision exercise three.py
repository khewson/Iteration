#Kim Hewson
#09/10/14
#revision exercise #3
num = 0
user_input=int(input("Please enter how many numbers are to be averaged"))

for count in range (user_input):
    num= num + int(input("Please enter a number"))
    average=num/user_input
print(average)
    
