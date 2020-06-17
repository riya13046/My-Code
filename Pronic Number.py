#Input a string
a=input()
s=set()
l=[]
str=" "
# To take all substrings of given string
for i in range(len(a)):
    for j in range(i,len(a)):
        l.append(a[i:j+1:])
# To check pronic
for i in l:
    for j in range(1,int(i)//2+1):
        if j*(j+1)==int(i):
            s.add(int(i))
print(sorted(s))


    

        
            
    
