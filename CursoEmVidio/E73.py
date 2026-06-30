brasileirao = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'Sao Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco da Gama', 'Vitoria', 'Atletico Mineiro', 'Fluminense', 'Gremio', 'Juventude', 'Bragantino', 'Paranaense', 'Criciuma', 'Atletico Goianiense', 'Cuiaba')

print(f'\nLos primeros 5 son: {brasileirao[:5]}')
print(f'\nLos ultimos 4 son: {brasileirao[-4:]}\n')
print(sorted(brasileirao))
print(f'\nEl Sao Paulo esta en: {brasileirao.index('Sao Paulo') + 1} posicion')