from modules.biudzetas import Biudzetas

biudzetas = Biudzetas()

while True:
    pasirinkimas = int(input("1 - įvesti pajamas\n2 - įvesti išlaidas\n3 - peržiūrėti\n4 - balansas\n0 - išeiti\n"))
    match pasirinkimas:
        case 1:
            suma = abs(float(input("Suma: ")))
            siuntejas = input("Siuntėjas: ")
            info = input("Papildoma informacija: ")
            biudzetas.prideti_pajamu_irasa(suma, siuntejas, info)
        case 2:
            suma = abs(float(input("Suma: ")))
            atsiskaitymo_budas = input("Atsiskaitymo būdas: ")
            isigyta = input("Įsigyta prekė/paslauga: ")
            info = input("Papildoma informacija: ")
            biudzetas.prideti_islaidu_irasa(suma, atsiskaitymo_budas, isigyta, info)
        case 3:
            biudzetas.ataskaita()
        case 4:
            biudzetas.balansas()
        case 0:
            break
