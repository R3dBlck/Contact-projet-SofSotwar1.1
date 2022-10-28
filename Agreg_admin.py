

def agreg_admin():
    nombre = input("Nombre del contacto ")
    if nombre.isalpha() == True :
        nombre = nombre.lower()
        Agreg_contacto = input("Agregar Contacto ? T or F")
        Modif_contacto = input("Modificar un contacto ? T or F ")
        Eliminar_contacto = input("Eliminar un contacto ? T or F")
        Listar_contacto = input("Listar un contacto ? T or F")
        Agregar_usario = input("Agregar un usario ? T or F")

        if Agreg_contacto == "F" or Agreg_contacto =="T" and Modif_contacto== "F" or Modif_contacto =="T" and Eliminar_contacto== "F" or Eliminar_contacto =="T" and Listar_contacto== "F" or Listar_contacto =="T" and Agregar_usario== "F" or Agregar_usario =="T":
            fichier_admin = open("Bdatos_Admin.txt", "a")
            a = ( nombre + ";" + Agreg_contacto + ";" + Modif_contacto + ";" + Eliminar_contacto + ";" + Listar_contacto + ";" + Agregar_usario+";")
            fichier_admin.write("\n")
            fichier_admin.write(a)
            fichier_admin.close()
            print("(!) Seguridad OK !! (!)")
        else:
            print("Erreure !! Ecrire T o F !! ")
            agreg_admin()
    else :
        print("Erreure !! Escribe correctament elle nombre")
        agreg_admin()
