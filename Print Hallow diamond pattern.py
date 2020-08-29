t=int(input())
for i in range(1,t+1):
    row = int(input())
    print('Case #{}:'.format(i)) 
    for i in range(row):
        for j in range(row):
            if (j+i==row//2 or i+j==row-1+(row//2) or j==i+(row//2) or i==j+(row//2)):
                print("*",end='')
            else:    
                print(" ",end='')
        print()
