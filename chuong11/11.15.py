#tạo từ điển 
dic={"cat":"Con mèo",
"dog":"Con chó",
"ant":"Con kiến",
"bear":"Con gấu"
}
n=int(input("Bạn muốn làm gì? 1: Xem từ điển; 2: Tra từ; 3: thêm từ; 4: Xóa từ \n"))
if n==1:
    print(dic)
elif n==2:
    s=str(input("Nhập từ cần tra: "))
    print(dic[s])
elif n==3:
    ta=str(input("thêm từ Anh: "))
    tv=str(input("Nghĩa của Từ: "))
    dic[ta]=tv
    print(dic)
elif n==4:
    xoa=str(input("Nhập từ cần xóa: "))
    hoi=input("bạn có thực sự muốn xóa hay không/ 1: Xóa, 0: Không")
    if hoi==1:
        del dic[xoa]
        print("Đã xóa trong từ điển")
        print(dic)
    else:
        print(dic)
next=int(input("Tiếp tục lựa chọn? 1: Có; 2: Không"))
while next==1:
    n=int(input("Bạn muốn làm gì/ 1: Xem từ điển; 2: Tra từ; 3: thêm từ; 4: Xóa từ "))
    if n==1:
        print(dic)
    elif n==2:
        s=str(input("Nhập từ cần tra: "))
        print(dic[s])
    elif n==3:
        ta=str(input("thêm từ Anh: "))
        tv=str(input("Nghĩa của Từ: "))
        dic[ta]=tv
        print(dic)
    elif n==4:
        xoa=str(input("Nhập từ cần xóa: "))
        hoi=input("bạn có thực sự muốn xóa hay không/ 1: Xóa, 0: Không \n")
        if hoi==1:
            del dic[xoa]
            print("Đã xóa trong từ điển")
            print(dic)
        else:
            print(dic)
    next=int(input("Tiếp tục lựa chọn? 1: Có; 2: Không  \n"))