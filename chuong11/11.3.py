#tạo danh sách và in ra danh sách thú
animal=['ant','bear','cat','dog','elephant','fish','goat','hippo']
#sô lượng thú
print("số lượng thú là:",len(animal))
#tìm thú
f=str(input("con thú cần tìm: "))
find= f in animal
if find==True:
    print("There is",f,"in list of animals")
else:
    print("There isn't",f,"in list of animals")
