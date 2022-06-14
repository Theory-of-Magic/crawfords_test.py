import matplotlib.pyplot as plt
import numpy as np
modifier = float(0)
rolls = float(input(print("How many rolls?")))
dicetype = float(input(print("How many sides does your dice have?")))
PI = 3.1415926535897932384626433832795

A = ((0.5 * (dicetype + 1.0) * rolls + modifier ) * (((PI / 6.0) * rolls) * (dicetype ** 2.0 - 1.0 ))** -0.5)
sigma = np.sqrt((rolls * (dicetype ** 2.0 - 1.0)) / 12.0) 

print("A = ", A)
print("Sigma = ", sigma)
