import sqlite3
import datetime
import random


def datos():
  cedula = int(input('Cédula: '))
  print('1 - Ahorro, 2 - Corriente')
  tCuenta = input('Tipo de cuenta: ')
  tCuenta.lower()
  if tCuenta == '1':
    tCuenta = 'Ahorro'
  elif tCuenta == '2':
    tCuenta = 'Corriente'
  monto = float(input('Monto: '))
  clave = int(input('Clave: '))
  evalua_datos(cedula, tCuenta, monto, clave)

conexion_1 = sqlite3.connect('Cuentas de Banco.db')
conexion_2 = sqlite3.connect('Registro del Punto.db')
cursor_1 = conexion_1.cursor()
cursor_2 = conexion_2.cursor()

try:
  cursor_2.execute('''
    CREATE TABLE Compras (
      cedula INTEGER,
      numero_factura STRING PRIMARY KEY,
      monto FLOAT,
      fecha DATETIME
    )
  '''
  )
except sqlite3.OperationalError:
  pass

def evalua_datos(cedula, tCuenta, monto, clave):
  cursor_1.execute(f'SELECT * FROM Cuentas WHERE cedula = {cedula}')
  get_users = cursor_1.fetchall()
  lista_vacia = not get_users
  if lista_vacia == True:
    print('Cédula Inválida')
  else:
    for user in get_users:
      if tCuenta != user[3]:
        print('Tipo de Cuenta Inválido')
      elif monto <= 0:
        print('Monto Inválido')
      elif monto > user[4]:
        print('Saldo Insuficiente')
      elif clave != user[5]:
        print('Clave Inválida')
      else:
        if monto > 0 and monto < user[4]:
          update_saldo(monto, user)
        fecha = datetime.datetime.now()
        factura(user, monto, fecha)

def update_saldo(monto, user):
  resta = user[4] - monto
  cursor_1.execute(f'UPDATE Cuentas SET saldo = "{resta}" WHERE cedula = {user[0]}')

def factura(user, monto, fecha):
  print('-' * 30, '\nFactura')
  print('-' * 30)
  print('Compra por:', user[1])
  print('Cédula:', user[0])
  print('Banco:', user[2])
  print('Monto:', monto)
  print('Fecha:', fecha)
  numeros = '1234567890'
  longitud = 8
  muestra = random.sample(numeros, longitud)
  n_factura = ''.join(muestra)
  print('Número de Factura:', n_factura)
  registrar_compra(user, n_factura, monto, fecha)

def registrar_compra(user, n_factura, monto, fecha):
  cedula = user[0]
  info_factura = [
    (cedula, n_factura, monto, f"{fecha}")
  ]
  cursor_2.executemany('INSERT INTO Compras VALUES (?, ?, ?, ?)', info_factura)


datos()
conexion_1.commit()
conexion_2.commit()
conexion_1.close()
conexion_2.close()