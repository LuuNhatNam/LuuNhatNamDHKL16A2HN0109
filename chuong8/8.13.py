n=int(input("Nhập n: "))
s_chan=0
s_le=0
c=0
d=0
e=0
f=0
for i in range(0, n + 1):
    if i % 2 != 0:
        s_le += i
print("A= ",s_le)
for i in range(0, n + 1):
    if i % 2 == 0:
        s_chan += i
print("B= ",s_chan)

for i in range(0, n + 1):
        c*= i
print("C= ",c)

for i in range(0, n + 1):
    if i % 3 == 0:
        d*= i
print("D= ",d)
for i in range(0, n + 1):
    if i % 2 != 0:
        s_le += i
print("A= ",s_le)

    

    