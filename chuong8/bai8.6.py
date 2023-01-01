loai_xe=int(input("loại xe: "))
km=float(input("số km: "))
tg=int(input("thời gian chờ: "))
if loai_xe==4 and km<20:
    print("tiền cước taxi= ",(tg-5)*8.000+(12.100*km))
elif loai_xe==4 and km>=20:
    print("tiền cước taxi= ",(tg-5)*8.000+12.100*20+10.000*(km-20))
elif loai_xe==7 and km<30:
    print("tiền cước taxi= ",(tg-5)*8.000+14.100*km)
elif loai_xe==7 and km>=30:
    print("tiền cước taxi= ",(tg-5)*8.000+30*14.100+(km-30)*12.000)
else:
    print("loại xe không hợp lệ")