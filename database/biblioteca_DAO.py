from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_biblioteche(self):
        cnx = DBConnect.get_connection()
        result=[]
        if cnx is None:
            return []
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM biblioteca")
        for r in cursor:
            b = Biblioteca(r["id"], r["nome"], r["indirizzo"])
            result.append(b)
        cursor.close()
        cnx.close()
        return result

