from math import sqrt
print('Đây là bài toán tính tốc độ của vật lúc chạm đất khi được thả rơi tự do')
h=float(input('Nhập độ cao (đơn vị mét) của vật khi được thả '))
v= sqrt(2*9.8*h)
print('Tốc độ của vật lúc chạm đất khi được thả rơi tự do từ độ cao', h, '(m) là:', v)