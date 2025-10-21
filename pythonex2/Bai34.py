decimal = int(input("Nhập một số nguyên thập phân: "))

if decimal == 0:
    print("Số nhị phân tương ứng là: 0")
else:
    binary = ""  
    n = decimal
    while n > 0:
        remainder = n % 2          
        binary = str(remainder) + binary  # ghép dư vào đầu chuỗi
        n = n // 2                

    print(f"Số {decimal} trong hệ nhị phân là: {binary}")
