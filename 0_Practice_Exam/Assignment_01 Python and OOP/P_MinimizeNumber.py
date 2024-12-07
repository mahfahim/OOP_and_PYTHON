n = int(input())
arr = list(map(int,input().split()))
ans = 100000005
cnt = 0
for i in range(n):
    while arr[i]%2 == 0 :
          cnt += 1
          arr[i] /=2

    ans = min(ans,cnt)
    cnt=0

print(ans)
           