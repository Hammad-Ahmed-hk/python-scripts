import random
n= random.randiant(1,100)
a = -1
guesses = 1
while(a !=n):
    
    a = int(input("Guess the number :"))
    if(a>n):
        print("choose lower number ")
        guesses +=1
    elif(a<n):
        print("chose higher nmber ")
    guesses +=1

print(f"congratulation you have guess the exact the number{n} in{guesses} attempts")
