s = str(input())
cL = 0
cR = 0
count = 0
st = []
ans =[]


for i in range(0,len(s),1):
        st.append(s[i])
        if s[i]=='L': 
            cL+=1
        elif s[i]=='R':
            cR+=1
        if cL == cR:
           count+=1
           ans.append(''.join(st))
           st=[]
           cL=0
           cR=0


print(count)
for i in range(0,len(ans),1):
        print(ans[i])
              