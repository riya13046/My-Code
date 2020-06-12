a = list(map(int,input().split(",")))
#here we sum all the numbers which don't lie between 5 and 8
num1 = sum(a[:a.index(5)])+sum(a[a.index(8)+1:])
print(num1)
#  To concatenate all numbers from 5 to 8
l = a[a.index(5):a.index(8)+1]
num2 = ""
for i in l:
num2+=str(i)
print(int(num2)+num1)
