cci=[74,74,72,72,73,69,69,71,76,71]
ccm=[]
print(cci)
#đổi inch sang mét
for i in range(len(cci)):
    a=cci[i]*0.0254
    ccm.append(a)
print(ccm)
#in ra 3 chiều cao đầu tiên 3 chiều cao cuối cùng
print("3 chiều cao đầu tiên lượt là:\n")
for i in range(0,3):
    print(ccm[i])
print("3 chiều cao cuối cùng lần lượt là:\n")    
for i in range(7,10):
    print(ccm[i])
