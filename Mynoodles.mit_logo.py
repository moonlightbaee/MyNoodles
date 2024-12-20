#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 21:05:31 2024

@author: moonlightbae
"""

import tkinter as tk
from tkinter import ttk

# Willkommen zum Test1
# Bilder hinzufügen
from PIL import Image, ImageTk

# Funktion, die beim Drücken eines Buttons ausgeführt wird
def show_tab_content(tab_num):


    # Inhalt der Tabs werden ausgeblendet
    for tab in [tab1, tab2, tab3, tab4]:
        tab.pack_forget()
        
        
        
    # gewählte Tabs anzeigen
    

    if tab_num == 1:
        tab1.pack(fill="both", expand=True)  #fill=both: Höhe und Breite(ganzer Platz) werden gefüllt
    elif tab_num == 2:
        tab2.pack(fill="both",  expand=True)  #expand=True: wenn Fenster vergrößert wird, wird Tab auch vergrößert
    elif tab_num == 3:                       #bei False: Tab bleibt unverändert und passt sich nicht an
        tab3.pack(fill="both", expand=True) 
    elif tab_num == 4:
        tab4.pack(fill="both", expand = True)




# Liste, die die ausgewählten Produkte speichert
selected_items = []

# add to List
def add_to_list(item):
    # Item zur Liste hinzufügen, falls es noch nicht vorhanden ist
    if item not in selected_items:
        selected_items.append(item)
    update_display()

# ausgewählte Items im rechten Frame 
def update_display():
    # Lösche den aktuellen Inhalt des rechten Frames
    for widget in cup_frame.winfo_children():
        if widget is not cup_label: # Label bleibt im Frame
            widget.destroy()
            

    # Zeige jedes ausgewählte Item im rechten Frame an
    if selected_items:
        for item in selected_items:
            item_label = tk.Label(cup_frame, text=item)
            item_label.pack(pady=5)




# Hauptfenster
window = tk.Tk()
window.title("MyNoodles")
window.geometry("1500x900")
window.configure(bg = "darkorange") # Hintergrund

# Frame oben, wo Logo ist
frame = tk.Frame(window, bg = "white", height = 40)
frame.pack(fill = "x") #streckung

# Logo
icon_path = "/Users/moonlightbae/Documents/MyNoodles/Logo_rot.png" #path zum Logo
icon_image = Image.open(icon_path)
icon_image = icon_image.resize((64, 64))
icon_photo = ImageTk.PhotoImage(icon_image) #Bild wird in passendes Format umgewandelt


icon_label = tk.Label(frame, image = icon_photo, bd = 0, highlightthickness=0) #Label im Frame, damit Bild angezeigt werden kann
icon_label.pack(side = "top", padx = 10, pady = 5) #x,y: Abstand zum Rahmen


window.iconphoto(True, icon_photo) # windows: Logo in Titelleiste #macOS: Im Dock/ Icon



# Sidebar links
category_frame = tk.Frame(window, bg = "darkorange")
category_label = tk.Label(category_frame, text = "<3", bd = 0, highlightthickness=0)
category_label.pack()
category_frame.pack(side="left", fill="y", padx=10)


# sidebar rechts (cup)
cup_frame = tk.Frame(window, bg = "firebrick")
cup_label = tk.Label(cup_frame, text = "Dein Cup", bd = 0, highlightthickness=0)
cup_label.pack()
cup_frame.pack(side="right", fill="both", expand = True)

# cup vorschau
cup= tk.Frame(window)
# Foto

"""
#Bild

new_path = "path einfügen"
image = Image.open(new_path)
image = image.resize((100, 100))
photo = ImageTk.PhotoImage(image)

import os
new_path = os.path.join(os.getcwd(), "path einfügen")
image.save(new_path, format="JPEG")


label = tk.Label(window, image = photo)
label_image = photo
label_image.image = photo
label.pack(pady=20)"""

# Basis
tab1 = tk.Frame(window, bg ="darkorange")


label = tk.Label(text = "Bitte wähle", bd = 0, highlightthickness=0)
label.pack()

basis_buttons = {"Weizennudeln": lambda: add_to_list("Weizennudeln"),
                 "Reisbandnudeln": lambda: add_to_list("Reisbandnudeln"),
                 "Glasnudeln": lambda: add_to_list("Glasnudeln"),
                 "Vollkornnudeln": lambda: add_to_list("Vollkornnudeln"),
                 "Glutenfreie Nudeln": lambda: add_to_list("Glutenfreie Nudeln")}

for text, command in basis_buttons.items():
    tk.Button(tab1, text = text, width = 90, height = 8, command = command).pack(fill = "x", padx = 5, pady = 5)


# Bild mit Pillow laden
image = Image.open("/Users/moonlightbae/Downloads/pngtree-noodles-food-noodles-dry-picture-image_13176534.png")
photo = ImageTk.PhotoImage(image)

# Button mit Text und Bild
button = tk.Button(tab4, text="Klick mich", image=photo, compound="left")
button.pack()


# Protein
tab2 = tk.Frame(window, bg="darkorange")

protein_buttons = {"Hühnerfleisch": lambda: add_to_list("Huhn"),
                   "Entenfleisch": lambda: add_to_list("Entenfleisch"),
                   "Rindfleisch": lambda: add_to_list("Rindfleisch"),
                   "Schweinefleisch": lambda: add_to_list("Schweinefleisch"),
                   "Schrimps": lambda: add_to_list("Schrimps"),
                   "Fish Cake": lambda: add_to_list("Fish Cake"),
                   "Surimi": lambda: add_to_list("Surimi"),
                   "Tintenfisch": lambda: add_to_list("Tintenfisch"),
                   "Tofu": lambda: add_to_list("Tofu")}

for text, command in protein_buttons.items():
    tk.Button(tab2, text = text, width = 90, height = 5, command = command).pack(fill = "x", padx = 5, pady = 5)
    

# Gemüse
tab3 = tk.Frame(window, bg ="darkorange")

veggie_buttons = {"Mais": lambda: add_to_list("Mais"),
                  "Lauch": lambda: add_to_list("Lauch"),
                  "Karotten": lambda: add_to_list("Karotten"),
                  "Shitake Pilze": lambda: add_to_list("Shitake Pilze"),
                  "Morcheln": lambda: add_to_list("Morcheln"),
                  "Kohl": lambda : add_to_list("Kohl")}

for text, command in veggie_buttons.items():
    tk.Button(tab3, text = text, width = 90, height = 6, command = command).pack(fill = "x", padx = 5, pady = 5)


# Flavour
tab4 = tk.Frame(window, bg="darkorange")

flavour_buttons = {"Miso": lambda: add_to_list("Miso"),
                   "Tom Yum": lambda: add_to_list("Tom Yum")}

for text, command in flavour_buttons.items():
    tk.Button(tab4, text = text, width = 90, height = 8, command = command).pack(fill = "x", padx = 5, pady = 5)






# Kalorien- und Preisberechnung (Peer)
# Nährwerte (Linus)
# Preise (Linus) 
 


# Sidebar Tabs untereinander
tab1_button = tk.Button(category_frame, text="Basis", command=lambda: show_tab_content(1), width=8, height=3)
tab1_button.config(bg="blue")  # Hex-Farbcode
tab1_button.pack(fill="x", padx=5, pady=5)                          #command: welche Fkt soll ausgeführt werden
                  #padx, pady: Abstand oben unten                   #lambda:  Funktion, die show_tab_content(x) aufruft(bei Klick)
                                   
tab2_button = tk.Button(category_frame, text="Protein", bg = "beige", command=lambda: show_tab_content(2), width=8, height=3)
tab2_button.pack(fill="x", padx=5, pady=5)

tab3_button = tk.Button(category_frame, text="Gemüse", command=lambda: show_tab_content(3), width=8, height=3)
tab3_button.pack(fill="x", padx=5, pady=5)

tab4_button = tk.Button(category_frame, text = "Brühe", command = lambda: show_tab_content(4), width=8, height=3)
tab4_button.pack(fill ="x", padx=5, pady=5) 


# Anwendung starten
window.mainloop()
