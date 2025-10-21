def print_except_first5():
    squares = []  

    for i in range(1, 21):  
        squares.append(i ** 2)  
    print("Các phần tử còn lại là:", squares[5:])

# Gọi hàm
print_except_first5()
