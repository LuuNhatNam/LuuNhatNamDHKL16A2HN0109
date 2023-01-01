#test
n=int(input("Nhập số phần tử trong set1 : "))
set1={int(input(">>"))for i in range(n)}
print(set1)
print("Số phần tử trong set1:",len(set1))
print("tổng giái trị của các phần tử trong set1:",sum(set1))
m=int(input('Nhập số phần trong set2 : '))
set2={int(input(">>"))for i in range(m)}
print(set2)
print("Số phần tử trong set2:",len(set2))
print("tổng giái trị của các phần tử trong set2:",sum(set2))

#tìm gt max min của mỗi set
print("Giá trị lớn nhất của set1 là:",max(set1))
print("Giá trị lớn nhật của set2 là:",max(set2))
print("Giá trị nhỏ nhất của set1 là:",min(set1))
print("Giá trị nhỏ nhất của set2 là:",min(set2))

#Lấy ra 1 phần tử trong set1 và in ra 

set=set1.pop()
print(set)


#Thực hiện set union của set1 và set2 

union = set1|set2
print(union)

#Thực hiện set intersection của set1 và set2

i=set1&set2
print(i)

#Thực hiện set difference của set1 và set2

d= set1 - set2
print(d)

#Thực hiện set symmetric difference của Set1 và set2

ssd= set1 ^ set2
print(ssd)

#Sắp xếp set1 tăng dần và set 2 giảm dần

sorted(set1)
print(set1)
sorted(set2, reversed = True)
print(set2)


