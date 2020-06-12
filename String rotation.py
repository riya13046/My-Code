a=input().split(',')
mul=0
l1=[]
for i in a:
   str1=""
   l=[]
   # to separate digits and numbers
   # we can also do it using slicing
   for j in i:
      if j.isalpha():
        str1=str1+j
      elif j.isdigit():
        l.append(j)
   for i in l:
      mul=mul+int(i)*int(i)
   # to check if the addition of square of digit is even or odd
   # if even rotate the string right by 1
   if mul%2==0:
     str1=str1[len(str1)-1::]+str1[0:len(str1)-1:]
   # otherwise rotate it left by 2
   else:
     str1=str1[2::]+str1[0:2:]
   l1.append(str1)
print(",".join(l1))
