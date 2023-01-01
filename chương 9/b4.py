def tinh_S(n,x):
    return (x*x + 1)**n
n=int(input("Nhập n: "))
x=int(input("Nhập x: "))
print("S = (x*x + 1)**n =",tinh_S(n,x))