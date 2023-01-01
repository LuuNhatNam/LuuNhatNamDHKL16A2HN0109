lsta=[]
lstd=[]
lst1=[]
lst=[int(input("Nhập giá trị: "))]
n=int(input("Tiếp tục nhập giá trị? 1: có, 0: không \n"))
while n==1:
    a=int(input("Nhập giá trị: "))
    lst.append(a)
    n=int(input("Tiếp tục nhập giá trị? 1: có, 0: không \n"))
print(lst)
#tìm các số nguyên tố trong list
def check(b):
    #flag = 0 => không phải số nguyên tố
    #flag = 1 => số nguyên tố
    flag = True
    if (b <2):
        flag = False
        return flag 
    for p in range(2, b):
        if b % p == 0:
            flag = False
            break 
    return flag
for i in range(len(lst)):
    c=check(lst[i])
    if c == True:
        lst1.append(lst[i])
print("các số nguyên tố trong list:",lst1)
#sắp xếp list trung bình cộng dương và âm
def tbc(j):
    #flag = 0 => không phải số nguyên tố
    #flag = 1 => số nguyên tố
    flag = True
    if (j<0):
        flag = False
        return flag 
    else:
        flag = True
        return flag
for i in range(len(lst)):
    d=tbc(lst[i])
    if d == True:
        lstd.append(lst[i])
    else:
        lsta.append(lst[i])
print("trung bình công các phần tử dương trong list:",sum(lstd)/len(lstd))
print("trung bình cộng các phần tử âm trong list:",sum(lsta)/len(lsta))
print("Giá trị max trong list:",max(lst))
print("Giá trị min trong list:",min(lst))
print("list sắp tăng dần:",sorted(lst))