#Facts
dogs = ['fido','rover','henry']

#Rules
def isAnimal (name):
    return True if name in dogs else False
    
#Execution
print(isAnimal ('fido'))
print(isAnimal ('otto')) 