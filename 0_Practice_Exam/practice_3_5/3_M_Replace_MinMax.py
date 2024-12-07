n = int(input())
a = list(map(int,input().split()))

mx = max(a)
mn = min(a)
b = a
for i in range(n):
    if a[i] == mx:
        b[i]=mn
    elif a[i] == mn:
        b[i]=mx
for i in range(n):
    print(b[i],end=" ")
