n = int (input('Enter a integer greater than 0:  '))
sum = 0.0
for i in range (1, n+1):
    sum+= float(i/(i+1))
print ('sum=',sum)    
