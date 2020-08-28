def KMPSearch(pat, txt): 
    M = len(pat) 
    N = len(txt) 
    lps = [0]*M 
    j = 0
    computeLPSArray(pat, M, lps) 
    i = 0
    count=0
    while i < N: 
        if pat[j] == txt[i]: 
            i += 1
            j += 1
        if j == M:
            count+=1
            j = lps[j-1] 
        elif i < N and pat[j] != txt[i]: 
            if j != 0: 
                j = lps[j-1] 
            else: 
                i += 1
    return count           
def computeLPSArray(pat, M, lps): 
    len = 0
    lps[0]  
    i = 1
    while i < M: 
        if pat[i]== pat[len]: 
            len += 1
            lps[i] = len
            i += 1
        else: 
            if len != 0: 
                len = lps[len-1] 
            else: 
                lps[i] = 0
                i += 1
t=int(input())
for i in range(t):
    s1,s2=map(str,input().split())
    print(KMPSearch(s1,s2))