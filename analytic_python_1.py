print("hello world")
print("this is my first code")


print("""hello world
      this is my first code
      i like it""")

print("hello\nworld")

# a=13
# b=14
# print(a,b)
# temp=a
# a=b
# b=temp
# print(a,b)
a=78
b=87
a=a+b
b=a-b
a=-a+b
print(a,b)

print("-------------------")
hk=4.22
print(int(hk))


print("-------------------")
a=45
print(a**2)

#bitwise operator

print(bin(21))
print(10&8)#And

print(10|8)#or

#XOR operator
print(10 ^ 8)

#zero fill to left shift
print(10>>1)
#zero fill to right shift
print(10<<2)


#Membership Operator
k="helllo"
print("l"in k)

h="helllo"
print("l"not in h)


#Conditional Statment:


#if The STatment
a=6
if(a>=5):
    print("hammad is good boy")
else:
    print("Thank you")
#Nested if statment
marks=77

if marks>=80:
    print("you will get new phone")
    if marks>=95:
        print("you got  a trip")
else:
    print("no phone for a month")

#Short Hand iF statment
#in one line
marks=99
if marks>=90:print("you will gwt a new phone")

marks=89
print("go to a trip")if marks>=90 else print("noo phone for a month")

