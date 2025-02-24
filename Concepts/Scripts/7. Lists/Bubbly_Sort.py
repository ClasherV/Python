a=[2,3,1,7,8,5]
# a="ClasherV"
n=len(a)
for i in range(n-1):
    for j in range(i+1,n):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)

# ((N-1)(N-1+1))/2
# =N(N-1)/2
# =N**2/2-N/2
# =O(N**2)