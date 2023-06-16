

from cosas import *

def main():
    l1 = Libro.libro_planeta("EL perfume", Autor("Patrik", "PS"), 1980)
    print(l1)


l1.autor.pseudonimo = l1.autor.pseudonimo.lower()
print(l1)
print("---------es herencia---------" )
al2 = Alumno("jose", 19, "23232", "ICO", 9)
al2.nombre = "Pepe"
print(vars(al2))

