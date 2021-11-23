from . import info


def ask_group_name():
    group_name = input("Entrez le nom du groupe: ")
    info.group_name = group_name
    return group_name


def ask_date():
    date = input("Entrez la date: ")
    info.date = date
    return date


def ask_nbr_friends():
    x = False
    while not x:
        nbr_friends = input("Entrez le nombre d'amis dans le groupe: ")
        if nbr_friends.isnumeric():
            info.nbr_friends = int(nbr_friends)
            return
        else:
            print("Entrez une donnée numérique pour le nombre d'amis dans le groupe")


def ask_basic_info():
    ask_group_name()
    ask_date()
    ask_nbr_friends()
    info.complet_name = "{}-{}".format(info.group_name, info.date)
    print(info.complet_name)