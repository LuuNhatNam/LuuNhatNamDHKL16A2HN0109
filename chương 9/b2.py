can = ['Canh','Tân','Nhâm','Quý','Giáp','Ất','Bính','Đinh','Mậu','Kỷ']
chi = ['Thân','Dậu','Tuất','Hợi','Tý','Sửu','Dần','Mão','Thìn','Tị','Ngọ','Mùi']
nam=int(input("Nhập số năm âm lịch: "))
print("năm",nam ,"là năm:",can[nam%10] ,chi[nam%12] ,"trong âm lịch")