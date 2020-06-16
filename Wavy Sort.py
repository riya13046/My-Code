# No of testcases
a=int(input())
for i in range(a):
    # No. of elements in a array
    b=input()
    # Space separated sorted array as input
    c=input().split()
    # Flip numbers in pair of two
    for j in range(len(c)):
        if j%2==0 and j!=len(c)-1:
            t=c[j]
            c[j]=c[j+1]
            c[j+1]=t
#Output
print(" ".join(c))
            
