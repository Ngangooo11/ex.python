from tu_dien import *

max_value = int(input("Nhập chỉ số Max: "))
TD = tao_TD(max_value)

print("\nCác phần tử của từ điển là:")
Print_Item(TD)

print("\nKhóa các phần tử của từ điển:")
Print_key(TD)

print("\nGiá trị các phần tử của từ điển:")
Print_value(TD)
