lst=[int(input("Nhập giá trị: "))]
n=int(input("Tiếp tục nhập giá trị? 1: có, 0: không \n"))
while n==1:
    a=int(input("Nhập giá trị: "))
    lst.append(a)
    n=int(input("Tiếp tục nhập giá trị? 1: có, 0: không \n"))
print(lst)
x=int(input("Nhập vào số cần tìm x: "))
#tổng list
print('tổng các giá trị trong list:',sum(lst))
#tìm x trong list
print(x ,"xuất hiện",lst.count(x),"lần trong list")
#so sách x với các phần tử trong list
lst.sort()
lst1=lst[(lst.index(x)+lst.count(x)):]
if x <= max(lst) and x>=min(lst):
    print(x," không lớn hơn tất cả các số trong  list")
    print("các số lớn hơn",x," trong list:",lst1)
elif x == min(lst):
    print(x,"là số nhỏ nhất trong list")
elif x == max(lst):
    print(x,"là số lớn nhất trong list")