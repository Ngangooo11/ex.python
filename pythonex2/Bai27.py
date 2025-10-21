side = int (input ('Enter the number of side (from 3 to 10): '))
if side>=3 and side<=10 :
    if side==3 :
        print('This is a triangle')
    elif side ==4:
        print('This is aquadrilateral')
    elif side==5:
        print('This is a pentagon ')
    elif side==6:
        print('This is a hexagon ')
    elif side==7:
        print('This is a heptagon ')
    elif side==8:
        print('This is a octagon')
    elif side==9:
        print('This is a nonagon')
    elif side==10:
        print('This is a decagon')
else:
    print('Side is incorrect')        