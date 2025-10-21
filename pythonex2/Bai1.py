'''
Viết một chương trình nhập vào một số nguyên dương.
 Nếu nó là số chẵn thì in ra chuỗi “Đây là số chẵn”, ngược lại thì in ra chuỗi “Đây là số lẻ”:
'''
number = int(input('Enter a positive integer: '))
if (number%2==0):
    print ('This is an even number')
else: 
    print ('This is an odd number')
