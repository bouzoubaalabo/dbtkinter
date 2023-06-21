def make_ref_analyse_primary_key():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="Codemy",
    )
    
    my_cursor = mydb.cursor()

    # Supprimer l'ancienne clé primaire (si elle existe)
    try:
        my_cursor.execute("ALTER TABLE analyses DROP PRIMARY KEY")
    except mysql.connector.Error as err:
        print("Erreur lors de la suppression de l'ancienne clé primaire: {}".format(err))
    
    # Définir ref_analyse comme nouvelle clé primaire
    try:
        my_cursor.execute("ALTER TABLE analyses ADD PRIMARY KEY (ref_analyse)")
        print("ref_analyse a été défini comme clé primaire avec succès")
    except mysql.connector.Error as err:
        print("Erreur lors de la définition de ref_analyse comme clé primaire: {}".format(err))
    
    mydb.commit()
    mydb.close()

"""    
    print("About to call get_ref_analyse_list()") 
    ref_analyse_list = get_ref_analyse_list()
    print("ref_analyse récupérée") 
    if ref_analyse == "":
        messagebox.showwarning("Erreur", "Veuillez entrer une référence d'analyse")
        print("ref_analyse vide")
    elif ref_analyse in ref_analyse_list:
        messagebox.showwarning("Erreur", "Cette référence existe déjà")
        print("ref_analyse existe déjà")
    else:
"""



"""
def add_analyse():
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
    
#tester si ref_analyse existe déjà, si oui, message (cette référence existe déjà, voulez-vous enregistrer les modifications ? Oui/Non)
# , si non, ajouter les données dans la base de données)
    ref_analyse_list = get_ref_analyse_list()
    results = my_cursor.fetchall() 
    if ref_analyse == "":
        messagebox.showwarning("Erreur", "Veuillez entrer une référence d'analyse")
    #si ref_analyse existe déjà, message (cette référence existe déjà, voulez-vous enregistrer les modifications ? Oui/Non)
    elif ref_analyse in ref_analyse_list:
        my_cursor = mydb.cursor(buffered=True)
        messagebox.showwarning("Erreur", "Cette référence existe déjà")

    else:
        my_cursor.execute("INSERT INTO analyses (ref_analyse, type_analyse, date_prelevement, date_reception, renseignements_cliniques, macroscopie, pec, validation, sorti, prix, total_encaissement, remise, reste)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (ref_analyse, type_analyse, date_prelevement, date_reception, renseignements_cliniques, macroscopie, pec, validation, sorti, prix, total_encaissement, remise, reste))
        results = my_cursor.fetchall() 
        mydb.commit()  
"""







 
        

    

    




























"""
# Affichage des informations sur les champs
my_cursor =mydb.cursor()
my_cursor.execute("DESCRIBE analyses")
columns = my_cursor.fetchall()
for column in columns:
    print("Nom du champ:", column[0])
    print("Type de données:", column[1])
    print("Clé primaire:", "Oui" if column[3] == "PRI" else "Non")
    print("Auto-incrémentation:", "Oui" if column[5] == "auto_increment" else "Non")
    print("--------------------------------------")

def save(self, *args, **kwargs):
    if not self.pk:
        today = timezone.now().strftime("%d%m%Y")
        last_pvt = Prelevement.objects.filter(code_pvt__startswith=today).order_by('-code_pvt').first()
        if last_pvt:
            next_pvt_number = int(last_pvt.code_pvt[-3:]) + 1
        else:
            next_pvt_number = 1
        self.code_pvt = f"{today}{next_pvt_number:03}"
    super(Prelevement, self).save(*args, **kwargs)
"""



