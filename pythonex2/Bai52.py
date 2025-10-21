def perfect_number(n):
    if n <= 1:
        return False

    sum = 1  
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum += i
            if i != n // i:  # ktra ước đối xứng có trùng không
                sum += n // i # cộng thêm ước đối xứng ( ví dụ 81/3=27 mà căn 81 là 9.)

    return sum == n

num = int(input('Nhập số nguyên dương: '))

if perfect_number(num):
    print(f'{num} là số hoàn hảo')
else:
    print(f'{num} không phải là số hoàn hảo')

perfect_list =[]
for i in range(1, 10001):
    if perfect_number(i): 
        perfect_list.append(i)
print ('các số hoàn hảo trong khoảng 1-10000 là: ',perfect_list)        