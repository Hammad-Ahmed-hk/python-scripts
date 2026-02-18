#sum of even between 1-50
sum=0
for i in range(1,51):
    if i%2==0:
        sum+=i

print(f"the sum of even number between 1-50 nmb is ={sum}")


print("---------------------------------")
#02:first twenty nmb and there square
for i in range(1,21):
    print(f"{i} and square is = {i**2}")

print("----------------------------")

#sum of 10 odd nmb
sum1=0
n=0
while n<=20:
    if n%2!=0:
        sum1+=n
    n+=1

print(f"the sum of 10 odd nmb is ={sum1}")

print("-----------------------")
#divisible by 8 and 12
for i in range(1,101):
    if i % 8==0 and i%12==0:
        print(i)



