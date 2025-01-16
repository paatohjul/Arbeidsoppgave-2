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





def hent_data_for_land(land):
    if land in data:
        hovedstad, befolkning = data[land]
        print(f"Hovedstad: {hovedstad}, Befolkning: {befolkning} millioner")
    else:
        print(f"{land} finnes ikke i listen.")

land = input("Skriv inn ett land: ")
land = land.capitalize()
print(hent_data_for_land(land))


#legger inn ett nytt land
nytt_land = input("Skriv inn det nye landet: ")
nytt_land = nytt_land.capitalize() #Lager stor bokstav
ny_hovedstad = input(f"Skriv inn hovedstaden i {nytt_land}: ")
ny_hovedstad = ny_hovedstad.capitalize()
ny_inb_ant = float(input(f"Skriv inn antall innbyggere i {ny_hovedstad}: "))

data[nytt_land] = [ny_hovedstad, ny_inb_ant]


land = input("Skriv inn ett land: ")
land = land.capitalize()
print(hent_data_for_land(land))
    

