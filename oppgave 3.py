# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 19:02:21 2025

@author: knutj
"""

import numpy as np

v_grad = float(input('Skriv inn gradtallet:' ))

v_rad = v_grad * np.pi/180

print(f"{v_grad} grader er {v_rad:.2f} radianer") 