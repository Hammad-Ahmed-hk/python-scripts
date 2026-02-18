# Global Variable
"""variable is container
local variable used only for a small snappet of code cant used same as during function
whereas global can be used"""
#Local Variable
x=24
print("first variable x",x)
def hello():
    x=25
    return x

print(hello())

print(x)

#Global Variable
y=24
print("first variable x",y)
def hello():
    global y
    y=25
    return y

print(hello())

print(y)


    