from  cosas import Libro, Autor, Alumno

def main():
    l1= Libro.libro_planeta("El perfume", Autor("Patrick", "PS"), 1980)
    print(l1)
    #Codigo para cambiar el pseudonimo
    l1.autor.pseudonimo = l1.autor.pseudonimo.lower()
    print(l1)

    print("-----------Herencia------------")
    al2 = Alumno("Jose", 19, "324224", "Ico", 9)
    al2.nombre= "Pepe"
    print(vars(al2))

main()