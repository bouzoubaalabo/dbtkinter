#créer database
#my_cursor.execute("CREATE DATABASE Codemy")

"""
#Ajouter un champs de liaison avec la table "patients" une fois créée
my_cursor.execute("ALTER TABLE analyses ADD COLUMN id_patient INT, ADD FOREIGN KEY (id_patient) REFERENCES patients(id_patient)")


#Test to see if database was ceated
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)

my_cursor = mydb.cursor()

my_cursor.execute("DROP TABLE IF EXISTS analyses")


my_cursor.execute("CREATE TABLE analyses (id_analyse INT AUTO_INCREMENT PRIMARY KEY,"
                  "type_analyse ENUM('H', 'C', 'MOL'),"
                  "ref_analyse VARCHAR(50),"
                  "date_reception DATE DEFAULT CURRENT_DATE(),"
                  "validation TINYINT(1) CHECK (validation IN (0, 1)))")

# Vérification de l'existence de la table "analyses"
my_cursor.execute("SHOW TABLES")
tables = my_cursor.fetchall()

# Vérification de l'existence de la table "analyses"
if ('analyses',) in tables:
    print("La table 'analyses' a été créée avec succès.")
else:
    print("La table 'analyses' n'a pas été trouvée.")


# Affichage des informations sur les champs

my_cursor.execute("DESCRIBE analyses")
columns = my_cursor.fetchall()
for column in columns:
    print("Nom du champ:", column[0])
    print("Type de données:", column[1])
    print("Clé primaire:", "Oui" if column[3] == "PRI" else "Non")
    print("Auto-incrémentation:", "Oui" if column[5] == "auto_increment" else "Non")
    print("--------------------------------------")



my_cursor.execute("DROP TABLE analyses")
print("La table 'analyses' a été supprimée avec succès.")
"""