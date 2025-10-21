a, b, c = map (float, input ('Nhập 3 cạnh của tam giác: ').split())
if a>0 and b>0 and c>0:
    if a+b>c and a+c>b and b+c>a:
        if a==b and a==c:
            print('Đây là tam giác đều')
        elif a==b or a==c or b==c:
            print('Đây là tam giác cân')
        else:
            print('Đây là tam giác bình thường')
    else:
        print('Ba cạnh trên không tạo thành 1 tam giác')
else:
    print('Ba cạnh không phù hợp')