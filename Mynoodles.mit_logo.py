# Tkinter = Library, um Fenster zu erzeugen
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import pandas as pd

# Globale Variablen
window = tk.Tk()
selected_items = []
tabs = {}

# Hauptfenster einrichten
def initialize_window():
    global window
    window.title("MyNoodles")

    # Bildschirmgröße abrufen
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Fenstergröße auf die Bildschirmgröße setzen
    window.geometry(f"{screen_width}x{screen_height}")

    window.configure(bg="darkorange")
    create_header()
    create_sidebars()
    create_tabs()
    create_sidebar_buttons()

    window.mainloop()

# Header mit Logo
def create_header():
    frame = tk.Frame(window, bg="darkred", height=50)
    frame.pack(fill="x")

    icon_path = "Logo_rot.png"
    
    # Bild öffnen und die Größe anpassen
    icon_image = Image.open(icon_path)
    icon_image = icon_image.resize((80, 80))
    
    # Bild laden
    icon_photo = ImageTk.PhotoImage(icon_image)

    # Label mit dem Bild erstellen
    icon_label = tk.Label(frame, image=icon_photo, bd=0, border=False)
    icon_label.pack(side="top", padx=10, pady=15)

    # Fenster-Icon setzen
    window.iconphoto(True, icon_photo)
    
    # Bild speichern (Ohne diese Zeile kommt es zu Anzeigefehlern)
    icon_label.image = icon_photo 

# Seitenleisten einrichten
def create_sidebars():
    global category_frame, cup_frame

    # Linke Sidebar
    category_frame = tk.Frame(window, bg="darkorange", width=460)  # Breite 
    category_frame.pack(side="left", fill="y", padx=10)
    category_frame.pack_propagate(False)  # Verhindert, dass sich die Größe automatisch an den Inhalt anpasst

    #Pandabild einfügen
    panda_image = ImageTk.PhotoImage(Image.open("panda.png").resize((190, 210)))
    panda_label = tk.Label(category_frame, image=panda_image, bg="darkorange")
    panda_label.place(relwidth=1, relheight=1.4)

    #Pandabild speichern
    panda_label.image = panda_image
    

    # Rechte Sidebar
    cup_frame = tk.Frame(window, bg="darkorange", width=450)
    cup_frame.pack(side="right", fill="both", expand=True)

    # Cup Hintergrundbild einfügen
    background_image = ImageTk.PhotoImage(Image.open("MyCup.png").resize((700, 450)))  
    background_label = tk.Label(cup_frame, image=background_image, bg="darkorange")
    background_label.place(relwidth=1, relheight=1.3)
    
    # Bild speichern (Ohne diese Zeile kommt es zu Anzeigefehlern)
    background_label.image = background_image

# Tabs einrichten
def create_tabs():
    global tabs, notebook
    
    # Stil erstellen, um die Tab-Überschriften zu verstecken
    style = ttk.Style()
    style.configure("TNotebook", tabposition="none")  # Tab-Überschriften verstecken

    # Das Notebook-Widget erstellen
    notebook = ttk.Notebook(window, style="TNotebook")

    # Basis Tab
    tabs[1] = create_tab(
        {"Weizennudeln": "Weizennudeln", "Reisbandnudeln": "Reisbandnudeln",
         "Glasnudeln": "Glasnudeln", "Vollkornnudeln": "Vollkornnudeln"}, 5)

    # Protein Tab
    tabs[2] = create_tab(
        {"Hähnchen": "Hähnchen",
         "Rind": "Rind", "Schwein": "Schwein", "Pute": "Pute",
         "Shrimps": "Shrimps", "Fishcake": "Fishcake", "Lachs": "Lachs",
         "Tofu": "Tofu"}, 5)

    # Gemüse Tab
    tabs[3] = create_tab(
        {"Mais": "Mais", "Lauchzwiebeln": "Lauchzwiebeln", "Karotten": "Karotten",
         "Shitake": "Shitake", "Morcheln": "Morcheln", "Algen (Nori)": "Algen (Nori)", 
         "Kohl": "Kohl", "Grüne Bohnen": "Grüne Bohnen"}, 5)

    # Brühe Tab
    tabs[4] = create_tab(
        {"Misobrühe": "Misobrühe", "Tom Yum": "Tom Yum", "Gemüsebrühe": "Gemüsebrühe", 
         "Pho Brühe": "Pho Brühe", "Thai Curry": "Thai Curry", "Süß-Sauer": "Süß-Sauer", 
         "Sesambrühe": "Sesambrühe"}, 5)

    # Tabs zum Notebook hinzufügen 
    for tab_id, tab_content in tabs.items():
        notebook.add(tab_content)  
    
    # Das Notebook in das Fenster einfügen 
    notebook.pack(fill="both", expand=True)

# Generische Tab-Erstellung
def create_tab(items, height):
    tab = tk.Frame(window, bg="darkorange")
    
    # Canvas für das Scrollen erstellen
    canvas = tk.Canvas(tab, width=800, bg="darkred")
    canvas.pack(side=tk.LEFT, fill="both", expand=True)
    
    # Vertikalen Scrollbalken für das Canvas erstellen
    scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill="y")
    
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Einen Frame innerhalb des Canvas erstellen, um die Buttons zu halten
    button_frame = tk.Frame(canvas, bg="darkred")
    canvas.create_window((0, 0), window=button_frame, anchor="nw")

    # Buttons zum Frame hinzufügen
    for text, value in items.items():
        tk.Button(button_frame, font=("Verdana", 11, "bold"), bg="white", text=text, width=80, height=height, command=lambda v=value: add_to_list(v)).pack(fill="x", padx=5, pady=5)

    # Die Scrollregion des Canvas aktualisieren
    button_frame.update_idletasks()  # Nach dem Platzieren aller Widgets aktualisieren
    canvas.config(scrollregion=canvas.bbox("all"))
    
    return tab

# Sidebar-Buttons erstellen
def create_sidebar_buttons():
    tk.Button(category_frame, text="Basis",font=("Verdana", 12, "bold"), bg="white", command=lambda: show_tab_content(1), width=8, height=4).pack(fill="x", padx=5, pady=5)
    tk.Button(category_frame, text="Protein", font=("Verdana", 12, "bold"), bg="white", command=lambda: show_tab_content(2), width=8, height=4).pack(fill="x", padx=5, pady=5)
    tk.Button(category_frame, text="Gemüse", font=("Verdana", 12, "bold"), bg="white", command=lambda: show_tab_content(3), width=8, height=4).pack(fill="x", padx=5, pady=5)
    tk.Button(category_frame, text="Brühe", font=("Verdana", 12, "bold"), bg="white", command=lambda: show_tab_content(4), width=8, height=4).pack(fill="x", padx=5, pady=5)
    tk.Button(category_frame, text="Reset", font=("Verdana", 12, "bold"), bg="white", command=reset_selected_items, width=8, height=4).pack(fill="x", padx=5, pady=5)

#Liste der ausgewählten items zurücksetzten
def reset_selected_items():
    global selected_items
    selected_items.clear()
    update_display()

# Den Inhalt des ausgewählten Tabs anzeigen
def show_tab_content(tab_num):
    global current_tab
    current_tab = tab_num
    notebook.select(tabs[tab_num])

# Ein Element zur Liste hinzufügen
def add_to_list(item):
    global selected_items, current_tab

    # Überprüfe, wie viele Items bereits für den aktuellen Tab ausgewählt wurden
    current_tab_items = [i for i in selected_items if i in tab_items[current_tab]]

    # Begrenzung prüfen
    if len(current_tab_items) >= max_selections_per_tab[current_tab]:
        print(f"Maximale Auswahl von {max_selections_per_tab[current_tab]} für diesen Tab erreicht.")
        return

    # Item hinzufügen, falls es noch nicht ausgewählt ist
    if item not in selected_items:
        selected_items.append(item)

    # Anzeige aktualisieren
    update_display()
# Die Anzeige der ausgewählten Elemente aktualisieren
def update_display():
    for widget in cup_frame.winfo_children():
        if widget is not cup_frame.winfo_children()[0]:
            widget.destroy()

    total_price = 0
    total_kcal = 0

    for item in selected_items:
        item_data = ingredients_data.loc[item]
        price = item_data['Preis angebotene Menge']  # Annahme: Spalte heißt 'Preis'
        kcal = item_data['Energie']  # Annahme: Spalte heißt 'Kalorien'

        total_price += price
        total_kcal += kcal

        item_label = tk.Label(cup_frame, text=f"{item} - Preis: {round(price,2)}€, Kalorien: {round(kcal,2)}kcal", font=("Verdana", 12))
        item_label.pack(pady=5)

    summary_label = tk.Label(cup_frame, text=f"Gesamt: Preis: {round(total_price,2)}€, Kalorien: {total_kcal}kcal", font=("Verdana", 15, "bold"))
    summary_label.pack(pady=30, side="bottom")


#Excel Daten laden
ingredients_data = pd.read_excel("Datensatz.xlsx", header=0)
ingredients_data.set_index("Zutat", inplace=True)

#Maximale Auswahl pro Tab
max_selections_per_tab = {
    1: 1,  # Maximal 1 Auswahlmöglichkeiten im Basis-Tab
    2: 1,  # Maximal 1 Auswahlmöglichkeiten im Protein-Tab
    3: 2,  # Maximal 4 Auswahlmöglichkeiten im Gemüse-Tab
    4: 1   # Maximal 1 Auswahlmöglichkeit im Brühe-Tab
}

#Items dem Tab zuordnen 
tab_items = {
    1: ["Weizennudeln", "Reisbandnudeln", "Glasnudeln", "Vollkornnudeln"],
    2: ["Hähnchen", "Rind", "Schwein", "Shrimps", "Fishcake", "Tofu", "Pute", "Lachs"],
    3: ["Mais", "Lauchzwiebeln", "Karotten", "Shitake", "Morcheln", "Kohl", "Grüne Bohnen", "Algen (Nori)"],
    4: ["Misobrühe", "Tom Yum", "Gemüsebrühe", "Pho Brühe", "Thai Curry", "Süß-Sauer", "Sesambrühe"]
}
# Aktueller Tab 
current_tab = 1  

#Anwendung starten
initialize_window()