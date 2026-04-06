ls=list(map(int,input().split()))
maxi=max(ls)

for i in range (len(ls)):
    if maxi > ls[i]:
        x=maxi
    else:
        maxi = ls[i]
print(maxi)
