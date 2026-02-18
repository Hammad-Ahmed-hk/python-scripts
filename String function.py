A="Why fit in,When you are Born to Stand Out!"
print(len(A))
print(A.count("o"))
b=A.lower()
print(b)

c=A.upper()
print(c)\

d=A.title()
print(d)

print(A.find("fit in"))

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# for i in range(1,6):
#     for j in range(6,i,-1):
#         print(i,end=" ")
#     print()


# for i in range(1,6):
#     for j in range(5,i,-1):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print()


# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j,end=" ")

#     print()

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")

    print()
for i in range(5,0,-1):
    for k in  range(0,i-1):
        print("*",end=" ")
    print()



