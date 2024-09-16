from models.islaidu_irasas import IslaiduIrasas
from models.pajamu_irasas import PajamuIrasas

class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def prideti_pajamu_irasa(self):
        suma = abs(float(input("Įveskite sumą (€): ")))
        siuntejas = input("Įveskite siuntėją: ")
        papildoma_info = input("Įveskite papildomą informaciją: ")
        pajamos = PajamuIrasas(suma, siuntejas, papildoma_info)
        self.zurnalas.append(pajamos)

    def prideti_islaidu_irasa(self):
        suma = abs(float(input("Įveskite sumą (€): ")))
        atsiskaitymas = input("Įveskite atsiskaitymo būdą: ")
        pirkinys = input("Įveskite įsigytą prekę/paslaugą: ")
        islaidos = IslaiduIrasas(suma, atsiskaitymas, pirkinys)
        self.zurnalas.append(islaidos)

    def gauti_balansa(self):
        balansas = 0
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                balansas += irasas.suma
            else:
                balansas -= irasas.suma
        print(f"Balansas: {format(balansas, '.2f')}€\n")

    def parodyti_ataskaita(self):
        if not self.zurnalas:
            print("Neįvesta pajamų/išlaidų\n")
        for irasas in self.zurnalas:
            print(irasas)