n=int(input("enter a number:"))
m=0
count=0
for i in range(n):
    m+=1
    if n%m==0:
        count +=1
if n==1:
    print("neither composite nor prime")
elif count <=2:
    print('it is prime')
else:
    print("it is not prime")

