# help(str.join)

tupla_str = ('Hola', 'Mundo', 'Tecnicatura', 'Universitaria')
mensaje = ' - '.join(tupla_str)
print(f'Mensaje: {mensaje}')

lista_cursos = ['Java', 'Python', 'JavaScript', 'Angular', 'Spring']
mensaje = ", ".join(lista_cursos)
print(f'Mensaje: {mensaje}')

cadena = 'HolaMundo'
mensaje = '.'.join(cadena)
print(f'Mensaje: {mensaje}')

diccionario = {'nombre': 'Hernán', 'apellido': 'Pérez', 'edad': '18'}
llaves = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
print(f'Llaves: {llaves}, Type: {type(llaves)} '
      f'Valores: {valores}, Type: {type(valores)} ')