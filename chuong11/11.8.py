n=int(input("Nhập số các số trong list:"))
L=[int(input("Nhập phần tử trong list:\n")) for i in range(n)]
l=[]
for i in range(0,len(L)):
    a=L[i]
    flag = True
    if a%7==0:
        flag = True
        l.append(flag)
        print(l)
        break


