import zipfile

def nen_tep(ten_zip, danh_sach_tep):
    # Tạo file ZIP mới (chế độ 'w' = write)
    with zipfile.ZipFile(ten_zip, 'w') as zipf:
        for tep in danh_sach_tep:
            zipf.write(tep)
            print(f"Đã nén: {tep}")
    print(f"\nHoàn tất! Đã tạo tệp nén: {ten_zip}")

# Danh sách các file cần nén
tep_can_nen = ['f1.txt', 'f2.txt', 'f3.txt']
ten_tap_tin_zip = 'tap_tin_nen.zip'

# Gọi hàm nén
nen_tep(ten_tap_tin_zip, tep_can_nen)
