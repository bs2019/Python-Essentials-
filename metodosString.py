#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 09:19:06 2021

@author: macbookpro
"""

var_prueba= "   mensaje de trabajo para pruebas   "
print(len(var_prueba), "el len si se ejecuta en el shell pero no desde el código")
print(var_prueba[-1])

var1=90
var1+=1
print(var1)

var_prueba=var_prueba+'texto adicional'
print(var_prueba)
print(var_prueba[:7]) #[0:7]
print(var_prueba[7:])
print(var_prueba[-8:-1])#EL LÍMITE SUPERIOR E ABIETO
print(var_prueba[-8:])


print(var_prueba.upper())
print(var_prueba.rstrip())
print(var_prueba.replace("e","100"))
print(var_prueba.split())
correo = "xime@hotmail.com"
print(correo.split("@"))



