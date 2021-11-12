def escribir_agenda(nombre_agenda, agenda_digital):
    """Escribe en la agenda en un fichero de texto

    Parametros posicionales
    nombre_agenda -- str que respresenta el nombre de la agenda en el disco
    agenda_digital -- dict que representa la agenda digital y los contactos
    """
    agenda_fichero = open(nombre_agenda, 'w') #abre el fichero para modo escritura

    # Esta sentencia escribe el diccionario en el fichero
    agenda_fichero.write(str(agenda_digital))#escribe en el fichero convirtiendo el dict en str
    # Esta sentencia cierra el fichero que has abierto con la funcion open()
    agenda_fichero.close()


def leer_agenda(nombre_agenda):
    """Lee la agenda digital de un fichero en disco.

    Parametros posicionales
    nombre_agenda -- str
    """
    agenda_digital_lectura = open(nombre_agenda, 'r')
    # Esta sentencia lee todas las líneas del fichero y las asigna a la variable agenda_digital
    agenda_digital = agenda_digital_lectura.readlines()

    # Esta sentencia cierra el fichero que has abierto con la función open()
    agenda_digital_lectura.close()
    return eval(agenda_digital[0])  # eval lo devuelve en forma de diccionario


def solicitar_contacto_agenda():
    """Esta informacion solicita los datos de un nuevo contacto al usuario"""
    nombre = input("Introduce el nombre completo del contacto: ")
    direccion = input("Introduce el direccion del contacto: ")
    email = input("Introduce el email del contacto: ")
    tel = input("Introduce el telefono del contacto: ")
    # construimos un diccionario con los valores recibidos
    contacto = {
        "nombre": nombre,
        "direccion": direccion,
        "email": email,
        "tel": tel
    }

    return contacto


def crear_contacto(agenda_digital, nuevo_contacto):
    """Introduce un nuevo contacto en la agenda

    parametros posicionales
    agenda_digital -- dict que representa la agenda digital existente
    nuevo_contacto -- dict que representa un nuevo contacto
    """

    agenda_digital[nuevo_contacto["nombre"]] = {
        "direccion": nuevo_contacto["direccion"],
        "email": nuevo_contacto["email"],
        "tel": nuevo_contacto["tel"],
    }

    return agenda_digital

def consultar_contacto_agenda(agenda_digital):
    """Esta funcion consulta un contacto en la agenda"""
    nombre = input("introduce el nombre completo del contacto: ")
    print("\n[+]", nombre)
    print("\tDireccion: ", agenda_digital[nombre]["direccion"])
    print("\tEmail: ", agenda_digital[nombre]["email"])
    print("\tTelefono: ", agenda_digital[nombre]["tel"])


agenda_digital = {}
escribir_agenda ('agenda_digital.txt', agenda_digital)
nuevo_contacto  = solicitar_contacto_agenda()
agenda_digital = crear_contacto(agenda_digital,nuevo_contacto  )
escribir_agenda ('agenda_digital.txt', agenda_digital)

# para consultar contacto
# agenda_digital = leer_agenda("agenda_digital.txt")
# consultar_contacto_agenda(agenda_digital)