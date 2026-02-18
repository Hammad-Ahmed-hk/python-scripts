# # # def max(a,b,c):
# # #     if a>b and b>c:
# # #         return print("a is maximum nmb")
# # #     elif b>c and c>a:
# # #         return print("b is maximum nmb")
# # #     else:
# # #         return print("c is maximum nmb")
    
# # # print(max(6,4,7))
   
# # # print(max(6,11,7))

# # # #python function to create and print list value and square
# # # def create_list():
# # #     l=[]
# # #     for i in range(1,31):
# # #         l.append(i**2)

# # #     return l
# # # print(create_list())


# # #prime or not
# # def check_prime(num):
# #     if num==1:
# #         print("it is not prime")
# #     if num==2:
# #         print("it is a prime nmb")
# #     if num>2:
# #         for i in range(2,num):
# #             if num%i==0:
# #                 print("it is not a prime nmb")
# #                 break
# #     else:
# #         print("its prime nmb")
         

# # check_prime(1)
# # check_prime(2)

# # check_prime(7)
    
# # check_prime(8)


# #sum of nmb in list
# def add(numbers):
#     total=0
#     for i in numbers:
#         total=total+i
#     return (total)
# print(add([12,13,6,9,11,14]))

#fabonci series using recursion
def fs(num):
    if num==1:
        return (0)
    if num==2:
        return (1)
    else:
        return (fs(num-1)+fs(num-2))
    
print(fs(8))
