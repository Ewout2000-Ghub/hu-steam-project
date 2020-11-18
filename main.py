import json
import tkinter as tk


# Laad het json bestand in
def laad_json():
    f = open('steam.json')
    data = json.load(f)
    f.close()

    return data


# Sorteer een lijst op basis van een bepaalde key
def sorteer(list, key):
    return sorted(list, key=lambda k: k[key], reverse=True)


# Laad een tkinter GUI in
root = tk.Tk()

label = tk.Label(text=laad_json()[0]['name'])
label.pack()

root.mainloop()
