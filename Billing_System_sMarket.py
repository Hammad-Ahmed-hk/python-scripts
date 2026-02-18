while True:
    name=input("Enter your name = ")
    total=0
    while True:
        print("enter the amount and quantity = ")
        quantity=float(input("enter quantiity = "))
        amount=float(input("enter amount of item = "))
        total+=amount*quantity
        repeat=input("do you want another thing?(yes/No)")
        if repeat=="no" or repeat=="No":
            break
    print("-"*40)
    print("Name:=",name)
    print("amount to be paid:= ",total)
    print("-"*40)
    print("*********Happy Shoping*********")

    repeat1 = input("do you want to go to next customer? (yes/no)")
    if repeat1=="no" or repeat1=="No":
        break

