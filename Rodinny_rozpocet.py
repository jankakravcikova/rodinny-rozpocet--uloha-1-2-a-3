#Program na evidenciu bilancie rodinnych financii
#autor: Jana Kravcikova
#verzia: 1.0

from random import randint

denneOperaciePocet=int(input('Zadajte ocakavany pocet dennych operacii:'))
denneOperacieSumy=[]
for i in range(denneOperaciePocet):
                       denneOperacieSumy.append(randint(-1000,1000))
print(denneOperacieSumy)

celkovaBilancia=sum(denneOperacieSumy)

print("Denny zostatok Vasich rodinnych financii je",celkovaBilancia,".")

tyzdenneObraty=[]
for i in range(7):
    dennaBilanciaVydavkov()




