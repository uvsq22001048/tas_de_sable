###########################
# groupe BI TD3
# Ceylia DUPIN
# Laetitia SALE
# Louis REBÊCHE
# Lou GUEVEL
###########################

##########
# Importation de la librairie
import tkinter as tk
from tkinter import * 
"j'ai du utiliser * car je n'arrivai pas a importer button"
###############
# programme principale
racine = tk.Tk()
racine.title("tas de sable")
canvas = tk.Canvas(racine, width=600, height=600)
canvas.grid(column=0, row=0)

# creation d'un bouton
bt_blue = Button(racine, text="configuration")
bt_blue_w = canvas.create_window(40, 20, window=bt_blue)
 
 


# boucle principale
racine.mainloop()
