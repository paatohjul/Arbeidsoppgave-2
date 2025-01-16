# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 12:22:19 2025

@author: knutj

Skriv en kode som plotter funksjonen 𝑓(𝑥) = −x^2 − 5, for x på intervallet [-10,10].
Hint: np.linspace(-10, 10, 200) gir en array med 200 punkter jevnt fordelt på intervallet 
[-10,10].

"""

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-10, 10, 200) #dette gir ett x array fra -10 til 10 og 200 punter

f_x = -x**2 - 5

plt.plot(x,f_x, label="f(x)=-x^2-5")
plt.xlabel("x")
plt.ylabel("fx)")
plt.title("Plot av funskjonen f(x)=-x^2-5") 
plt.legend()
plt.grid(True)
plt.show()
