class Autor:
    def __init__(self, nom, pseudo):
        self.__nombre = nom
        self.__pseudonimo = pseudo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nom):
        self.__nombre = nom


    @property
    def pseudonimo(self):
        return self.__pseudonimo

    @pseudonimo.setter
    def pseudonimo(self, pseudo):
        self.__pseudonimo = pseudo

    def __str__(self):
        return f"nombre: {self.__nombre} pseudonimo: {self.__pseudonimo}"
    def escribir(self):
        print(f"{self.__pseudonimo} esta escribiendo su siguiente libro")


class Libro:
        def __init(self, tit, aut, an, ed):
            self.__titulo = tit
            self.__autor = aut
            self.__ano = an
            self.__editorial = ed

        @property
        def titulo(self):
            return self.__titulo

        @titulo.setter
        def titulo(self, tit):
            self.__titulo = tit


        @property
        def autor(self):
            return self.__autor

        @autor.setter
        def autor(self, aut):
            self.__autor = aut

        @property
        def ano(self):
            return self.__ano

        @ano.setter
        def ano(self, an):
            self.__ano = an

        @property
        def editorial(self):
            return self.__editorial

        @editorial.setter
        def editorial(self, ed):
            self.__editorial

        def __str__(self):
            return f"""
            
            titulo ={self.__titulo}
            autor ={self.__autor}
            ano = {self.__ano}
            editorial ={self.__editorial}
            
            """

        @classmethod
        def libro_planeta(clscls, titulo, autor, ano):
            return cls(titulo, autor, ano, "Planeta")

        def leer(self, minutos):
            print(f"leyendo por {minutos} minutos")

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nom):
        self.__nombre = nom


class Alumno(Persona):
    def __init__(self, nombre, edad, numer_cuenta, carrera, promedio):
        super().__init__(nombre, edad)
        self.numero_cuenta = numer_cuenta
        self.__carrera = carrera
        self.__promedio= promedio





