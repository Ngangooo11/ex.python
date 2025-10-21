import zipfile

def giai_nen_tep(ten_zip, thu_muc_dich):
    # Mở file ZIP ở chế độ đọc
    with zipfile.ZipFile(ten_zip, 'r') as zipf:
        zipf.extractall(thu_muc_dich)
        print(f"Đã giải nén tất cả tệp vào thư mục: {thu_muc_dich}")

# Gọi hàm giải nén
giai_nen_tep('tap_tin_nen.zip', './thu_muc_giai_nen')
