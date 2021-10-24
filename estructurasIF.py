#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 08:09:39 2021

@author: macbookpro
"""

# edad = int(input("Ingrese su edad como un número:" ))

#if edad < 13 and edad >=0:
#    print("Usted es niñ@")
#elif edad<18 and edad>=13:
#    print("Usted es adolescente")
#elif edad >=18 and edad<45:
#    print("Usted es adulto joven")
#else:
#    print("Usted es adulto mayor")

# if edad < 13 and edad >=0:
#     print("Usted es niñ@")
# elif edad<18:
#     print("Usted es adolescente")
# elif edad<45:
#     print("Usted es adulto joven")
# else:
#     print("Usted es adulto mayor")


# compras = input()
# compras1 = compras.split(",")
# for i in compras1:
#      print(i)

# WHILLE
# var1 = 1
# while var1<10:
#     print(var1)
#     var1+=1
# print("The End")


# num = int(input("Escriba un número positivo: "))
# while num <=0:
#     print("Número no positivo, vuelva a ingresar")
#     num = int(input("Escriba un número positivo: "))
# print("El número es correcto")

"""
Escribir un código que permita mostrar en pantalla lo que el 
usuario ingresa por teclado. Cuando el usuario ingresa la palabra 
salir (puede ser en mayúsculas o minúsculas) se debe terminar la ejecución.
"""

# palabra = ""
# while palabra.lower() != "salir":
#     print(palabra)
#     palabra = input("Ingrese un palabra: ")
# print("Ha terminado")


# control = True
# while control == True:
#     palabra = input("Ingrese un palabra: ")
#     if palabra.lower() == "salir":
#         break
#     print(palabra)
# print("end")


'''
CONTINUE
'''

var1 = 1
while var1<10:
    if var1== 5:
        var1+=1
        continue
    print(var1)
    var1+=1
        
print("The End")


for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print ('Current Letter :', letter)

var = 10                    # Second Example
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print ('Current variable value :', var)
print ("Good bye!")



'''
FOR
'''
for i in [78,32,-3,'3']:
    print("number")
    print(i)
for i in "palabra":
    print("number")
    print(i)

lst = range(4)
print(lst)



for i in range(4):
    print("number")
    print(i)


'''
Escribir un programa que pregunte al usuario una frase
 y una letra, y muestre por pantalla el número de veces que 
 aparece la letra en la frase.
'''
frase_larga = input("Ingreso de la frase: ")
letra_bsq = input("Letra a contar: ")
contar = 0
for i in frase_larga:
    if letra_bsq == i.lower() or letra_bsq == i.upper():
        contar+=1
print (contar)








