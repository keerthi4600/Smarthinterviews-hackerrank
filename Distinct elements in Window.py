from collections import defaultdict 
def countDistinct(arr, k, n): 
    mp = defaultdict(lambda:0) 
    dist_count = 0
    for i in range(k): 
        if mp[arr[i]] == 0: 
            dist_count += 1
        mp[arr[i]] += 1
    print(dist_count, end=' ') 
    for i in range(k, n): 
        if mp[arr[i - k]] == 1: 
            dist_count -= 1
        mp[arr[i - k]] -= 1
        if mp[arr[i]] == 0: 
            dist_count += 1
        mp[arr[i]] += 1
        print(dist_count,end=' ') 
    print()    
t=int(input())
for i in range(t):
    n,k=map(int,input().split(' '))
    arr=list(map(int,input().strip().split(' ')))[:n]
    countDistinct(arr, k, n) 
