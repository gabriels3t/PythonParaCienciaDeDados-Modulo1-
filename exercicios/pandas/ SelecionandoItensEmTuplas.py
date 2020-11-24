carros = (
    (
        'Jetta Variant',
        'Motor 4.0 Turbo',
        2003,
        False,
        ('Rodas de liga', 'Travas elétricas', 'Piloto automático')
    ),
    (
        'Passat',
        'Motor Diesel',
        1991,
        True,
        ('Central multimídia', 'Teto panorâmico', 'Freios ABS')
    )
)

print(carros[0][3])
print(carros[-1][-1][-1])
print(carros[0][-1][:2])