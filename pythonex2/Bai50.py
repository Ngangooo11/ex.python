import random

def generate_password():
    length = random.randint(7,10)
    password =''
    for i in range(length):
        char = chr (random.randint(33, 126))
        password += char
    return password
print('Mật khẩu được tạo ngẫu nhiên là ', generate_password())    
