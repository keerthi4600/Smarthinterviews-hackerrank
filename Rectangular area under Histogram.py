def histogram(hist): 
    stack = list() 
    max_area = 0 # Initialize max area 
    index = 0
    while index < n: 
        if (not stack) or (hist[stack[-1]] <= hist[index]): 
            stack.append(index) 
            index += 1
        else: 
            top = stack.pop() 
            area = (hist[top] *((index - stack[-1] - 1) if stack else index)) 
            max_area = max(max_area, area) 
    while stack: 
        top = stack.pop() 
        area = (hist[top] *((index - stack[-1] - 1) if stack else index)) 
        max_area = max(max_area, area) 
    return max_area
t=int(input())
for i in range(t):
    n=int(input())
    hist = list(map(int,input().strip().split(' ')))[:n]
    print(histogram(hist))
