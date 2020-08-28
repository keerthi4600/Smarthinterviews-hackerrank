from sys import stdin,stdout
t=int(stdin.readline())
lst=[1]*1000001
for i in range(1,1000000+1):
    lst[i]=((lst[i-1])%(10**9+7))*i
    lst[i]=lst[i]%(10**9+7)
for i in range(t):
    n=int(stdin.readline())
    stdout.write(str(lst[n])+'\n')
