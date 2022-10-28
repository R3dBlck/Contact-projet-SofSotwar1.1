def verif_droit(qui_verif):
    fichier_admin = open("Bdatos_Admin.txt", "r")
    Admin = fichier_admin.readlines()
    fichier_admin.close()
    for i in range(0, len(Admin)):
        User = Admin[i].split(";")
        if User[0] == qui_verif:
            return True


