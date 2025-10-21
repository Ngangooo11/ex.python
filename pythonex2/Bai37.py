words = []  

print("Nhập các từ (nhấn Enter để kết thúc):")

while True:
    word = input("> ").strip()  # xóa khoảng trắng đầu/cuối
    if word == "":  
        break
    if word not in words:  # nếu từ chưa có trong danh sách thì thêm vào
        words.append(word)

print("\nCác từ bạn đã nhập (không trùng, theo thứ tự):")
for w in words:
    print(w)
