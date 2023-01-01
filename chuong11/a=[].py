a=[]
m=int(input("Nhap so tu nhien m:"))
n=int(input("nhap so tu nhien n"))
for i in range(m):
    print("Chuan bi nhap ma tran hang thu", i+1, ":")
    b=[]
    for j in range(n):
       x=int(input("Nhap phan tu thu"+str(j+1)+ ":"))
       b=b+[x]
    a.append(b)
print("Ma tran a da nhap xong")
#in
for i in range(m):
    for j in range(n):
        print(a[i][j],end="")
        print()