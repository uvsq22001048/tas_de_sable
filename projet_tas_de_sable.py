###########################
# groupe BI TD3
# Ceylia DUPIN
# Laetitia SALE
# Louis REBÊCHE
# Lou GUEVEL
###########################

##########
# Importation de la librairie
"from curses import BUTTON2_DOUBLE_CLICKED"
"on ma dit de le garder car on pourrais en avoir besoin plus tard"
import tkinter as tk
from tkinter import * 
from random import *
###############
# programme principale


# début de la création de la configuration aléatoire
HEIGHT = 500
WIDTH = 500
largeur_case = WIDTH // 3
hauteur_case = HEIGHT // 3

tas_de_sable = [[0 for x in range(5)]for y in range(5)]
tas_de_sable [0][0] = ""
tas_de_sable [0][1] = "#"
tas_de_sable [0][2] = "#"
tas_de_sable [0][3] = "#"
tas_de_sable [0][4] = ""

tas_de_sable [1][0] = "#"
tas_de_sable [1][4] ="#"

tas_de_sable [2][0] = "#"
tas_de_sable [2][4] = "#"

tas_de_sable [3][0] ="#"
tas_de_sable [3][4] ="#"

tas_de_sable [4][0] = ""
tas_de_sable [4][1] = "#"
tas_de_sable [4][2] = "#"
tas_de_sable [4][3] = "#"
tas_de_sable [4][4] = ""

"pas terminer"
#canevas
racine = tk.Tk()
racine.title("tas de sable")
canvas = tk.Canvas(racine, width=600, height=600)
canvas.grid(column=0, row=0)
canvas.grid()
for i in range(3):
    for j in range(3):
        if (i+j) % 2 == 0:
            color = "white"
        else:
            color = "white"
        canvas.create_rectangle((i*largeur_case, j*hauteur_case),
                ((i+1)*largeur_case, (j+1)*hauteur_case), fill=color)



# creation d'un bouton
btn = Button(racine, text="configuration")
btn.n = canvas.create_window(550, 300, window=btn)

btn_2 = Button(racine,text= "faire une avalanche" )
btn_2.n = canvas.create_window (550, 400, window= btn_2)
# création d'une variable

"n = random.randint(0,10) "
"a utiliser dans le bouton 2 plus tard "




# boucle principale
racine.mainloop()
