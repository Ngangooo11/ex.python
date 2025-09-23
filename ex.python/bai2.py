email = "minhnhutvh@gmail.com"
position = email.find("@")
host = email[position + 1 :]
print(host)