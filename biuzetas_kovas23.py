# biuzetas

import pickle

class Irasas:
    def __init__(self, suma):
        self.suma = suma

    def __str__(self):
        return f"{self.suma}"


class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, info):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.info = info

    def __str__(self):
        return f"Pajamos: {self.suma}, siuntėjas - {self.siuntejas}, info: {self.info}"


class IslaiduIrasas(Irasas):
    def __init__(self, suma, budas, isigyta):
        super().__init__(suma)
        self.budas = budas
        self.isigyta = isigyta

    def __str__(self):
        return f"Išlaidos: {self.suma}, mokėjimo būdas - {self.budas}, įsigyta prekė/paslauga: {self.isigyta}"


class Biudzetas:
    def __init__(self):
        self.zurnalas = self._gauti_zurnala()

    def _gauti_zurnala(self):
        try:
            with open('zurnalas.pkl', 'rb') as file:
                zurnalas = pickle.load(file)
        except:
            zurnalas = []
        return zurnalas

    def _irasyti_zurnala(self):
        with open('zurnalas.pkl', 'wb') as file:
            pickle.dump(self.zurnalas, file)

    def prideti_pajamu_irasa(self, suma, siuntejas, info):
        irasas = PajamuIrasas(suma, siuntejas, info)
        self.zurnalas.append(irasas)
        self._irasyti_zurnala()

    def prideti_islaidu_irasa(self, suma, budas, isigyta):
        irasas = IslaiduIrasas(suma, budas, isigyta)
        self.zurnalas.append(irasas)
        self._irasyti_zurnala()

    def gauti_balansa(self):
        suma = 0
        for irasas in self.zurnalas:
            if type(irasas) is PajamuIrasas:
                suma += irasas.suma
            if type(irasas) is IslaiduIrasas:
                suma -= irasas.suma
        return suma

    def parodyti_ataskaita(self):
        for irasas in self.zurnalas:
            print(irasas)


biudzetas = Biudzetas()

while True:
    pasirinkimas = int(input("1 - pridėti pajamas\n2 - pridėti išlaidas\n3 - balansas\n4 - ataskaita\n0 - išeiti\n"))
    match pasirinkimas:
        case 1:
            suma = float(input("Suma: "))
            siuntejas = input("Siuntėjas: ")
            info = input("Papildoma informacija: ")
            biudzetas.prideti_pajamu_irasa(suma, siuntejas, info)
        case 2:
            suma = float(input("Suma: "))
            budas = input("Mokėjimo būdas: ")
            isigyta = input("Įsigyta prekė/paslauga: ")
            biudzetas.prideti_islaidu_irasa(suma, budas, isigyta)
        case 3:
            print(biudzetas.gauti_balansa())
        case 4:
            biudzetas.parodyti_ataskaita()
        case 0:
            print("Viso gero")
            break