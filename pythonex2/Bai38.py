negatives = []
zeros = []
positives = []

print("Nhập các số nguyên (nhấn Enter để kết thúc):")

while True:
    line = input("> ").strip()
    if line == "":
        break  
    
    n = int(line)  
    # Phân loại số
    if n < 0:
        negatives.append(n)
    elif n == 0:
        zeros.append(n)
    else:
        positives.append(n)

print("\nCác số âm:")
for n in negatives:
    print(n)

print("\nCác số 0:")
for n in zeros:
    print(n)

print("\nCác số dương:")
for n in positives:
    print(n)
