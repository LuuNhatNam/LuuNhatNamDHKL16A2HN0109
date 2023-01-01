#vd
n = int(input("Nhap vao so luong phan tu: "))

print("Nhap vao phan tu cho mang:")
a = []
for i in range(0, n):
    print("\tPhan tu thu", (i+1), "la:", end=" ")
    a.append(int(input()))

print("Mang vua nhap la:")
for i in range(len(a)):
    print(a[i], end="\t")

chan, le, s_chan, s_le = 0, 0, 0, 0