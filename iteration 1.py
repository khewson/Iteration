#Kim Hewson
#09/10/14
#program to prompt for 8 numbers and report the total to the user

num=0
for count in range (1,9):
    add=int(input("Enter number {0}: ".format(count)))
    num=num+add
print(num)    
