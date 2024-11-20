n,q = list(map(int,input().split()))
a = list(map(int,input().split()))
sum = [0]*(n+2)
for i in range(n) :
    sum[i+1]=sum[i]+a[i]

for i in range(q):
    x,y = list(map(int,input().split()))
    x-=1
    print(sum[y]-sum[x])
    