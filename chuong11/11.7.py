n=int(input("Nhập số các số trong list L:"))
L=[int(input("Nhập phần tử trong list L:\n")) for i in range(n)]
thresh=int(input("Nhập thresh:"))
l=[]
for i in range(0,len(L)):
    a=L[i]
    def egt(a,thresh):
        flag = True
        if a <= thresh:
            flag = False
            return flag
        else :
            flag = True
            return flag
    l.append(egt(a,thresh))
print(l)

