n=int(input("nhập số các số trong dãy: "))
lst = []
for i in range(n):
    lst.append(int(input()))
    i+=1
answer = 0
for v in lst:
    answer += v

print("tổng= ",answer)