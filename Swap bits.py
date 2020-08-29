def swapAdjacentBits(num):
    return ((num & 0xAAAAAAAA) >> 1) | ((num & 0x55555555) << 1)
n=int(input())
for i in range(n):
    num = int(input())
    num = swapAdjacentBits(num)
    print(num)
