num1, num2, num3 = map (int, input ('Enter 3 number to find max number: ').split())
if (num1>=num2) and (num1>= num3):
    max = num1
if (num2>= num1) and num2>= num3:
    max = num2
else:
    max = num3
print('The max number in ', num1, num2, num3, 'is: ',max)    