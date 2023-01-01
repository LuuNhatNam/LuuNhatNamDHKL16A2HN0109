# Nhap du lieu
nam=int(input('Nhap nam nam: '))
# Kiem tra nam nhuan
if (nam % 400 == 0) or ((nam % 4 == 0) and (nam % 100 != 0)):
    print('Nam nhuận')
else:
    print('Nam không nhuận')