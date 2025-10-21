n = int(input("Nhập một số nguyên n: "))

result = {}  

for i in range(1, n + 1):
    result[i] = i * i  

print("Dictionary kết quả là:")
print(result)
