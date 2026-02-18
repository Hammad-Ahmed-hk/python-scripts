a=int(input("enter a number "))
if a>=0:
    print("number is positive")
else:
    print('number is negative')

print("--------------")
b=int(input("enter a number"))
if b%2==0:
    print("number is even")
else:
    print("number is odd")

print("---------")
print("******ARea Calculator*****")
print("""press 1 to get the are of square
      press 2 to get are of rectangle
      press 3 to get area of the circle
      press 4 to get area of trianglr""")

choice=int(input("select one pf the above to find whose area"))
if choice==1:
    side=float(input("enter the length of sides"))
    area=side**2
    print("the area of square is",area )

elif choice ==2:
    length=float(input("enter the length of rectangle"))
    width=float(input("enter the width of rectangle"))
    area=length*width
    print("the area of rectangle is =",area)
elif choice==3:
    radius=float(input("enter the radius of the circle"))
    area=2*3.14*radius
    print("the area of the circle is =",area)
elif choice==4:
    base=float(input("enter the base of rectangle"))
    height=float(input("enter the height of triangle"))
    area=(base*height)/2
    print(":the area of rectangle is =",area)
else:
    print("you choose a wrong number")
