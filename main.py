print("###############################################################################################")
print("# Hola ! Bienvenidos en el Aplicacion de gestion de contact.                                  #")
print("# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #")
print("# Autor : Laura AMIOT                                                                         #")
print("# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #")
print("###############################################################################################")
import sys
from Quienes import apl_dep, qui_escritura
from LoSabias import verif_droit
from Menu import menu
from Mod_contacto_list import listar_contacto, eliminar_contact, agregar_contact, modifiar_contacto
from Agreg_admin import agreg_admin
from Secu_admin import Droit_action

print(
    "               _____            _             _                         _ _ \n              / ____|          | |           | |            /\         | (_)\n             | |     ___  _ __ | |_ __ _  ___| |_ ___      /  \   _ __ | |_ \n             | |    / _ \| '_ \| __/ _` |/ __| __/ _ \    / /\ \ | '_ \| | |\n             | |___| (_) | | | | || (_| | (__| || (_) |  / ____ \| |_) | | |\n             \_____\___/|_| |_|\__\__,_|\___|\__\___/  /_/    \_\ .__/|_|_|\n                                                                 | |        \n                                                                 |_|        ")


def qui_main():
    qui = apl_dep()
    qui_verif = qui_escritura(qui)
    return qui_verif


Liste_menu = [1, 2, 3, 4, 5, 0]


def sorti_menu(val_menu):
    if int(val_menu) in Liste_menu:
        if val_menu == "0":
            print("###############################################################################################")
            print(
                "   ___                _               _               _                                _    \n  / _ \_ __ __ _  ___(_) __ _ ___    | |__   __ _ ___| |_ __ _   _ __  _ __ ___  _ __ | |_ ___  \n / /_\/  __/ _` |/ __| |/ _` / __|   |  _ \ / _  / __| __/ _  | |  _ \|  __/ _ \|  _ \| __/ _ \ \n/ /_\\| | | (_| | (__| | (_| \__ \_  | | | | (_| \__ \ || (_| | | |_) | | | (_) | | | | || (_) |\n\____/|_|  \__,_|\___|_|\__,_|___( ) |_| |_|\__,_|___/\__\__,_| | .__/|_|  \___/|_| |_|\__\___/ \n                                 |/                             |_|                             ")
            sys.exit()
        if val_menu == "1":
            if Droit_action(qui_verif, int(val_menu)) is True:
                agregar_contact()
                new_val_menu = menu()
                sorti_menu(new_val_menu)
            else:
                print("Vous n'avez pas les droits pour cela... ")
                new_val_menu = menu()
                sorti_menu(new_val_menu)
        if val_menu == "2":
            if Droit_action(qui_verif, int(val_menu)) is True:
                modifiar_contacto()
                new_val_menu = menu()
                sorti_menu(new_val_menu)
            else:
                print("Vous n'avez pas les droits pour cela... ")
                new_val_menu = menu()
                sorti_menu(new_val_menu)
        if val_menu == "3":
            if Droit_action(qui_verif, int(val_menu)) is True:
                eliminar_contact()
                new_val_menu = menu()
                sorti_menu(new_val_menu)
            else:
                print("Vous n'avez pas les droits pour cela... ")
                new_val_menu = menu()
                sorti_menu(new_val_menu)
        if val_menu == "4":
            if Droit_action(qui_verif, int(val_menu)) is True:
                listar_contacto()
                new_val_menu = menu()
                sorti_menu(new_val_menu)
            else:
                print("Vous n'avez pas les droits pour cela... ")
                new_val_menu = menu()
                sorti_menu(new_val_menu)
        if val_menu == "5":
            if Droit_action(qui_verif, int(val_menu)):
                agreg_admin()
                new_val_menu = menu()
                sorti_menu(new_val_menu)
            else:
                print("Vous n'avez pas les droits pour cela... ")
                new_val_menu = menu()
                sorti_menu(new_val_menu)
    else :
        print("entrada no possible : OUT ! ")
        sys.exit()

qui_verif = qui_main()
if verif_droit(qui_verif) != True:
    print("Je ne te connais pas dehors !")
    sys.exit()

val_menu = menu()
sorti_menu(val_menu)
