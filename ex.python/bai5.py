st = input("enter your string:")
first_five_character = st[:5]
last_five_character = st[-5:]
four_str_1_line = 4 * (st + " ")
four_str_4_line = 4 * (st + "\n")
print(" 5 kí tự đầu là :" + first_five_character)
print(" 5 kí tự cuối là:"+ last_five_character)
print(" 4 chuỗi trên 1 dòng:" + four_str_1_line)
print("4 chuỗi trên 4 dòng: \n" + four_str_4_line)