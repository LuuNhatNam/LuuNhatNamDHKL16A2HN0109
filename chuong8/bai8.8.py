lp=int(input("Nhập loại phòng: "))
so_dem=int(input("Nhập số đêm: "))
if lp==1:
    if so_dem==1:
        print("Thành Tiền: 1260")
    elif so_dem>=2 and so_dem<=3:
        print("Thành Tiền: ",1260*0.75*so_dem)
    elif so_dem>=4:
        print("Thành Tiền: ",1260*0.70*so_dem)
elif lp==2:
    if so_dem==1:
        print("Thành Tiền: 1550")
    elif so_dem>=2 and so_dem<=3:
        print("Thành Tiền: ",1550*0.75*so_dem)
    elif so_dem>=4:
        print("Thành Tiền: ",1550*0.70*so_dem)
elif lp==3 or lp==4:
    if so_dem==1:
        print("Thành Tiền: 1830")
    elif so_dem>=2 and so_dem<=3:
        print("Thành Tiền: ",1830*0.75*so_dem)
    elif so_dem>=4:
        print("Thành Tiền: ",1830*0.70*so_dem)
elif lp==5 or lp==6:
    if so_dem==1:
        print("Thành Tiền: 2120")
    elif so_dem>=2 and so_dem<=3:
        print("Thành Tiền: ",2120*0.75*so_dem)
    elif so_dem>=4:
        print("Thành Tiền: ",2120*0.70*so_dem)
elif lp==7:
    if so_dem==1:
        print("Thành Tiền: 2540")
    elif so_dem>=2 and so_dem<=3:
        print("Thành Tiền: ",2540*0.75*so_dem)
    elif so_dem>=4:
        print("Thành Tiền: ",2540*0.70*so_dem)
elif lp==8:
    if so_dem==1:
        print("Thành Tiền: 4800")
    elif so_dem>=2 and so_dem<=3:
        print("Thành Tiền: ",4800*0.75*so_dem,)
    elif so_dem>=4:
        print("Thành Tiền: ",4800*0.70*so_dem)


    