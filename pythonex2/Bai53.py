def sublists(lst):
    result = [[]]  #luôn có 1 sublist rỗng
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n + 1):
            result.append(lst[i:j])
    return result


data = [1, 2, 3]
print("Các danh sách con của", data, "là:")
print(sublists(data))
