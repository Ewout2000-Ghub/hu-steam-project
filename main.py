import json
import tkinter as tk
from sort import *
from statistiek import *


# Laad het json bestand in
def laad_json():
    f = open('steam.json')
    data = json.load(f)
    f.close()

    return data


# Laad een tkinter GUI in
root = tk.Tk()

json = laad_json()
merge_sort(json, 'price')
label = tk.Label(text=json[0]['name'])
label.pack()

root.mainloop()
