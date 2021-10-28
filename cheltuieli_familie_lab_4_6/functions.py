
# Creating a dictionary to store data
global numar_cheltuiala
numar_cheltuiala = 1
cheltuieli={}

def verifica_user_input_int(message):
    """Verifica ca inputul utilizatorului sa fie de tip int"""

    # mesajul de input nu e un numar
    valid_input = False

    # initializeaza input
    user_input = ""

    # inputul tot nu e un numar
    while not valid_input:
        try:
            user_input = int(input(message))
            valid_input = True
        except ValueError:
            print("Introdu un numar!")

    return user_input


def input_adauga_cheltuieli():
    """Preia inputul userului"""

    ziua_mesaj = "Introdu ziua in care cheltuiala a fost facuta:"

    ziua = verifica_user_input_int(ziua_mesaj)

    suma_mesaj = "Introdu suma cheltuita:"

    suma = verifica_user_input_int(suma_mesaj)

    print("Tipurile de cheltuieli sunt: mancare, intretinere, imbracaminte, telefon, altele")

    tipul = input("Introdu tipul cheltuielii:")

    return ziua,suma,tipul # Returneaza parametrii necesari


def validare_tip_cheltuiala(tipul):
    """Verifica daca tipul cheltuielii este valid"""

    tipuri_cheltuieli = ['mancare', 'intretinere', 'imbracaminte', 'telefon', 'altele']

    while tipul not in tipuri_cheltuieli:
        # Indicam userului faptul ca nu a introdus o optiune valida

        tipul = input("Acest tip nu exista.Alege unul dintre tipurile de cheltuilei :")

    return tipul

def test_validare_tip_cheltuiala():
    """Testeaza functia validare_tip_cheltuiala"""

    assert validare_tip_cheltuiala('mancare') == 'mancare'

test_validare_tip_cheltuiala()

def adauga_cheltuieli(ziua,suma,tipul):
    """Adauga o cheltuiala"""

    global numar_cheltuiala
    cheltuieli[numar_cheltuiala]={'ziua':ziua,  'suma':suma,  'tipul':tipul}
    numar_cheltuiala += 1


def stergere_cheltuiala_ziua(ziua_data):
    """Sterge cheltuielile dintr o zi data"""

    for entry in list(cheltuieli):
        if cheltuieli[entry]['ziua']  == ziua_data:
            del cheltuieli[entry]


def stergere_cheltuiala_interval(ziua_inceput,ziua_sfarsit):
    """Sterge cheltuielile dintr un interval de timp"""

    for entry in list(cheltuieli):
        if cheltuieli[entry]['ziua']  >= ziua_inceput and cheltuieli[entry]['ziua'] <= ziua_sfarsit:
            del cheltuieli[entry]


def stergere_cheltuiala_tip(tipul_dat):
    """Sterge cheltuielile de un anumit tip"""

    for entry in list(cheltuieli):
        if cheltuieli[entry]['tipul']  == tipul_dat:
            del cheltuieli[entry]


def afisare_meniu_stergere():
    """Afiseaza meniul de stergere al cheltuielilor"""

    print("Alege una dintre urmatoarele actiuni:\n")

    print("(a) Șterge toate cheltuielile pentru ziua dată")
    print("(b) Șterge cheltuielile pentru un interval de timp")
    print("(c) Șterge toate cheltuielile de un anumit tip")
    print("(d) Revino la meniul principal")

def input_optiune_submeniu():
    """Preia inputul pentru submeniu"""

    optiune_submeniu = input("Introdu una dintre optiuni (a,b,c,d):")

    return optiune_submeniu

def validare_optiune_submeniu(optiune_submeniu):
    """Valideaza optiunea submeniu"""

    optiuni_sub = ['a', 'b', 'c', 'd']

    while optiune_submeniu not in optiuni_sub:
        optiune_submeniu = input("Alege o optiune valida: ")
    return optiune_submeniu

def input_interval_timp():
    """Preia inputul userului - intervalul de timp"""

    ziua_inceput_mesaj = "Alege ziua de inceput pentru care sa stergi cheltuielile: "
    ziua_inceput = verifica_user_input_int(ziua_inceput_mesaj)

    ziua_sfarsit_mesaj = "si ziua de sfarsit: "
    ziua_sfarsit = verifica_user_input_int(ziua_sfarsit_mesaj)

    return ziua_inceput,ziua_sfarsit

def afisare_meniu_filtrare():
    """Afisare submeniu filtrare"""

    print("Alege una dintre urmatoarele actiuni:\n")

    print("(a) Elimină toate cheltuielile de un anumit tip")
    print("(b) Elimină toate cheltuielile mai mici decât o sumă dată")
    print("(c) Revino la meniul principal")


def input_optiune_submeniu_filtrare():
    """Preia inputul pentru submeniu filtrare"""

    optiune_submeniu_filtrare = input("Introdu una dintre optiuni (a,b,c):")

    return optiune_submeniu_filtrare

def validare_optiune_submeniu_filtrare(optiune_submeniu_filtrare):
    """Valideaza optiunea submeniu filtrare"""

    optiuni_sub_filtrare = ['a', 'b', 'c']

    while optiune_submeniu_filtrare not in optiuni_sub_filtrare:
        optiune_submeniu_filtrare = input("Alege o optiune valida: ")
    return optiune_submeniu_filtrare

def filtreaza_cheltuieli_mai_mici_decat_suma(suma_data):
    """Filtreaza cheltuielile mai mici decat suma introdusa de catre user"""

    for entry in list(cheltuieli):
        if cheltuieli[entry]['suma'] >= suma_data:
            print(cheltuieli[entry])

def filtreaza_cheltuieli_tipul_dat(tipul_dat):
    """Filtreaza cheltuieli de un anumit tip"""
    for entry in list(cheltuieli):
        if cheltuieli[entry]['tipul'] != tipul_dat:
            print(cheltuieli[entry])

def afisare_meniu_cautare():
    """Afiseaza meniul de cautare a cheltuielilor"""

    print("Alege una dintre urmatoarele actiuni:\n")

    print("(a) Tipărește toate cheltuielile mai mari decât o sumă dată")
    print("(b) Tipărește toate cheltuielile efectuate înainte de o zi dată și mai mici decât o sumă (WIP)")
    print("(c) Tipărește toate cheltuielile de un anumit tip.")
    print("(d) Revino la meniul principal")

def afisare_sume_mai_mari(suma_data_cautare):
    """Cauta cheltuieli mai mari decat o suma data"""

    for entry in list(cheltuieli):
        if cheltuieli[entry]['suma'] > suma_data_cautare:
            print(cheltuieli[entry])

def cautare_cheltuieli_tipul_dat(tipul_dat):
    """Cauta cheltuieli de un anumit tip"""

    for entry in list(cheltuieli):
        if cheltuieli[entry]['tipul'] == tipul_dat:
            print(cheltuieli[entry])





