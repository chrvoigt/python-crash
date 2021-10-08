import random
import csv

filename ='test.csv'

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer (csvfile, dialect='excel', delimiter =';')
    for lines in range (1,100):
        iterable =  (random.normalvariate (10, 3) for i in range (0,3))
        writer.writerow(iterable)
      
    
'''
    filewriter = csv.writer(csvfile, delimiter=';')
    iterable =  (random.normalvariate (10, 100) for i in range (0,100))
    filewriter.writerow('i)
'''

        
        
    

    
    