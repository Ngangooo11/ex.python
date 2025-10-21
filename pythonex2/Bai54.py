def format_list(words):
    if len(words) == 0:
        return ""  
    elif len(words) == 1:
        return words[0]
    elif len(words) == 2:
        return words[0] + " and " + words[1]
    else:
        return ", ".join(words[:-1]) + " and " + words[-1]
words = []

print("Nhập các từ (Enter để dừng):")
while True:
    word = input("> ").strip()
    if word == "":
        break
    words.append(word)

result = format_list(words)
print("\nKết quả định dạng:")
print(result)
