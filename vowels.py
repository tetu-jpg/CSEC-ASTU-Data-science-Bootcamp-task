ls=["a","e","i","o","u"]
s=input("enter a string :")
count=0
for i in s:
    for j in ls:
        if i==j:
            count+=1
print(count)


