tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
even_numbers = ()  

for i in tup:
    if i % 2 == 0:  
        even_numbers += (i,) 

print("Tuple các số chẵn là:", even_numbers)
