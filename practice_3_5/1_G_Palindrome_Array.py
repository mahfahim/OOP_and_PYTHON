n = int(input())
a = list(map(int,input().split()))
# for i in range(n):
#    a.append(int(input()))

b = []
for i in range(-1,-(n+1),-1):
   b.append(a[i])

flag = True
for i in range(n):
   if(a[i] != b[i]):
      flag = False

if(flag): print("YES")
else: print("NO")

