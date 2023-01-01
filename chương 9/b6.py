x = int(input("nhập x: "))
flag = True
 
# Kiểm tra SNT
if (x < 2):
    flag = False
elif (x == 2):
    flag = True
elif (x % 2 == 0):
    flag = False
else:
    for i in range(3, x/2, 2):
        if (x % i == 0):
            flag = False
if flag == True:
    print("True")
else:
    print("False")
