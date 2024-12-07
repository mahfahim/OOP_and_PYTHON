s = input()
slist = s.split()
rev = []
for u in slist:
    word = u[::-1]
    rev.append(word)

# for u in slist:
#      print(u,end=" ")
# for u in rev:
#      print(u,end=" ")

ans = " ".join(rev)
print(ans)