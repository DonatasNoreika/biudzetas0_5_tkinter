import tkinter as tk
from modules.biudzetas import Biudzetas

biudzetas = Biudzetas()

def gui_ivesti_pajamas():
    suma = float(pajamos_suma_entry.get())
    siuntejas = pajamos_siuntejas_entry.get()
    info = pajamos_info_entry.get()
    biudzetas.prideti_pajamu_irasa(suma, siuntejas, info)
    pajamos_suma_entry.delete(0, tk.END)
    pajamos_siuntejas_entry.delete(0, tk.END)
    pajamos_info_entry.delete(0, tk.END)
    pajamos_suma_entry.focus()
    zurnalas_listbox.delete(0, tk.END)
    zurnalas_listbox.insert(tk.END, *biudzetas.zurnalas)


def gui_ivesti_islaidas():
    suma = float(islaidos_suma_entry.get())
    atsiskaitymo_budas = islaidos_atsiskaitymo_budas_entry.get()
    isigyta = islaidos_isigyta_entry.get()
    info = islaidos_info_entry.get()
    biudzetas.prideti_islaidu_irasa(suma, atsiskaitymo_budas, isigyta, info)
    islaidos_suma_entry.delete(0, tk.END)
    islaidos_isigyta_entry.delete(0, tk.END)
    islaidos_atsiskaitymo_budas_entry.delete(0, tk.END)
    islaidos_info_entry.delete(0, tk.END)
    islaidos_suma_entry.focus()
    zurnalas_listbox.delete(0, tk.END)
    zurnalas_listbox.insert(tk.END, *biudzetas.zurnalas)

# def istrinti():
#     indeksas = asmenys_listbox.curselection()[0]
#     del asmenys[indeksas]
#     irasyti_pkl()
#     asmenys_listbox.delete(0, tk.END)
#     asmenys_listbox.insert(tk.END, *asmenys)


window = tk.Tk()
window.geometry("180x400")

# pajamų forma:
pajamos_label = tk.Label(window, text="Įveskite pajamas:")
pajamos_suma_label = tk.Label(window, text="Suma")
pajamos_suma_entry = tk.Entry(window)
pajamos_siuntejas_label = tk.Label(window, text="Siuntėjas")
pajamos_siuntejas_entry = tk.Entry(window)
pajamos_info_label = tk.Label(window, text="Info")
pajamos_info_entry = tk.Entry(window)
pajamos_ivedimas_button = tk.Button(window, text="Įvesti pajamas", command=gui_ivesti_pajamas)

# pajamų forma:
islaidos_label = tk.Label(window, text="Įveskite išlaidas:")
islaidos_suma_label = tk.Label(window, text="Suma")
islaidos_suma_entry = tk.Entry(window)
islaidos_atsiskaitymo_budas_label = tk.Label(window, text="Atsk. būdas")
islaidos_atsiskaitymo_budas_entry = tk.Entry(window)
islaidos_isigyta_label = tk.Label(window, text="Įsigyta")
islaidos_isigyta_entry = tk.Entry(window)
islaidos_info_label = tk.Label(window, text="Info")
islaidos_info_entry = tk.Entry(window)
islaidos_ivedimas_button = tk.Button(window, text="Įvesti išlaidas", command=gui_ivesti_islaidas)

# trinti_button = tk.Button(window, text="Ištrinti", command=istrinti)
zurnalas_listbox = tk.Listbox(window)
zurnalas_listbox.insert(tk.END, *biudzetas.zurnalas)

# Pajamų forma grid:
pajamos_label.grid(row=0, columnspan=2)
pajamos_suma_label.grid(row=1, column=0)
pajamos_suma_entry.grid(row=1, column=1)
pajamos_siuntejas_label.grid(row=2, column=0)
pajamos_siuntejas_entry.grid(row=2, column=1)
pajamos_info_label.grid(row=3, column=0)
pajamos_info_entry.grid(row=3, column=1)
pajamos_ivedimas_button.grid(row=4, columnspan=2)

# Išlaidų forma grid:
islaidos_label.grid(row=5, columnspan=2)
islaidos_suma_label.grid(row=6, column=0)
islaidos_suma_entry.grid(row=6, column=1)
islaidos_atsiskaitymo_budas_label.grid(row=7, column=0)
islaidos_atsiskaitymo_budas_entry.grid(row=7, column=1)
islaidos_isigyta_label.grid(row=8, column=0)
islaidos_isigyta_entry.grid(row=8, column=1)
islaidos_info_label.grid(row=9, column=0)
islaidos_info_entry.grid(row=9, column=1)
islaidos_ivedimas_button.grid(row=10, columnspan=2)

zurnalas_listbox.grid(row=11, columnspan=2)

window.mainloop()
