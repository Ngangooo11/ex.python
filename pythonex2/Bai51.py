def check_password(password):
    if len(password)<8:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    for ch in password: 
        if ch.isupper():
            has_upper = True
        if ch.islower():
            has_lower = True
        if ch.isdigit():
            has_digit = True
        if has_upper and has_lower and has_digit:
            return True
    return False

st = input('Nhập mật khẩu cần kiểm tra: ')
if check_password(st):
    print ('Mật khẩu tốt')
else:
    print('Mật khẩu không tốt')        