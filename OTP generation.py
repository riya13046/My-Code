# string of numbers as input for 4 digit OTP generation
a=input()
str1=""
str2=""
# to iterate through the string
for i in a:
    # to ignore number if it is even
    if int(i)%2==0:
        continue
    #else for odd number square it
    else:
        b=int(i)*int(i)
        str1=str1+str(b)
for i in range(len(str1)):
    if len(str2)!=4:
       str2=str2+str1[i]
print(str2)        
