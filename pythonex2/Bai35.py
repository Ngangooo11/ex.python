nums = list (map(int, input('Nhập danh sách các số: ').split()))
odd_nums = []
for n in nums:
    if n % 2 != 0:
        odd_nums.append(n)

print("Các số lẻ là:", odd_nums)