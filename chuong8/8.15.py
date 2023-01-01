mang_cac_so_nhap_vao = []
print('Nhập vào các số:')
while True:
  number = int(input(''))
  if (number == 0):
    break
  mang_cac_so_nhap_vao.append(number)
tong=0
for v in mang_cac_so_nhap_vao:
    tong += v

print("tổng= ",tong)
