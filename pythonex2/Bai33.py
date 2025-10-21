st = input("Nhập chuỗi cần kiểm tra: ")
st = st.lower()

is_palindrome = True  # giả sử ban đầu chuỗi là palindrome

# Duyệt nửa chuỗi
for i in range(len(st) // 2):
    if st[i] != st[-(i + 1)]:  
        is_palindrome = False
        break  # thoát khỏi vòng lặp 

# In kết quả
if is_palindrome:
    print(f"'{st}' là chuỗi Palindrome.")
else:
    print(f"'{st}' không phải là chuỗi Palindrome.")
