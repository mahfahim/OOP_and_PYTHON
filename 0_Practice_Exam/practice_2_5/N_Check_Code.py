a,b=map(int,input().split())
s = str(input())
flag = True
if(s[a]!='-'): flag = False
for i in range(a):
     if not s[i].isdigit(): flag = False
for i in range(a+1,len(s),1):
     if not s[i].isdigit(): flag = False

if(flag): print("Yes") 
else: print("No") 