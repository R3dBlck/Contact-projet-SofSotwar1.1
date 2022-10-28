from Secu import secu_num_tel, secu_appe_nombre, escritura_correcta_appellido, escritura_correcta_nombre


def listar_contacto():
    fichier_contact = open("Bdatos.txt", "r")
    contact = fichier_contact.readlines()
    fichier_contact.close()
    print("                     ##############################################")
    print("                     #--------------------------------------------#")
    for i in range(0, len(contact)):
        c = contact[i].split(";")
        print("                     Contacto n° : ", i)
        for j in range(0, len(c)):
            print("                     ", c[j])
        print("                     #--------------------------------------------#")
    print("                     ##############################################")


def eliminar_contact():
    listar_contacto()
    fichier_contact = open("Bdatos.txt", "r")
    contact = fichier_contact.readlines()
    fichier_contact.close()
    num_ct = input("¿A quién quieres eliminar? ")

    a = ""
    for i in range(0, len(contact)):
        if i != int(num_ct):
            c = contact[i].split(";")
            for j in range(0, 3):
                a = a + c[j]
                if j == 1 or j == 0:
                    a = a + ";"
                # print(a)

    fichier_contact = open("Bdatos.txt", "w")
    fichier_contact.truncate()
    fichier_contact.write(a)


def agregar_contact():
    nombre = input("Nombre del contacto ")
    if secu_appe_nombre(nombre) != True:
        print("Error por el Nombre")
        agregar_contact()
    nombre = escritura_correcta_nombre(nombre)

    apellido = input("Appellido del contacto ")
    if secu_appe_nombre(apellido) != True:
        print("Error por el Appellido")
        agregar_contact()
    apellido = escritura_correcta_appellido(apellido)

    num_tel = input("Numero de telephono del contacto ")
    if secu_num_tel(num_tel) != True:
        print("Error por el telefono")
        agregar_contact()

    fichier_contact = open("Bdatos.txt", "a")
    a = (nombre + ";" + apellido + ";" + num_tel)
    fichier_contact.write("\n")
    fichier_contact.write(a)
    fichier_contact.close()


def modifiar_contacto():
    listar_contacto()
    fichier_contact = open("Bdatos.txt", "r")
    contact = fichier_contact.readlines()
    fichier_contact.close()

    listar_contacto()
    num_ct = input("¿A quién quieres modificar? ")

    a = ""
    for i in range(0, len(contact)):
        if i != int(num_ct):
            c = contact[i].split(";")
            for j in range(0, 3):
                a = a + c[j]
                if j == 1 or j == 0:
                    a = a + ";"
                # print(a)

    fichier_contact = open("Bdatos.txt", "w")
    fichier_contact.truncate()
    fichier_contact.write(a)

    nombre = input("Nombre del contacto ")
    if secu_appe_nombre(nombre) != True:
        print("Error por el Nombre")
        agregar_contact()
    nombre = escritura_correcta_nombre(nombre)

    apellido = input("Appellido del contacto ")
    if secu_appe_nombre(apellido) != True:
        print("Error por el Appellido")
        agregar_contact()
    apellido = escritura_correcta_appellido(apellido)

    num_tel = input("Numero de telephono del contacto ")
    if secu_num_tel(num_tel) != True:
        print("Error por el telefono")
        agregar_contact()

    a = (nombre + ";" + apellido + ";" + num_tel)
    fichier_contact.write("\n")
    fichier_contact.write(a)
    fichier_contact.close()
