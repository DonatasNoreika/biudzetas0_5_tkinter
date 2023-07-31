from modules.irasas import Irasas


class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta, info):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta = isigyta
        self.info = info

    def __str__(self):
        return f"Išlaidos: {self.suma} (atsiskaitymo " \
               f"būdas - {self.atsiskaitymo_budas}, " \
               f"įsigyta - {self.isigyta}, info - {self.info})"
