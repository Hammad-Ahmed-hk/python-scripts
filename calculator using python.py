def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def div(a,b):
    if b!=0:
        return a/b
    else:
        return "undefined"
print("select opernd +, - ,* , / ")
a=float(input("enter a number a ="))
op=input("select operand  =")
b=float(input("enter a number b ="))
if op=='+':
    print("sum ot two nmb is =",add(a,b))
elif op=='-':
    print("sub ot two nmb is =",sub(a,b))
elif op=='*':
      print("multiply ot two nmb is =",multiply(a,b))
else:
     print("div ot two nmb is =",div(a,b))
