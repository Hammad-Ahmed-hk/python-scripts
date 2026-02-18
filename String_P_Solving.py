# # # a = "OOTD.YOLO.ASAP.BRB.GTG.OTW"
# # # #01:seprate by comma
# # # b = a.split(".")
# # # print(b)

# # # k=input("enter any string:=")
# # # o=sorted(k)
# # # print(o)

# # # z="hello" 
# # # b=z.replace("l","")
# # # print(b)

# # # g="F.R.I.E.N.D.S"
# # # j=g.replace(".","")
# # # print(j)

# # # print("_____---part:02_______---")

# # # s=input("enter any string:=")
# # # print(s)
# # # print(s[::-1])


# # #write a program to check string contain digit
# # a=input("enter any string:=")
# # b=(a.isdigit())
# # if b==True:
# #     print("yes string contain only digit")
# # else:
# #     print("string can not have only digit")




# # a=input("enter a string to chech is it palindrom or not:=")
# # # print(a)
# # rev=a[::-1]
# # if a==rev:
# #     print("string is palindrome")
# # else:
# #     print("string is not palindrome")



# print("----------------")
# a=input("enter a string:=")
# Vowels=0
# for i in a:
#     if i=="a" or i=="A" or i=="e" or i=="E" or i=="i" or i=="I" or i=="o" or i=="O" or i=="u" or i=="U":
#         Vowels+=1

# print(f"the number of vowels in string is :+{Vowels}")

a=input("enter a string:=")
b=(a.istitle())
if b==True:
    print("yes every word start with capital letter")
else:
    print("not start with capital letter")
