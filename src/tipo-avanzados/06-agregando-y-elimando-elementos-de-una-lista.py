cervezas = [
    'pilsener',
    'lager',
    'ale',
    "regia",
    'stout',
    "regia",
    'ipa'
]

print(cervezas)

cervezas.insert(2, 'bock')
print(cervezas)

cervezas.append('weizen')
print(cervezas)

cervezas.remove('regia')
print(cervezas)

cervezas.pop()
print(cervezas)

cervezas.pop(1)
print(cervezas)

del cervezas[0]
print(cervezas)

cervezas.clear()
print(cervezas)
