import sys 
sys.setrecursionlimit(5000)
def giaithua(n):
    if n==1:
        return 1
    else:
        return n*giaithua(n-1)
number=int(input())
print(giaithua(number))