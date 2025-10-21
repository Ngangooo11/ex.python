def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Nhập một số nguyên: "))
print(f"Giai thừa của {n} là: {factorial(n)}")