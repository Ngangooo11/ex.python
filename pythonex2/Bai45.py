def print_first5_squares():
    squares = []

    for i in range(1, 21):  
        squares.append(i ** 2)  
    print("5 phần tử đầu tiên là:", squares[0:5])

# Gọi hàm
print_first5_squares()
