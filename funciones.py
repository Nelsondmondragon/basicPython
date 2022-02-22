# def imprimir_mensaje():
#     print('Mens')
#     print('OooOo')



# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

def conversacion(mensaje):
    print('Hola')
    print('Como estas?')
    print(mensaje)
    print('adios')

opcion = input('Elige una opcion(1,2,3): ')
if opcion == '1':
   conversacion('Elegiste la opcion 1')
elif opcion == '2':
   conversacion('Elegiste la opcion 2')
elif opcion == '3':
   conversacion('Elegiste la opcion 3')
else:
    print('Escribe la opcion correcta')