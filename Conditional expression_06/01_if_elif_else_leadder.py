#if-elif-leadder:
age=int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote.")
elif age<0:
    print("Invalid age entered.") 
elif age==0:
    print("you enter zero which is not correct")
else:
    print("You are not eligible to vote.") 
print("program ended.")
#2
print("____________________________")
number1 = int(input("Enter a number: "))
if number1 > 0:
    print("The number is positive.")
elif number1 < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
