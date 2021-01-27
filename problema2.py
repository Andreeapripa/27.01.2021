lista=[]
lista.extend(input('Inttroduceti numarul listei:'))
lista=[list(i) for i in lista]
print('lista:',lista)
print('Suma cifrelor numarului este', sum(lista))