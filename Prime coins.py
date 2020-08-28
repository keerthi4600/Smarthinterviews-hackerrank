def findWinner(n): 
    if (n  % 6 == 0): 
        print("Banta") 
    else: 
        print("Santa")
t=int(input())
for i in range(t):
    n=int(input())
    findWinner(n)
