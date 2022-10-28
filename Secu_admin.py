def Droit_gene(who):
    fichier_admin = open("Bdatos_Admin.txt", "r")
    Admin = fichier_admin.readlines()
    fichier_admin.close()
    for i in range(0, len(Admin)):
        User = Admin[i].split(";")
        if User[0] == who:
            return User


def Droit_action(who, action):
    list_droit = Droit_gene(who)
    #print(list_droit)
    if list_droit[action] == "T":
        print("Ok tu tiennes el DERECHA de hacer lo ! ")
        return True
    else:
        print("NO !! tu NO tiennes el derecha de haver lo ! ")
        return False
