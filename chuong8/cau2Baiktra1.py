mang_cac_so_nhap_vao = []
dem_so_duong = 0
dem_so_am = 0
tong_so_am = 0

print('Nhập vào các số:')
while True:
  number = int(input(''))
  if (number == 0):
    break
  mang_cac_so_nhap_vao.append(number)
  if (number > 0):
    dem_so_duong += 1
  else:
    dem_so_am += 1
    tong_so_am += number

trung_binh_cong_so_am = tong_so_am / dem_so_am

print('Các số đã nhập: ')
print(' '.join(str(number) for number in mang_cac_so_nhap_vao))

print('Tổng số dương: ', dem_so_duong)
print('Trung bình cộng của số âm: ', trung_binh_cong_so_am)