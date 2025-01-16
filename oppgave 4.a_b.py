# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 19:08:00 2025

@author: knutj
"""

data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.892],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873],
        }

land = input("Skriv inn ett land: ")
land = land.capitalize()

if land in data:
    hovedstad, befolkning = data[land]
    print(f"Hovedstad: {hovedstad}, Befolkning: {befolkning} millioner")
else:
    print(f"{land} finnes ikke i listen.")

    