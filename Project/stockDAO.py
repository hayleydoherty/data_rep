import mysql.connector
from mysql.connector import cursor

class stockDAO:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database= "shopstock"
        )

    def create(self, stock):
        cursor= self.db.cursor()
        sql= "insert into shopStock (code, Product, amount, price) values (%s, %s, %s, %s)"
        values = [
            stock['code'],
            stock['Product'],
            stock['amount'],
            stock['price']
        ]        
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid
        

    def getAll(self):
        cursor= self.db.cursor()
        sql= "select * from shopStock"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultasDict = self.convertToDict(result)
            returnArray.append(resultasDict)
        return returnArray
 
    def findByID(self, code):
        cursor= self.db.cursor()
        sql= "select * from shopStock where code = %s"
        values= [ code ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
            
    def update(self, stock):
        cursor = self.db.cursor()
        sql="update shopStock set Product=%s, amount=%s, price= %s where code = %s"
        values = [
            stock['Product'],
            stock['amount'],
            stock['price'],
            stock['code']
        ]     
        cursor.execute(sql, values)
        self.db.commit()
        return stock
        
    def delete(self, code):
        cursor = self.db.cursor()
        sql="delete from shopStock where code = %s"
        values = [code]
        cursor.execute(sql, values)
        self.db.commit()
        #print("delete done")
        
    def deleteAll(self):
        cursor = self.db.cursor()
        sql="delete from shopStock;" 
        cursor.execute(sql)        
        self.db.commit()
        print("delete done")
        
        
    def convertToDict(self, result):
            colnames = ['code', 'Product', 'amount', 'price']
            stock = {}

            if result:
                for i , colname in enumerate(colnames):
                    value = result[i]
                    stock[colname] = value
            return stock

stockDAO = stockDAO()

        
        
        
        
        
           
        
        
        
        
        
        