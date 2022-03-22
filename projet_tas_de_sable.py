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
" apparu je ne sais pas comment ,on ma dit de le garder au cas ou"
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

#class tas_de_sable:
tas_de_sable = [[0] * 5 for x in range(5)]
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

#pas terminer"


#canevas
racine = tk.Tk()
racine.title("tas de sable")
canvas = tk.Canvas(racine, width=600, height=600)
canvas.grid(column=0, row=0)
canvas.grid()


# création d'un bouton afin de créer la configuration aléatoire
# lorsque le bouton "configuration" est cliqué 
# le tableau "tas_de_sable" est initialisé avec une de la configuration aléatoire
# 

tas_de_sable [1][1] = randint(0, 4)
tas_de_sable [1][2] = randint(0, 4)
tas_de_sable [1][3] = randint(0, 4)
tas_de_sable [2][1] = randint(0, 4)
tas_de_sable [2][2] = randint(0, 4)
tas_de_sable [2][3] = randint(0, 4)
tas_de_sable [3][1] = randint(0, 4)
tas_de_sable [3][2] = randint(0, 4)
tas_de_sable [3][3] = randint(0, 4)
col = "white"

###
for i in range (1,4):
    for j in range (1, 4):
        if tas_de_sable [i][j] == 1:
            col = "yellow"
        else:
            col = "white"
        canvas.create_rectangle(((j-1)*largeur_case, (i-1)*hauteur_case),
                ((j)*largeur_case, (i)*hauteur_case), fill=col)

btn = Button(racine, text="configuration")
btn.n = canvas.create_window(550, 300, window=btn)

# création d'un bouton pour déclencher l'avalanche
btn_2 = Button(racine,text= "faire une avalanche" )
btn_2.n = canvas.create_window (550, 400, window= btn_2)
# création d'une variable
print(tas_de_sable)





# boucle principale
racine.mainloop()
