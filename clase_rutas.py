
# contents = file.read()
# print(contents)
# # Se cierra para liberar espacio en la ram de la computadora :
# file.close()'''
#
# # Otra manera de traer archivos sin usar mucho espacio es esta notación:
# '''with open('my_file.txt') as file:
#     contents = file.read()
#     print(contents) '''
# # Así solo se abre cuando se desee
#
# # Se puede import el archivo de diferentes maneras y con diferentes parámetros:
# '''with open('my_file.txt', mode='a') as file: # a de append
#     file.write('\n new text')'''
#
# # Se puede crear archivos de la nada, solo con modo write = w
#
# with open('my_file_2.txt', mode = 'w') as file2:
#     file2.write('new file')
#
# # Con esto aprendido, se modificó el codigo de snake, para tener un highcore
#
#
# # Ahora buscamos conocer los caminos para encontrar archivos en el ordenador
# # Se movió el archivo my_file_2.txt a el escritorio
# # Hacer funcionar este codigo:
# '''with open('my_file_2.txt') as file :
#     contents = file.read()
#     print(contents)'''
# ruta = '/home/marco/Escritorio/my_file_2.txt'
# with open(ruta) as file:
#     contents = file.read()
#     print(contents)