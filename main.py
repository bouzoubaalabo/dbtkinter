import tkinter as tk
from datetime import date, datetime, timezone
from urllib import response

import mysql.connector
from tkinter import IntVar, StringVar, ttk, messagebox, END

root = tk.Tk()
root.title("bdtkinter")
#root.geometry("400x400")






def get_ref_analyse_list():
    print("Entered get_ref_analyse_list function")  # This will print when the function is called
    my_cursor = mydb.cursor()
    print("Cursor created")  # This will print after the cursor is created

    my_cursor.execute("SELECT ref_analyse FROM analyses")
    print("Query executed")  # This will print after the query is executed

    ref_analyse_list = [row[0] for row in my_cursor.fetchall()]
    print("Fetched all rows")  # This will print after all rows are fetched

    # Ignore any remaining results
    while my_cursor.nextset():
        pass

    print("Passed nextset")  # This will print after passing nextset

    return ref_analyse_list

def column_attributes():
    ref_analyse = ref_entry.get()
    type_analyse = histo_cyto_Entry.get()
    date_prelevement = entryDateP.get()
    date_reception = entryDateR.get()
    renseignements_cliniques = clinique_entry.get()
    macroscopie = macro_entry.get()
    pec = pec_entry.get()
    validation = valid.get()
    sorti = sortie.get()
    prix = prix_entry.get()
    total_encaissement = encaiss_entry.get()
    remise = remise_entry.get()
    reste= reste_entry.get()

def add_analyse():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Codemy",
    )
    my_cursor = mydb.cursor()
    ref_analyse = ref_entry.get()
    type_analyse = histo_cyto_Entry.get()
    date_prelevement = entryDateP.get()
    date_reception = entryDateR.get()
    renseignements_cliniques = clinique_entry.get()
    macroscopie = macro_entry.get()
    pec = pec_entry.get()
    validation = valid.get()
    sorti = sortie.get()
    prix = prix_entry.get()
    total_encaissement = encaiss_entry.get()
    remise = remise_entry.get()
    reste= reste_entry.get()
    
     #insérer les données dans la base de données)
    if ref_analyse == "":
        messagebox.showwarning("Erreur", "Veuillez entrer une référence d'analyse")
    else:
        my_cursor.execute("INSERT INTO analyses (ref_analyse, type_analyse, date_prelevement, date_reception, renseignements_cliniques, macroscopie, pec, validation, sorti, prix, total_encaissement, remise, reste)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (ref_analyse, type_analyse, date_prelevement, date_reception, renseignements_cliniques, macroscopie, pec, validation, sorti, prix, total_encaissement, remise, reste))
        mydb.commit()
       
def delete_analyse():
    print("Entered delete_analyse function")
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Codemy",
    )
    my_cursor =mydb.cursor()

    print("Cursor created")
    # Obtenir ref_analyse de l'entrée
    ref_analyse = ref_entry.get()
    print(ref_analyse)

    # Demander une confirmation à l'utilisateur avant de supprimer l'enregistrement
    if messagebox.askyesno("Confirmation", "Voulez-vous vraiment supprimer cet enregistrement ?"):
        # Supprimer l'enregistrement correspondant dans la base de données
        my_cursor.execute("DELETE FROM analyses WHERE ref_analyse = %s", (ref_analyse,))
        mydb.commit()
        my_cursor.close
        clear_entries
    else:
        return
        
def fetch_data():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Codemy",
    )

    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT ref_analyse, type_analyse FROM analyses")
    
    rows = my_cursor.fetchall()
    mydb.commit()
    my_cursor.close()
    return rows
print("About to run query 2")        

def validate_date(event):
    input_date = entryDateR.get()
    try:
        datetime.strptime(input_date, "%d-%m-%Y")
    except ValueError:
        messagebox.showwarning("Erreur", "Format de date invalide")
        entryDateR.delete(0, END)
        entryDateR.focus_set()

def validate_dateR(event):
    input_date = entryDateR.get()
    try:
        datetime.strptime(input_date, "%d-%m-%Y")
    except ValueError:
        messagebox.showwarning("Erreur", "Format de date invalide")
        entryDateR.delete(0, END)
        entryDateR.focus_set()


def calculate_reste(*args):
#    Calculate the reste.
    prix = prix_var.get()
    encaiss = encaiss_var.get()
    remise = remise_var.get()
    if is_float(prix) and is_float(encaiss) and is_float(remise):
        reste = float(prix) - float(encaiss) - float(remise)
        reste_var.set(str(reste))
        reste_var.set(str(reste))
    else:
        reste_var.set("")

def is_float(input):
#    check if the input is a float.
    try:
        float(input)
        return True
    except ValueError:
#        messagebox.showwarning("Erreur", "Veuillez entrer un nombre")
        return False  # You should return False here.

# Create the validation command
validatecommand = root.register(is_float)

#définir la fonction clear_entries
def clear_entries():
    #effacer les entrées
    ref_entry.delete(0, END)
    histo_cyto_Entry.delete(0, END)
    entryDateP.delete(0, END)
    entryDateR.delete(0, END)
    clinique_entry.delete(0, END)
    macro_entry.delete(0, END)
    pec_entry.delete(0, END)
    valid.set(0)
    sortie.set(0)   
    prix_entry.delete(0, END)
    encaiss_entry.delete(0, END)
    remise_entry.delete(0, END)
    reste_entry.delete(0, END)
    
def populate_table(tree):
    for row in fetch_data():
        tree.insert("", 'end', values=row)

def search_by_ref(Event=None):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Codemy",
    )
    my_cursor = mydb.cursor()
    # Obtenir l'enregistrement d'analyse par ref_analyse
    ref_analyse = search_entry.get()
    my_cursor.execute("SELECT * FROM analyses WHERE ref_analyse = %s", (ref_analyse,))
    row = my_cursor.fetchone()
    # Supprimer les valeurs actuelles des entrées
    clear_entries()
    if row is not None:
        # Mettre à jour chaque entrée avec les valeurs correspondantes de l'enregistrement
        id_entry.config(state=tk.NORMAL)  # Change the state to normal
        id_entry.delete(0, 'end')  # Clear the current value
        id_entry.insert(0, row[0])  # Insert the new value
        id_entry.config(state='readonly')  # Change the state back to readonly

        ref_entry.insert(0, row[2])
        histo_cyto_Entry.insert(0, row[1])
        entryDateP.insert(0, row[3])
        entryDateR.insert(0, row[4])
        clinique_entry.insert(0, row[5])
        macro_entry.insert(0, row[6])
        pec_entry.insert(0, row[7])
        valid.set(row[8])  # mettre à jour la valeur de la variable de contrôle pour le Checkbutton valid
        sortie.set(row[9])  # mettre à jour la valeur de la variable de contrôle pour le Checkbutton sorti
        prix_entry.insert(0, row[10])
        encaiss_entry.insert(0, row[11])
        remise_entry.insert(0, row[12])
        reste_entry.insert(0, row[13])
    else:
        messagebox.showwarning("Erreur", "Aucun enregistrement trouvé avec cette référence d'analyse")
    my_cursor.close()
    
    
   
      

frame_analyses = tk.Frame(root, bg="red")
frame_analyses.grid(row=0, column=1, padx=20, pady=20)
        
tree = ttk.Treeview(frame_analyses, height=10, columns=("ref_analyse", "type_analyse"))
tree['show'] = 'headings'

# Assuming your table has these columns. Modify as necessary.
tree.grid(row=0, column=0, columnspan=3,  padx=20, pady=20)
tree["columns"]=("ref_analyse", "type_analyse")
for col in tree["columns"]:
    tree.column(col, width=100)
    tree.heading(col, text=col)
#Appeler la fonction populate_table
populate_table(tree) 
    


framep =tk.Frame(root)
framep.grid(row=0, column=0, padx=20, pady=20)

search = tk.Frame(framep, bg="#eaeaee")
search.grid(row=0, column=0, padx=20, pady=20)

saisie = tk.Frame(framep, bg="#eaeaea")
saisie.grid(row=1, column=0, padx=20, pady=20)

#saisie = tk.LabelFrame(root, text="Saisie des données")

prix_var = StringVar()
encaiss_var = StringVar()
remise_var = StringVar()
reste_var = StringVar()
check_var = IntVar()

#Eiquettes + Entrys
search_label = tk.Label(search, text="Recherche")   
search_label.grid(row=0, column=0, padx=10, pady=5) 
search_entry = tk.Entry(search)
search_entry.grid(row=0, column=1, padx=20, pady=5)
search_entry.bind("<Return>", search_by_ref)


id_label = tk.Label(saisie, text="Id_analyse")
id_label.grid(row=0, column=0, sticky="e", padx=10, pady=5)
id_entry = tk.Entry(saisie, state="readonly")
id_entry.grid(row=0, column=1, padx=20, pady=5)

ref_label = tk.Label(saisie, text="Ref_analyse",)
ref_label.grid(row=1, column=0, sticky="e", padx=10, pady=5)
ref_entry = tk.Entry(saisie)
ref_entry.grid(row=1, column=1, padx=20, pady=5)

histo_cyto_label = tk.Label(saisie, text="histo ou cyto")
histo_cyto_label.grid(row=2, column=0, sticky="e", padx=10, pady=5)
histo_cyto_Entry = ttk.Combobox(saisie, values=["h", "c"])
histo_cyto_Entry.grid(row=2, column=1, padx=20, pady=5)

date_prelevement_label = tk.Label(saisie, text="Prélevé le :")
date_prelevement_label.grid(row=3, column=0, sticky="e", padx=10, pady=5)
entryDateP = tk.Entry(saisie)
entryDateP.insert(0, date.today().strftime("%d/%m/%y"))
entryDateP.grid(row=3, column=1, padx=10, pady=5)


date_reception_label = tk.Label(saisie, text="Reçu le :")
date_reception_label.grid(row=4, column=0, sticky="e", padx=10, pady=5)
entryDateR = tk.Entry(saisie)
entryDateR.insert(0, date.today().strftime("%d/%m/%y"))
entryDateR.grid(row=4, column=1, padx=10, pady=5)
#entryDateR.bind("<FocusOut>", validate_dateR)

clinique_label = tk.Label(saisie, text="Rennseignements cliniques")
clinique_label.grid(row= 5, column=0, sticky="e", padx=10, pady=5)
clinique_entry = tk.Entry(saisie)
clinique_entry.grid(row=5, column=1, padx=10, pady=5)

macro_label = tk.Label(saisie, text="Macroscopie")
macro_label.grid(row= 6, column=0, sticky="e", padx=10, pady=5)
macro_entry = tk.Entry(saisie)
macro_entry.grid(row= 6, column=1, padx=10, pady=5)

pec_label = tk.Label(saisie, text="Prise en charge par")
pec_label.grid(row= 7, column=0, sticky="e", padx=10, pady=5)
pec_entry = ttk.Combobox(saisie, values=["", "Clinique A", "Clinique B"])
pec_entry.grid(row= 7, column=1, padx=10, pady=5)

valid = IntVar()
valid_label = tk.Label(saisie, text="Validation résultat")
valid_label.grid(row= 8, column=0, sticky="e", padx=10, pady=5)
valid_check = tk.Checkbutton(saisie, text="validé", variable=valid, onvalue=1, offvalue=0)
valid_check.grid(row= 8, column=1, padx=10, pady=5)

sortie = IntVar()
sorti_label = tk.Label(saisie, text="Résultat sorti")
sorti_label.grid(row=9, column=0, sticky="e", padx=10, pady=5)
sorti_check = tk.Checkbutton(saisie, text="sorti", variable=sortie, onvalue=1, offvalue=0)
sorti_check.grid(row= 9, column=1, padx=10, pady=5)

prix_label = tk.Label(saisie, text ="Prix")
prix_label.grid(row=10, column=0, sticky="e", padx=10, pady=5)
prix_entry = tk.Entry(saisie, textvariable=prix_var) 
prix_entry.grid(row=10, column=1, padx=10, pady=5)

encaiss_label = tk.Label(saisie, text="total encaissé")
encaiss_label.grid(row=11, column=0, sticky="e", padx=10, pady=5)
encaiss_entry = tk.Entry(saisie, textvariable=encaiss_var) 
encaiss_entry.grid(row=11, column=1, padx=10, pady=5)

remise_label = tk.Label(saisie, text="remise")
remise_label.grid(row=12, column=0, sticky="e", padx=10, pady=5)
remise_entry = tk.Entry(saisie, textvariable=remise_var)
remise_entry.grid(row=12, column=1, padx=10, pady=5)

reste_label = tk.Label(saisie, text="Reste à payer")
reste_label.grid(row= 13, column=0, sticky="e", padx=10, pady=5)
reste_entry = tk.Entry(saisie, textvariable=reste_var, state="readonly")
reste_entry.grid(row=13, column=1, padx=10, pady=5)

#DEFINIR LA VALEUR DE RESTE A PAYER = PRIX - ENCAISSE - REMISE
prix_var.trace("w", calculate_reste)
encaiss_var.trace("w", calculate_reste)
remise_var.trace("w", calculate_reste)

btn_add_analyse = tk.Button(saisie, text="Ajouter Analyse", command=add_analyse)
btn_add_analyse.grid(row=14, column=0)

btn_delete_analyse = tk.Button(saisie, text="Supprimer Analyse", command=delete_analyse)
btn_delete_analyse.grid(row=14, column=1)

btn_clear = tk.Button(saisie, text="Effacer les entrées", command=clear_entries)
btn_clear.grid(row=14, column=2)


root.mainloop()