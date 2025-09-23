data = "minhnhutvh@gmail.com Sat Jan 5 09:14:16"
start = data.find("@")
end = data.find(" " , start)
host = data[start + 1 : end]
print(host)