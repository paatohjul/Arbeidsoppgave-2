# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 10:46:53 2025

@author: knutj


Lag et program med en funksjon som tar a og b som inn-argumenter og som så 
regner ut arealet og «ytre» omkrets til en figur satt sammen av en rettvinklet trekant og en 
halvsirkel, se figuren under. Med «ytre» omkrets menes samlet lengde av de sorte strekene. 
Funksjonen skal returnere arealet og «ytre» omkrets, som så skrives til skjerm med passende 
tekst.

"""
import numpy as np

print("Vi skal måle omkretsen til en figur som består av en halvsirkel;med diameter A")
print("på topp av en rettvinklet trekant med kateter lengde A og B")
radius_a = float(input("Skriv inn diameter på halvsirkelen: "))/2 #Radius til halvsirkel
kat_b = float(input("Skriv inn lengden på kateter B: ")) #Kateter B

omkrets_halvsirkel = np.pi*radius_a
hyp_c = np.sqrt((radius_a*2)**2 + kat_b**2) #Hyptenusen

omkrets_figur = omkrets_halvsirkel + kat_b + hyp_c

areal_figur = (kat_b * hyp_c)/2 + np.pi*radius_a**2/2




print(f"Omkretsen til Figuren er {omkrets_figur:.2f}")

print(f"Arealet til Figuren er {areal_figur:.2f}")
