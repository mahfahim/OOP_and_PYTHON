from collections import defaultdict

n = input()
ar = list(map(int,input().split()))
count = defaultdict(int)
for u in ar:
    count[u] = count.get(u,0)+1

ans = 0
for u,v in count.items():
    if(u>v): ans += v
    else: ans += (v-u)

print(ans)

