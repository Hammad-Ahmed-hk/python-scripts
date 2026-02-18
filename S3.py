letter=input("enter a letter")
if letter=="a":
    print("vowels")
elif letter=="e":
    print("vowels",letter)
elif letter=="i":
    print("vowels",letter)
elif letter=="o":
    print("vowels",letter)
elif letter=="u":
    print("vowels",letter)
else:
    print("not a vowels",letter)


nmb=int(input("enter nmb between 5digit range"))
if nmb>=0 and nmb<=9:
    print("one digit nmb")
elif nmb>=10 and nmb<=99:
    print("two digit nmb")
elif nmb>=100 and nmb<=999:
    print("three digit nmb")
elif nmb>=1000 and nmb<=9999:
    print("four digit nmb")
elif nmb>=10000 and nmb<=99999:
    print("five digit nmb")
else:
    print("you exceed the limit,be in limit")
