def average ():
    a, b, c = map(float, input('Nhập vào 3 số cần tính trung bình: ').split())
    avg = (a+b+c)/3
    print (f"Trung bình cộng của 3 số {a}, {b}, {c} là: {avg}")
average()
