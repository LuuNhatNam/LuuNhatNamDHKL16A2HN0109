def BMI(cannang,chieucao):
    return cannang/(chieucao**2)

def PhanLoai(BMI):
    if BMI < 18.5:
        return 'Bạn quá gầy'
    elif BMI <= 24.9:
        return  'Bạn bình thường'
    elif BMI <= 29.9:
        return 'Bạn hơi béo'
    elif BMI <= 34.9:
        return 'Bạn béo phì cấp độ 1'
    elif BMI <= 39.9:
        return 'Bạn béo phì cấp độ 2'
    else:
        return 'Bạn béo phì cấp độ 3'
x = float(input('Nhập vào cân nặng của bạn (kg): '))
y = float(input('Nhập vào chiều cao của bạn (m): '))
bmi = BMI(x, y)
print('BMI của bạn = ', bmi)
print(PhanLoai(bmi))