def rep(num):
    count =0
    i=5
    while(num/i>=1):
        count+=int(num/i)
        i*=5
    return int(count)
t=int(input())
for i in range(t):
    num = int(input())
    print(rep(num))
