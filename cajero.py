import sqlite3


conexion = sqlite3.connect('Cuentas de Banco.db')
cursor = conexion.cursor()

def login():
  cedula = int(input('Escriba su Cédula: '))
  password = int(input('Escriba su Clave: '))
  cursor.execute(f'SELECT * FROM Cuentas WHERE cedula = {cedula}')
  get_user = cursor.fetchall()
  lista_vacia = not get_user
  if lista_vacia == True:
    print('Cédula Inválida')
  else:
    for user in get_user:
      if cedula == user[0]:
        print(f'Bienvenido {user[1]} su saldo es: {user[4]}')
        opciones(user)
      else:
        print('Usuario o contraseña inválido')

def opciones(user):
  print('1 - Depositar | 2 - Retirar | 3 - Salir')
  operación = int(input('¿Qué desea hacer?: '))
  if operación == 1:
    print('Usted eligió Depositar')
    depositar(user)
  elif operación == 2:
    print('Usted eligió Retirar')
    retirar(user)
  elif operación == 3:
    print('Usted eligió Salir - Hasta luego!')
  else:
    print('Ha ocurrido un error')

def depositar(user):
  cantidad = float(input('¿Cuánto desea depositar?: '))
  if cantidad <= 0:
    print('Usted está intentando depositar una cantidad menor o igual a cero')
  else:
    deposito = user[4] + cantidad
    cursor.execute(f'UPDATE Cuentas SET saldo = "{deposito}" WHERE cedula = {user[0]}')
    print(f'Su nuevo saldo es: {deposito}')
    repetir()

def retirar(user):
  cantidad = float(input('¿Cuánto desea retirar?: '))
  if cantidad > user[4] or cantidad <= 0:
    print('Ha ocurrido un error')
  else:
    retiro = user[4] - cantidad
    cursor.execute(f'UPDATE Cuentas SET saldo = "{retiro}" WHERE cedula = {user[0]}')
    print(f'Su nuevo saldo es: {retiro}')
    repetir()

def repetir():
  pregunta = input('¿Desea hacer otra operación?: ')
  while pregunta == 'si':
    return opciones()
  return

login()

conexion.commit()
conexion.close()