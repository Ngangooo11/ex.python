message = input("Nhập thông điệp cần mã hóa: ")
encrypted = ""  # chuỗi kết quả rỗng ban đầu

for ch in message:
    if 'A' <= ch <= 'Z':  # nếu là chữ hoa
        encrypted += chr((ord(ch) - ord('A') + 3) % 26 + ord('A'))
    elif 'a' <= ch <= 'z':  # nếu là chữ thường
        encrypted += chr((ord(ch) - ord('a') + 3) % 26 + ord('a'))
    else:  # ký tự khác: giữ nguyên
        encrypted += ch

print("Thông điệp sau khi mã hóa:", encrypted)
