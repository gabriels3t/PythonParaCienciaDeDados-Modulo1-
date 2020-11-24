import numpy as np

peso = np.array([106.0,68.5,75.0])
altura = np.array([1.9,1.53,1.75])
imc = peso/ (altura * altura)
print(imc)