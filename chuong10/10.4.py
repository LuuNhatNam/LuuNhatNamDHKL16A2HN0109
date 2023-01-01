import math
x=float(input("Nhập x:"))
n=float(input("Nhập n:"))
a=lambda x, n: math.pow(math.pow(x,2)+x+1,n) + math.pow(math.pow(x,2)-x+1,n)
print("A=",a(x,n))