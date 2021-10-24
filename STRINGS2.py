#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 08:07:34 2021

@author: macbookpro
"""
#Pruebas con STRINGS
print("Mensaje de prueba uno\nSegunda línea del mensaje \nbackslahsn da un salto de línea")
print("the number is", 4, 
      "\nVARIOS tipos de datos",
      4.5)
var1='TEXT'
var2=54
var3=3.5
var4="text2"

print('Se concatena STRING')
print(var1 + str(var2)+str(var3)+ var4)
print(1+2+3)

print('\nNUEVA FORMA DE ESCRITURA version3.5 Con f todo es STRING')
print(f"variable1: {var1}\nVariable3: {var3*2}\nVarible4:{var4}")

print('\nTipo FORMAT (método)')
print("IMPLICIT- My last name is: {}, my name is:{}, and I am {} years old".format("Sánchez", "Xime", 31))
print("EXPLICIT- My last name is: {0}, my name is:{1}, and I am {2} years old".format("Sánchez", "Xime", 31))
print("EXPLICIT- My last name is: {1}, my name is:{1}, and I am {1} years old".format("Sánchez", "Xime", 31))
print("EXPLICIT- My last name is: {lastn}, my name is:{name}, and I am {age} years old".format(lastn="Sánchez", name="Xime"*2, age=31-1))

