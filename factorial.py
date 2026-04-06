n=int(input('enter positive number starting from 0:'))
m=1

if n==1 or n==0:
    m=1
else:
    while n>1:
        x= n * (n-1)
        m =m * x
        n=n-2
print(m)
