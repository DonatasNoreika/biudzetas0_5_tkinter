import pickle
from modules.pajamu_irasas import PajamuIrasas
from modules.islaidu_irasas import IslaiduIrasas


class Biudzetas:
    def __init__(self):
        self.zurnalas = self.nuskaityti_pkl()

    def nuskaityti_pkl(self):
        try:
            with open("zurnalas.pkl", 'rb') as file:
                zurnalas = pickle.load(file)
        except FileNotFoundError:
            zurnalas = []
        return zurnalas

    def irasyti_pkl(self):
        with open("zurnalas.pkl", 'wb') as file:
            pickle.dump(self.zurnalas, file)

    def prideti_pajamu_irasa(self, suma, siuntejas, info):
        irasas = PajamuIrasas(suma, siuntejas, info)
        self.zurnalas.append(irasas)
        self.irasyti_pkl()

    def prideti_islaidu_irasa(self, suma, atsiskaitymo_budas, isigyta, info):
        irasas = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta, info)
        self.zurnalas.append(irasas)
        self.irasyti_pkl()

    def ataskaita(self):
        for irasas in self.zurnalas:
            print(irasas)

    def balansas(self):
        suma = 0
        for irasas in self.zurnalas:
            if type(irasas) is PajamuIrasas:
                suma += irasas.suma
            else:
                suma -= irasas.suma
        print(suma)
        return suma
