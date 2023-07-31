import tkinter as tk
from modules.biudzetas import Biudzetas

biudzetas = Biudzetas()

# def ivesti():
#     vardas = vardas_entry.get()
#     pavarde = pavarde_entry.get()
#     asmuo = Asmuo(vardas, pavarde)
#     asmenys.append(asmuo)
#     irasyti_pkl()
#     asmenys_listbox.delete(0, tk.END)
#     asmenys_listbox.insert(tk.END, *asmenys)
#
#
# def istrinti():
#     indeksas = asmenys_listbox.curselection()[0]
#     del asmenys[indeksas]
#     irasyti_pkl()
#     asmenys_listbox.delete(0, tk.END)
#     asmenys_listbox.insert(tk.END, *asmenys)


window = tk.Tk()
window.geometry("180x250")
pajamos_label = tk.Label(window, text="Įveskite pajamas:")
pajamos_suma_label = tk.Label(window, text="Suma")
pajamos_suma_entry = tk.Entry(window)
pajamos_siuntejas_label = tk.Label(window, text="Siuntėjas")
pajamos_siuntejas_entry = tk.Entry(window)
pajamos_info_label = tk.Label(window, text="Info")
pajamos_info_entry = tk.Entry(window)
pajamos_ivedimas_button = tk.Button(window, text="Įvesti pajamas")

# trinti_button = tk.Button(window, text="Ištrinti", command=istrinti)
zurnalas_listbox = tk.Listbox(window)
zurnalas_listbox.insert(tk.END, *biudzetas.zurnalas)

pajamos_label.grid(row=0, columnspan=2)
pajamos_suma_label.grid(row=1, column=0)
pajamos_suma_entry.grid(row=1, column=1)
pajamos_siuntejas_label.grid(row=2, column=0)
pajamos_siuntejas_entry.grid(row=2, column=1)
pajamos_info_label.grid(row=3, column=0)
pajamos_info_entry.grid(row=3, column=1)
pajamos_ivedimas_button.grid(row=4, columnspan=2)
zurnalas_listbox.grid(row=5, columnspan=2)

# vardas_label.grid(row=0, column=0)
# vardas_entry.grid(row=0, column=1)
# pavarde_label.grid(row=1, column=0)
# pavarde_entry.grid(row=1, column=1)
# ivedimas_button.grid(row=2, column=0)
# trinti_button.grid(row=2, column=1)
# asmenys_listbox.grid(row=3, columnspan=2)

window.mainloop()
