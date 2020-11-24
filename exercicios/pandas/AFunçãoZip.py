nomes = ['Passat', 'Crossfox', 'DS5', 'C4', 'Jetta']
kms = [15000, 12000, 32000, 8000, 50000]

for nomes, kms in zip(nomes, kms):
    if kms < 20000:
        print(nomes)