year = int(input('nhập vào năm cần xem: '))
'''if year%4==0:
    if year%400==0:
        print('Đây là năm nhuận')
    elif year%100==0:
        print('Đây không phải là năm nhuận')
    else:
        print('Đây là năm nhuận')
else:
    print('Đây không phải là năm nhuận')'''
if (year%400==0) or (year%4==0 and year%100!=0 ):
    print('Đây là năm nhuận')
else:
    print('Đây không phải là năm nhuận')