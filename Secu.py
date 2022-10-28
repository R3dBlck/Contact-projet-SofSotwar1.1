
def secu_num_tel(Num):
    if len(Num) == 10 and isinstance(int(Num), (int, float)) == True:
        print("# SECURITY # (!) Numero de tel OK !!! (!) # SECURITY #")
        return True


def secu_appe_nombre(entry):
    if entry.isalpha() is True:
        print("# SECURITY # (!) Entry Nombre /Ap is OK !!! (!) # SECURITY #")
        return True


def droit_admin(qui_verif, for_what):
    fichier_admin = open("Bdatos_Admin.txt", "r")
    Admin = fichier_admin.readlines()
    fichier_admin.close()
    for i in range(0, len(Admin)):
        User = Admin[i].split(";")
        if User[0] == qui_verif:
            print(User[for_what])


def escritura_correcta_appellido(ape):
    new_ape = ape.upper()
    print("# SECURITY # (!) Entry Ape escritura correcto en basa de datos (!) # SECURITY #")
    return new_ape


def escritura_correcta_nombre(nom):
    new_nom = nom.title()
    print("# SECURITY # (!) Entry Nom escritura correcto en basa de datos (!) # SECURITY #")
    return new_nom


#def entrada_admin(entrada):
#    if entrada is "T" or "F":
#        print("# SECURITY # (!) Entry F or T OK !!! (!) # SECURITY #")
#        return True
