n=int(input())
a=input().split()
c=0
# To remove n number of elements
for i in range(n):
    a.remove(a[0])
# to remove elements which are repeating
b=set(a)
# to count elements remaining
for i in b:
    c=c+1
print(c)

    
