# set significa : grupo, conjunto o arreglo
primer = {1, 1, 5, 5, 2, 3, 4}
print(primer)

primer.add(8)
primer.remove(1)

print(primer)

primer.add(1)

print(primer)

segundo = [85, 4, 5]

segundo = set(segundo)

# unión: une los elementos de los sets eliminando los valores duplicados
print(primer | segundo)

# interscción: devuelve solo los valores que son comunes entre los sets
print(primer & segundo)

#
print(primer - segundo)

# diferencia simetrica: nos devuelve los elementos que se encuentren en el primero y en el segundo pero no se cuentren entre uno y el otro
print(primer ^ segundo)
