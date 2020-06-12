a=input().split(',')
str2=""
for j in a:
  str1=""
  l=[]
  # to separate digits and numbers
  for i in j:
    if i.isdigit()==True:
        l.append(i)
    elif i.isalpha()==True:
        str1=str1+i
  l1=list(map(int,l))
  l1.sort()
  l1.reverse()
  m=min(l1)
  # if length of name given is present in  number than return letter at that position
  if len(str1) in l1:
       str2=str2+str1[len(str1)-1]
  else:
      for i in l1:
        #otherwise print letter at position less than length
         if i<len(str1) and i>=m:
             m=i
             n=str1[m-1]
             break
          # if there is no number less than length of name return 'X'
         else:
             n='X'
      str2=str2+n
print(str2)
     
