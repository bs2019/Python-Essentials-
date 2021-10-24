#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 10:19:35 2021

@author: macbookpro
"""

# Escribir un programa que pregunte al ...
#usuario los productos de un carrito de compras,
# separados por comas, y muestre por pantalla cada
# uno de los productos en una línea 

compras = input("Ingrese 4 productos del carrito de compras separados en ")
z=compras.split(",")
print(f"{z[0]} \n{z[1]} \n{z[2]} \n{z[3]}")


print(compras.replace(",","\n"))