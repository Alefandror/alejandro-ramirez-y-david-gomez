pip install bigtree


from bigtree import Node, print_tree

# 1. Definimos la raíz
root = Node("A")

# 2. Creamos el primer nivel de hijos
b = Node("B", parent=root)
c = Node("C", parent=root)
d = Node("D", parent=root)

# 3. Agregamos más profundidad (árbol no binario: 'B' tiene 3 hijos)
e = Node("E", parent=b)
f = Node("F", parent=b)
g = Node("G", parent=b)

# 4. Agregamos hijos a otros nodos
h = Node("H", parent=c)
i = Node("I", parent=d)

# Visualizamos el resultado
print_tree(root)