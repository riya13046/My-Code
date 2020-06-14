a=input()
c=0
l=[]
l1=[]
l2=[]
# To separate digit and count number of special symbols in string
for i in a:
    if i.isalnum()==False:
        c=c+1
    elif i.isdigit()==True:
        l.append(i)
# To separate even and odd numbers
for i in l:
    if int(i)%2==0:
        l1.append(i)
    else:
        l2.append(i)
i=0
j=0
str=" "
#if special chars are even the series starts with even followed by odd
if c%2==0:
  while i!=len(l1) or j!=len(l2):
      if i<len(l1) and j<len(l2):
          str=str+l1[i]+l2[j]
          i=i+1
          j=j+1
      elif i==len(l1) and j<len(l2):
          str=str+l2[j]
          j=j+1
      elif i<len(l1) and j==len(l2):
          str=str+l1[i]
          i=i+1
# if odd then series starts with odd followed by even
else:
    while i!=len(l1) or j!=len(l2):
      if i<len(l1) and j<len(l2):
          str=str+l2[j]+l1[i]
          i=i+1
          j=j+1
      elif i==len(l1) and j<len(l2):
          str=str+l2[j]
          j=j+1
      elif i<len(l1) and j==len(l2):
          str=str+l1[i]
          i=i+1

print(str)          
          
           
    
