import math
a=int(input("Nhập a:"))
b=int(input("Nhập b:"))
c=int(input("nhập c:"))
dt=0
def S(a,b,c):
    if a==0 :
        if b == 0:
            print("Phương trình vô nghiệm")
        else:
            print("Phương trình có một nghiệm: x = ", (-c / b))
        return
    else:
        dt=math.pow(b,2)- 4*a*c
        if dt < 0:
            print("phương trình vô nghiệm")
        if dt == 0:
            print("Phương trình có nghiệm kép x=",-b/(2*a))
        else:
            print("Phương trình có 2 nghiệm phân biệt:")
            print("x1=",(-b+math.sqrt(dt))/2*a)
            print("x2=",(-b-math.sqrt(dt))/2*a)
        return
S(a,b,c)
            
        