from models.irasas import Irasas

class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymas, isigyta_preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymas = atsiskaitymas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga

    def __repr__(self):
        return (f"Išlaidos: {self.suma} Eur., atsiskaitymo būdas: {self.atsiskaitymas}, "
                f"įsigyta prekė/paslauga: {self.isigyta_preke_paslauga}.\n")