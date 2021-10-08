import random

WOERTER =  ['PARIS', 'DUBLIN', 'ZAGREB', 'RIGA', 'VADUZ', 'VILNIUS', 'LUXEMBURG', 'VALLETTA', 'BERLIN', 'MONACO', 'AMSTERDAM', 'SKOPJE', 'OSLO', 'WIEN', 'WARSCHAU', 'LISSABON', 'BUKAREST', 'MOSKAU', 'STOCKHOLM', 'BELGRAD', 'BRATISLAVA', 'LJUBLJANA', 'MADRID', 'PRAG', 'ANKARA','DUESSELDORF']
geheimWort =  random.choice (WOERTER)
falsche = []
richtige = []
emoticons = [':-D',':-)',':-/',':-(',':-((']

def visualisierung (falsche, richtige, geheimWort):
    print(emoticons[len(falsche)])
    # one blank per letter
    blanks = ['_'] * len(geheimWort)
    # replace blanks with correct letters
    for i in range (len(geheimWort)):
        if geheimWort[i] in richtige:
            blanks [i] = geheimWort[i]
    print (' '.join(blanks))
    
    
def fragSpieler (schon_geraten):
    while True:
        print ('Bitte einen Buchstaben:')
        buchstabe = input('?? ').upper()
        return buchstabe
    

while True:
    visualisierung (falsche, richtige, geheimWort)
    buchstabe = fragSpieler (falsche + richtige)
    
    if buchstabe in geheimWort:
        richtige.append (buchstabe)
    else:
        falsche.append (buchstabe)
    print (' ## Falsche: ', '-'.join(falsche))
    
        
    
    
    
