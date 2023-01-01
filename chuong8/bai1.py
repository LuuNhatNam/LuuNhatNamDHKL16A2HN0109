sodien=eval(input("số điện tháng này = "))
if sodien<=50:
    print("tiền điện = ",sodien*1.678)
elif sodien<=100:
    print("tiền điện= ",50*1.678+(sodien-50)*1.734)
elif sodien<=200:
    print("tiền điện= ",50*1.678+50*1.734+(sodien-100)*2.014)
elif sodien<=300:
    print("tiền điện= ",50*1.678+50*1.734+100*2.014+(sodien-200)*2.536)
elif sodien<=400:
    print("tiền điện= ",50*1.678+50*1.734+100*2.014+100*2.536+(sodien-300)*2.834)
else:
    print("tiền điện= ",50*1.678+50*1.734+100*2.014+100*2.536+100*2.834+(sodien-400)*2.937)


    