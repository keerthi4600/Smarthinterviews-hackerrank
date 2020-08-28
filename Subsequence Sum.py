import bisect 
def generateSubsets(start, setSize, S, res): 
    pow_setSize = pow(2, setSize) 
    add = 0
    for counter in range(pow_setSize): 
        add = 0
        for j in range(setSize): 
            if counter & (1 << j): 
                add += S[j + start] 
        res.append(add)           
def numberOfSubsets(S, N, A, B): 
    S1 = [] 
    S2 = [] 
    generateSubsets(0, N // 2, S, S1) 
    if (N % 2 != 0): 
        generateSubsets(N // 2,N // 2 + 1, S, S2) 
    else: 
        generateSubsets(N // 2,N // 2, S, S2) 
    S2.sort() 
    ans = 0
    for i in range(len(S1)): 
        low = bisect.bisect_left(S2, A - S1[i]) 
        high = bisect.bisect_right(S2, B - S1[i]) 
        ans += (high - low) 
    return ans 
t=int(input())
for i in range(t):
    n,a,b =map(int,input().split())
    lst=list(map(int,input().strip().split(' ')))[:n]
    print(numberOfSubsets(lst, n, a, b)) 
