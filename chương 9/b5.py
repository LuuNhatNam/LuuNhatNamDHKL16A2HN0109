def tinh_A(n,x):
    return (x*x + x + 1)**n + (x*x - x + 1)**n
n=int(input("Nhập n: "))
x=int(input("Nhập x: "))
print("A = (x*x + x + 1)**n + (x*x - x + 1)**n =",tinh_A(n,x))