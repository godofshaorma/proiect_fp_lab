from functions import *
from meniu import *

# Starting the program and generating the menu using the menu() function
menu()
option_message = "Bine ai venit in FamilyEconManager (1.0).Alege una dintre optiunile de mai sus: "
option = verifica_user_input_int(option_message)

# While loop for continous program use
while option != 7:

    if option == 1:

        # Adaugarea unei cheltuieli


        ziua, suma, tipul = input_adauga_cheltuieli() #Preia inputul clientului

        tipul = validare_tip_cheltuiala(tipul) #Valideaza tipul cheltuielii

        adauga_cheltuieli(ziua, suma, tipul) #Adaugam cheltuiala in memorie

    elif option == 2:

        # Stergerea unei cheltuieli

        afisare_meniu_stergere()

        optiune_submeniu = input_optiune_submeniu()

        optiune_submeniu = validare_optiune_submeniu(optiune_submeniu)

        while optiune_submeniu != 'd':

            if optiune_submeniu == 'a':
                """"Șterge toate cheltuielile pentru ziua dată"""

                ziua_data = int(input("Alege ziua pentru care sa stergi cheltuielile: "))

                stergere_cheltuiala_ziua(ziua_data)

            elif optiune_submeniu == 'b':
                """Șterge cheltuielile pentru un interval de timp"""

                ziua_inceput, ziua_sfarsit = input_interval_timp()

                stergere_cheltuiala_interval(ziua_inceput, ziua_sfarsit)

            elif optiune_submeniu == 'c':
                """Șterge toate cheltuielile de un anumit tip"""

                tipul_dat = input("Introdu tipul cheltuielii:")

                tipul_dat = validare_tip_cheltuiala(tipul_dat)

                stergere_cheltuiala_tip(tipul_dat)

            afisare_meniu_stergere()

            optiune_submeniu = input("Introdu una dintre optiuni (a,b,c,d):")

    elif option == 3:
        """Cautare in registrul de cheltuieli"""

        afisare_meniu_cautare()

        optiune_submeniu_cautare = input_optiune_submeniu()

        optiune_submeniu_cautare = validare_optiune_submeniu(optiune_submeniu_cautare)

        while optiune_submeniu_cautare != 'd':

            if optiune_submeniu_cautare == 'a':
                """"Tipareste toate cheltuielile mai mari decat o suma"""

                suma_data_cautare_mesaj = "Alege suma pentru care sa se afiseze cheltuielile mai mari: "
                suma_data_cautare = verifica_user_input_int(suma_data_cautare_mesaj)

                afisare_sume_mai_mari(suma_data_cautare)

            elif optiune_submeniu_cautare == 'b':
                """Tipareste toate cheltuielile efectuate inainte de o zi si mai mici decat o suma"""



            elif optiune_submeniu_cautare == 'c':
                """Tipareste toate cheltuielile de un anumit tip"""

                tipul_dat = input("Introdu tipul cheltuielii:")

                tipul_dat = validare_tip_cheltuiala(tipul_dat)

                cautare_cheltuieli_tipul_dat(tipul_dat)


            afisare_meniu_cautare()

            optiune_submeniu_cautare = input("Introdu una dintre optiuni (a,b,c,d):")


    elif option == 5:
        """Filtreaza cheltuielile"""

        afisare_meniu_filtrare()

        optiune_submeniu_filtrare = input_optiune_submeniu_filtrare()

        optiune_submeniu_filtrare = validare_optiune_submeniu_filtrare(optiune_submeniu_filtrare)

        while optiune_submeniu_filtrare != 'c' :

            if optiune_submeniu_filtrare == 'a':
                """Elimina toate cheltuielile de un anumit tip"""

                tipul_dat = input("Introdu tipul cheltuielii:")

                tipul_dat = validare_tip_cheltuiala(tipul_dat)

                filtreaza_cheltuieli_tipul_dat(tipul_dat)

            elif optiune_submeniu_filtrare == 'b':
                """Elimina toate cheltuielile mai mici de o anumita suma"""

                suma_data_mesaj = "Introdu suma dorita: "
                suma_data = verifica_user_input_int(suma_data_mesaj)
                filtreaza_cheltuieli_mai_mici_decat_suma(suma_data)

            afisare_meniu_filtrare()

            optiune_submeniu_filtrare = input_optiune_submeniu_filtrare()

            optiune_submeniu_filtrare = validare_optiune_submeniu_filtrare(optiune_submeniu_filtrare)








    # Keeping the menu looped
    print()
    menu()
    option = int(input("Continua folosirea FamilyEconManager 1.0.Alege una dintre optiunile de mai sus: "))

print("Lista cheltuieli: ")
print(cheltuieli)