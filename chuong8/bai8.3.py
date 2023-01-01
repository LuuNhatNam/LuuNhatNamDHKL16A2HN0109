Diem_TB=eval(input("Nhập điểm trung bình: "))
if Diem_TB>=0 and Diem_TB<=10:
    if Diem_TB < 5:
        print("Yếu/Kém!!")
    elif Diem_TB < 6:
        print("Trung bình!!")
    elif Diem_TB < 7:
        print("Trung Bình - Khá")
    elif Diem_TB < 8:
        print("Khá!!")
    elif Diem_TB < 9:
        print("Giỏi!!")
    else:
        print("Xuất Sắc!!!!")
else:
        print("Diểm nhập vào không hợp lệ !")

