import zipfile

def compress_file(file_path, zip_name):
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(file_path)
        print(f"Đã nén '{file_path}' thành '{zip_name}'")


file_path = input("Nhập đường dẫn tệp cần nén: ")
zip_name = input("Nhập tên file nén (.zip): ")
compress_file(file_path, zip_name)
