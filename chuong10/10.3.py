import math
x=float(input("Nhập x:"))
n=float(input("Nhập n:"))
s=lambda x, n: (math.pow(x,2)+1)*n
print("S = (x**2 + 1)*n =",s(x,n))