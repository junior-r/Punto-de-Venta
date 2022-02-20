# numero = '0000000001'
# print(numero)
# sumar = input('Desea sumar 1?: ')

# while sumar == 'si':
#   numero = int(numero) + 1
#   print(str(numero))
#   sumar = input('Desea sumar 1?: ')
# print(numero)

# def centrar_texto(texto):
#   lineas = '-' * 100
#   espacios = len(lineas) - len(texto)
#   centra = espacios / 2
#   espacios = ' ' * int(centra)
#   print(lineas)
#   print(espacios, texto, espacios)
#   print(lineas)

# centrar_texto('Factura')

codigos = ['1234567890']
start = 0

for codigo in codigos:
  longitud = len(codigo)
  print('----- Codigos -----')
  for i in range(5, longitud + 5, 5):
    print(codigo[start:i])
    start += 5

def cantidad_codigos(codigos):
  for codigo in codigos:
    longitud = len(codigo)
    if longitud % 5 == 0:
      return f'La cantidad de codigos son: {longitud // 5}'
    else:
      resto = longitud % 5
      relleno = 5 - resto
      relleno = relleno * '?'
      cod_incompleto = codigo[-resto:]
      return f'La cantidad de codigos son: {longitud // 5}. Y faltan caracteres en el último codigo: {cod_incompleto + relleno}'

print(cantidad_codigos(codigos))
