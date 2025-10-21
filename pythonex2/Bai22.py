def Tao_In_DS():
    ds = list()
    for i in range(1, 21):
        ds.append(i ** 2)
    print(ds[:5] + ds[-5:])  # 5 phần tử đầu + 5 phần tử cuối

Tao_In_DS()
