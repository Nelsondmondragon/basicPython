pesos = input('Cuantos pesos colombianos tienes?: ')
pesos = float(pesos)
valor_dolar = 3945
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print('tienes ' + dolares)