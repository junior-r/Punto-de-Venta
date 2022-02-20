import sqlite3


conexion = sqlite3.connect('Cuentas de Banco.db')
cursor = conexion.cursor()

try:
  cursor.execute('''
    CREATE TABLE Cuentas (
      cedula INTEGER PRIMARY KEY,
      nombre STRING,
      banco STRING,
      tipo_cuenta STTRING,
      saldo FLOAT,
      clave INTEGER
    )
  '''
  )
except sqlite3.OperationalError:
  pass


def create():
  users = [ # Cada usuario nuevo que se quiera agregar, debe ponerse de primero en esta lista, no olvidar la coma al final de la tupla.
    (10123119, 'Wilfredo Ruiz', 'Bicentenario', 'Ahorro', 1305.6, 1901),
    (14335217, 'Virginia Navas', 'Bicentenario', 'Ahorro', 1500, 1234),
    (26141349, 'Anthony Silva', 'B.O.D.', 'Corriente', 1200, 2614),
  ]

  try:
    cursor.executemany('INSERT INTO Cuentas VALUES (?, ?, ?, ?, ?, ?)', users)
  except sqlite3.IntegrityError:
    pass


def read():
  print('-' * 60, '\nLISTADO DE USUARIOS CON CUENTAS')
  print('-' * 60)
  cursor.execute('SELECT * FROM Cuentas')
  get_users = cursor.fetchall()
  for user in get_users:
    print('Cédula:', user[0], '- Nombre:', user[1], '- Banco:', user[2], '- Saldo:', user[3])


def update():
  read()
  print('-' * 60, '\nACTUALIZANDO USUARIOS')
  print('-' * 60)
  id = input('Escriba la cédula de usuario a actualizar: ')
  cursor.execute(f'SELECT * FROM Cuentas WHERE Cedula = {id}')
  get_id = cursor.fetchall()
  for i in get_id:
    i = i[0]
    print('cedula | nombre | banco | saldo')
    campo = input('¿Que desea actualizar?: ')
    campo.lower
    nuevo_valor = input('Diga el nuevo valor del campo: ')
    cursor.execute(f'UPDATE Cuentas SET {campo} = "{nuevo_valor}" WHERE cedula = {i}')
    print('Actualizado con éxito!')


def delete():
  read()
  print('-' * 60, '\nBORRANDO USUARIOS')
  print('-' * 60)
  id = input('Escriba la cédula de usuario a borrar: ')
  cursor.execute(f'SELECT * FROM Cuentas WHERE Cedula = {id}')
  get_id = cursor.fetchall()
  for i in get_id:
    i = i[0]
    print('si - no')
    advertencia = input('¿Usted entiende que el usuario será borrado permanentemente?: ')
    advertencia.lower
    if advertencia == 'si':
      cursor.execute(f'DELETE * FROM Cuentas WHERE cedula = {i}')
      print('Usuario Borrado Exitosamente')
      read()
    else:
      print('Borrar usuarios CANCELADO')


conexion.commit()
conexion.close()