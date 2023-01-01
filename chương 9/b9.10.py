n=int(input("Nhập n: "))
def fi(n):
    if n == 0: 
        return 0
    if n==1:
        return 1
    elif n > 1:
        return (fi(n-1)+fi(n-2))
print("fib(n) = ",fi(n))