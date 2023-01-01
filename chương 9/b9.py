r=eval(input("Nhập r: "))
a=int(input("Nhập a: "))
b=int(input("Nhập b: "))
import math
S_ht = lambda r: 3.14*math.pow(r,2)
V_ht = lambda r: 2*3.14*r
S_hcn = lambda a, b: a*b
V_hcn = lambda a, b: (a + b)/2
print("Diện tích hình tròn là:",S_ht(r))
print("Chu vi hình tròn là:",V_ht(r))
print("Diện tích hình chữ nhật là:",S_hcn(a,b))
print("Chu vi hình chữ nhật là:",V_hcn(a,b))