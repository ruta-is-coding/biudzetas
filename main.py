from biudzetas import Biudzetas

mano_biudzetas = Biudzetas()

while True:
    while True:
        try:
            veiksmas = int(input("\nPasirinkite veiksmą: \n1-pridėti pajamas (€), \n2-pridėti išlaidas (€), "
                                 "\n3-parodyti balansą, \n4-parodyti biudžeto ataskaitą, "
                                 "\n5-išeiti iš programos\n"))
            break
        except ValueError:
            print("Netinkamas pasirinkimas! Bandykite dar kartą")


    match veiksmas:
        case 1:
            mano_biudzetas.prideti_pajamu_irasa()
        case 2:
            mano_biudzetas.prideti_islaidu_irasa()
        case 3:
            mano_biudzetas.gauti_balansa()
        case 4:
            mano_biudzetas.parodyti_ataskaita()
        case 5:
            print("Viso geriausio :) !")
            break
        case _:
            print("Netinkamas pasirinkimas! Bandykite dar kartą!")
            continue
