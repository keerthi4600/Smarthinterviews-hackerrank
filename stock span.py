def calculateSpan(price, S): 
    n = len(price) 
    st = [] 
    st.append(0) 
    S[0] = 1
    for i in range(1, n): 
        while( len(st) > 0 and price[st[-1]] <= price[i]): 
            st.pop() 
        S[i] = i + 1 if len(st) <= 0 else (i - st[-1]) 
        st.append(i) 
def printArray(arr, n): 
    for i in range(0, n): 
        print (arr[i], end =" ")
    print()    
t=int(input())
for i in range(t):
    n=int(input())
    price = list(map(int,input().strip().split(' ')))[:n] 
    S = [0 for i in range(n+1)] 
    calculateSpan(price, S) 
    printArray(S, n) 
