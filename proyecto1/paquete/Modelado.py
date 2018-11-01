#Creación de clase persona
class Persona(object):
    def __init__(self):
        self.nombres = ""
        self.edad = 0
    #Métodos para agregar y obtener nombre y edad
    def agregar_nombres(self, n):
        self.nombres = n

    def agregar_edad(self, e):
        self.edad = e

    def obtener_edad(self):
        return self.edad

    def obtener_nombre(self):
        return self.nombres
    #Método para presentar los datos
    def presentar_datos(self):
        c = "%s-%s" % (self.obtener_edad(), self.nombres)
        return c


class Estudiante(Persona):
    #Método para definir atributos
    def __init__(self):
        super(Estudiante, self).__init__()
        self.nota = 0
    #Método para agregar nota a la persona
    def agregar_nota(self, nota):
        self.nota = nota
    #Presntación de los datos concatenando cadenas
    def presentar_datos(self):
        #c = '%s - %s -%s' % (self.nombres, self.edad, self.nota)
        c = '%s - %s' % (super(Estudiante, self).presentar_datos(),
                         self.nota)
        return c
