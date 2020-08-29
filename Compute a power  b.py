def power(a,b):
    if b==0: return 1
    t=power(a,int(b/2))
    if b%2 == 0:
        return (t*t)%1000000007
    else:
        return (a*t*t)%1000000007
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    print(power(a,b)%1000000007)
