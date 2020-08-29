t=int(input())
for i in range(t):
    n=int(input())
    A = list(map(int,input().strip().split()))[:n] 
    n-=1
    for i in range(n): 
        mini=0 
        for j in range((n-i)+1): 
            if A[mini] < A[j]: 
                mini = j
        print(mini,end=' ')        
        A[mini], A[n-i] = A[n-i], A[mini] 
    print()
