def apl_dep():
    qui = input("# ------- >  Quien es ? ")
    return qui


def qui_escritura(qui):
    if qui.isalpha():
        new_qui = qui.lower()
        return new_qui
    else:
        print("Votre entrée n'est pas correcte. Recommancé.")



