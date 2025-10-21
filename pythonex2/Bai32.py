message = input("Nhập thông điệp: ")
shift = int(input("Nhập số ký tự cần dịch chuyển: "))
mode = int (input("Bạn muốn mã hóa (nhập 1) hay giải mã (nhập 0) ? "))

# Nếu người dùng chọn giải mã thì:
if mode == 0:
    shift = -shift

encrypted = ""

for ch in message:
    if 'A' <= ch <= 'Z':  # Chữ hoa
        encrypted += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
    elif 'a' <= ch <= 'z':  # Chữ thường
        encrypted += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
    else:  # Ký tự khác: giữ nguyên
        encrypted += ch

print("\nKết quả sau khi xử lý:")
print(encrypted)
