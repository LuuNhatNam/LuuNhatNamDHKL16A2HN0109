#tạo danh bạ
danh_ba={
    "Minh":"0988741258",
    "Hạnh":"0903852147",
    "Bình":"0913753951",
    "An"  :"0933753654"
}
print(danh_ba)#hiển thị dic danh bạ
#kiểm tra tên có trong danh bạ hay không
try:
    n=str(input("search_name: "))
    print(danh_ba[n])
except  KeyError:
    print("không tìm thấy")
#thêm liên hệ mới
name=str(input("Nhập tên muốn thêm liên hệ mới:"))
sdt=int(input("Nhập số điện thoại: "))
danh_ba[name]=sdt
print(danh_ba)#hiển thị danh bạ khi thêm llieen hệ mới
