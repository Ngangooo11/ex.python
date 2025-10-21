st = input ('Enter a string: ')
sub_st = input ('Enter a string to find: ')
if sub_st in st:
    print('Sub string was found, at location:', st.find(sub_st) )
else: 
    print('Not found  ')