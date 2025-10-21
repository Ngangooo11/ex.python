# Bài 2: Xử lý ngoại lệ FileNotFoundError khi thực hiện chương trình đếm số từ trong file text

filename = "alice.txt"

try:
    # Mở file và tạo biến đối tượng f_obj
    with open(filename, 'r', encoding='utf-8') as f_obj:
        # Đọc và lưu nội dung file alice.txt vào biến contents
        contents = f_obj.read()

except FileNotFoundError:
    # Xử lý ngoại lệ khi không mở được file
    msg = "File " + filename + " không tồn tại."
    print(msg)

else:
    # Trường hợp đọc file hợp lệ
    # Tách các từ trong biến contents lưu vào danh sách words
    words = contents.split()
    
    # Đếm số từ lưu vào biến num_words
    num_words = len(words)
    
    print("File " + filename + " có " + str(num_words) + " từ.")
