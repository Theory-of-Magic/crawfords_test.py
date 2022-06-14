import matplotlib.pyplot as plt
import numpy as np
modifier = 0
dicetype = int(input(print("How many sides does your dice have?")))
rolls = int(input(print("How many rolls?")))
PI = 3.1415926535897932384626433832795

A = (0.5(dicetype + 1) * rolls + modifier ) * ((PI / 6)(dicetype ^ 2 - 1 ))^ -(1/2)
sigma = np.sqrt((rolls * (dicetype ^ 2 - 1)) / 12) 
