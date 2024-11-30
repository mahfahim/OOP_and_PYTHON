x = int(input())
a=0
b=1
if x == 1 : 
    print(a)
elif x == 2 :
    print(b)
else :
    while x > 2:
         temp = a + b
         a = b
         b = temp
         x -=1
    print(b)
       
    