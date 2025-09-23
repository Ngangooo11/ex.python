import math
a, b = map (int, input('Nhập 2 số nguyên a, b: ').split())
print('Tổng 2 số a+b =', a+b, '\n',
      'Hiệu 2 số a-b =', a-b, '\n',
      'Tích 2 số a*b =', a*b, '\n',
      'Thương 2 số a/b=', a/b, '\n',
      'Phần còn lại khi a/b là:', a%b, '\n',
      # hoặc math.fmod(a, b) thì đáp án sẽ cùng dấu với b
      'Log10(a)=', math.log10(a), '\n'
      'a^b=', math.pow(a,b))