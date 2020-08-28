def larpal(st) : 
    res=[]
    for i in range(len(st)):
        p1=p2=i
        s=m=0
        while p1>=0 and p2<len(st):
            if st[p1]==st[p2]:
                p1-=1
                p2+=1
                s=(p2-p1)-1
            else:
                break
        p1=i
        p2=p1+1
        while p1>=0 and p2<len(st):
            if st[p1]==st[p2]:
                p1-=1
                p2+=1
                m=(p2-p1)-1
            else:
                break
        g=max(s,m)
        res.append(g)
    return max(res)     
t=int(input())
for i in range(t):
    n=int(input())
    st=input()
    print(larpal(st))
