t = int(input())
while t>0:
    t-=1
    n = int(input())
    arr = list(map(int,input().split()))
    ans = float('inf')
    for i in range(0,n-1,1):
        for j in range(i+1,n,1):
              temp = arr[i]+arr[j]+(j+1)-(i+1)
              ans = min(ans,temp)
    
    print(ans)
