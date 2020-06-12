def fun(b):
    global m
    if b==sorted(b):
        if len(b)>m:
            m=len(b)
    else:
        l=b[:len(b)//2:]
        l1=b[len(b)//2:len(b):]
        fun(l)
        fun(l1)
a=int(input())
b=list(map(int,input().split()))
m=0
fun(b)
print(m)
        


