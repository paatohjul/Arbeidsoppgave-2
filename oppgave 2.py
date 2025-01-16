# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 18:49:03 2025

@author: knutj
"""
import numpy as np

# Tast inn hvor mange elever som deltar
antall_elever = int(input('Skriv inn antall elever:' ))

# Regn ut hvor mange pizzaer det må handles inn. 
# Det går 1/4 pizza pr. person og man kan ikke handle inn deler av en pizza

antall_pizza = np.ceil(antall_elever/4)

print(f"Det må kjøpes inn {antall_pizza:.0f} pizza for at alle skal få sin del.")
