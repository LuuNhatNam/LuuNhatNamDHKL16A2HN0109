n = input(eval('nhap so')) 
flag = True
if n<2:
    print("ko la so ngto")
    esle:
    for i in range (2,n):
        if n%i == 0:
            flag=False
            break
        if flag:
            print(n , "là so nguyen to")
            esle:
            print(n , "ko phai so ngto")