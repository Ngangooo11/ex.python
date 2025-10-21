numbers = []

while True:
    n = int(input("Nhập số nguyên (0 để dừng): "))
    if n == 0:
        break
    numbers.append(n)

sorted_numbers = sorted(numbers)  

print("\nCác số đã nhập đã được sắp xếp tăng dần:")
for num in sorted_numbers:
    print(num)
