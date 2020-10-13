import numpy as np

ceros = np.zeros((450, 620))
print(ceros)
for x in ceros.shape[0]:
    for y in ceros.shape[1]:
        if 210 < x < 418:
            if 0 < y < 153:
                ceros[x][y] = 1

print(ceros[215,5])
