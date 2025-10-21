# Bài 3: Thực hiện chương trình đếm số từ trong nhiều file text

def count_words(filename):        # Định nghĩa hàm count_words()
    try:
        # Mở file và tạo đối tượng f_obj
        with open(filename, 'r', encoding='utf-8') as f_obj:
            # Đọc nội dung file
            contents = f_obj.read()
    except FileNotFoundError:
        # Xử lý ngoại lệ khi file không tồn tại
        msg = "File " + filename + " không tồn tại."
        print(msg)
    else:
        # Trường hợp đọc file thành công
        words = contents.split()          # Tách các từ trong nội dung
        num_words = len(words)            # Đếm số từ
        print("File " + filename + " có " + str(num_words) + " từ.")

# Danh sách các file cần đếm
filenames = ['f1.txt', 'f2.txt', 'f3.txt']

# Gọi hàm count_words() cho từng file
for filename in filenames:
    count_words(filename)
