
def fun(b):
    global m
    if b==sorted(b):
        //we can also use the max function of python instead of this code
        if len(b)>m:
            m=len(b)
    else:
        // Here we can also take the elements of splitted list using for loop but it will unnecessarily increase the complexity of program
        l=b[:len(b)//2:]
        l1=b[len(b)//2:len(b):]
        fun(l)
        fun(l1)
a=int(input())
//To take space separated elements as input
b=list(map(int,input().split()))
m=0
fun(b)
print(m)
        


