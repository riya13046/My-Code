st=[]
op=['[','{','(']
clo=[']','}',')']
def check(s):
    for i in range(len(s)):
        if s[i] in op:
            st.append(s[i])
        else:
            last=clo.index(s[i])
            if len(st)>0 and op[last]==st[len(st)-1]:
                st.pop()
            else:
                return i+1
    # if properly nested return 0
    if len(st)==0:
        return '0'
    # otherwise return position of parenthesis disturning the balancing
    else:
        return len(s)+1
s=input()
print(check(s))
