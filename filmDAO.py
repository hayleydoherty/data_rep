import mysql.connector
from mysql.connector import cursor

class FilmDAO:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database= "datarep_project"
        )

    def create(self, film):
        cursor= self.db.cursor()
        sql= "insert into xmasfilms (title, director, year) values (%s, %s, %s)"
        values = [
            film['title'],
            film['director'],
            film['year']
        ]        
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor= self.db.cursor()
        sql= "select * from xmasfilms"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultasDict = self.convertToDict(result)
            returnArray.append(resultasDict)
        return returnArray
 
    def findByID(self, id):
        cursor= self.db.cursor()
        sql= "select * from xmasfilms where id = %s"
        values= [ id ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
            
    def update(self, values):
        cursor = self.db.cursor()
        sql="update xmasfilms set title=%s, director=%s, year= %s where id = %s"
        
        cursor.execute(sql, values)
        self.db.commit()
        #return film
        
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from xmasfilms where id = %s"
        values = [id]
        cursor.execute(sql, values)
        self.db.commit()
        #print("delete done")
        
    def deleteAll(self):
        cursor = self.db.cursor()
        sql="delete from xmasfilms;" 
        cursor.execute(sql)        
        self.db.commit()
        print("delete done")
        
        
    def convertToDict(self, result):
            colnames = ['id', 'title', 'director', 'year']
            film = {}

            if result:
                for i , colname in enumerate(colnames):
                    value = result[i]
                    film[colname] = value
            return film

filmDAO = FilmDAO()

        
        
        
        
        
          #values= [
            #film['title'],
            #film['director'],
            #film['year'],
            #film['id']
        #]      
        
        
        
        
        
        