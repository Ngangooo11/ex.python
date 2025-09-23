import math
m, dentaT = map(float, input('Nhập vào khối lượng nước (gram) và sự thay đổi nhiệt độ dentaT (độ C): ').split())
Q=4.186*m*dentaT
print('Năng lượng cần cung cấp để thay đổi', dentaT, '(độ C) cho', m, '(gram) nước là',
      round(Q,2), '(J)')
print('Chi phí cần thiết để thay đổi', dentaT, '(độ) của', m, '(gram) nước là:', round(Q*2.777*(math.e**-7)*8.9, 2) ,'cent')