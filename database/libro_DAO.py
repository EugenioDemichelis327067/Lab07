from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass
    def get_libri_genere_biblioteca(self,biblioScelta=None,genereScelto=None):
        cnx = DBConnect.get_connection()
        result = []
        parametri = []
        if cnx is None:
            return []
        cursor = cnx.cursor(dictionary=True)
        query = " SELECT DISTINCT * FROM libro WHERE 1=1 "
        if biblioScelta is not None:
            query += " AND id_biblioteca = %s"
            parametri.append(biblioScelta)
        if genereScelto is not None:
            query += " AND genere = %s"
            parametri.append(genereScelto)
        cursor.execute(query, tuple(parametri))
        for r in cursor:
            l = Libro(r["id"], r["titolo"], r["autore"], r["genere"], r["anno_pubblicazione"], r["id_biblioteca"])
            result.append(l)
        cursor.close()
        cnx.close()
        return result

    def get_generi(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            return []
        cursor = cnx.cursor()
        cursor.execute("SELECT DISTINCT genere FROM libro")
        for r in cursor:
            result.append(r[0])
        cursor.close()
        cnx.close()
        return result

"""    
    def get_libri_in_1Biblio(self,valore):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            return []
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT DISTINCT * FROM libro WHERE id_biblioteca = %s",(f"{valore}",))
        for r in cursor:
            l = Libro(r["id"], r["titolo"], r["autore"],r["genere"],r["anno_pubblicazione"], r["id_biblioteca"])
            result.append(l)
        cursor.close()
        cnx.close()
        return result
       
       
    def get_libri_in_biblio(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            return []
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT DISTINCT * FROM libro")
        for r in cursor:
            l = Libro(r["id"], r["titolo"], r["autore"],r["genere"],r["anno_pubblicazione"], r["id_biblioteca"])
            result.append(l)
        cursor.close()
        cnx.close()
        return result

    def get_libri_genere(self,valore):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            return []
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT DISTINCT * FROM libro WHERE genere = %s",(f"{valore}",))
        for r in cursor:
            l = Libro(r["id"], r["titolo"], r["autore"],r["genere"],r["anno_pubblicazione"], r["id_biblioteca"])
            result.append(l)
        cursor.close()
        cnx.close()
        return result
        
        cursor.execute("SELECT DISTINCT * FROM libro WHERE genere = %s and id_biblioteca = %s",(f"{genereScelto}",f"{biblioScelta}"))
        for r in cursor:
            l = Libro(r["id"], r["titolo"], r["autore"],r["genere"],r["anno_pubblicazione"], r["id_biblioteca"])
            result.append(l)
        cursor.close()
        cnx.close()
        return result
    
    """

