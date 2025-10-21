month = int (input('Enter a month to know the number of day in that month: '))
day30 = [4,6,9, 11]
day31 = [1,3,5,7,8,10,12]
if 1<=month<=12:
    if month in day30:
        print('That month has 30 days')
    elif month in day31:
        print ('That month has 31 days')
    elif month==2:
        print ('That month has 28 or 29 days')
else:
    print('The month is incorrect')