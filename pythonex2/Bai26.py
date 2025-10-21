cha = input ('Enter a character: ')
if len(cha)!=1 :
    print ('That is not a character!' )
else:
    if cha in ('u', 'e', 'o', 'a', 'i') :
        print ('That is a vowel')
    elif cha=='y':
        print ("That can be a vowel or consonant")
    else: 
        print('That is a consonant')    