from stockDAO import stockDAO
import mysql.connector
from mysql.connector import cursor

stock1 = {
    'code': 102852,
    'Product': "Knit Cardigan",
    'amount': 12,
    'price': 2150,
}

stock2 = {
    'code': 115262,
    'Product': "Denim Jacket",
    'amount': 8,
    'price': 33.60
}

stock3 = {
    'code': 103264,
    'Product': "Sweater Dress",
    'amount': 7,
    'price': 14.40
}

stock4 = {
    'code': 115262,
    'Product': "Denim Jacket",
    'amount': 8,
    'price': 23.60
}

#create
first = stockDAO.create(stock1)
#print(returnValue)

'''# find by id
result = stockDAO.findByID(stock1['code'])
print(result)

second = stockDAO.create(stock2)

# get all
returnValue = stockDAO.getAll()
print(returnValue)

#update
returnValue= stockDAO.update(stock4)
print('Update done')

# get all
returnValue = stockDAO.getAll()
print(returnValue)

# delete
returnValue= stockDAO.delete(stock1['code'])
print('Delete done')

# get all
returnValue = stockDAO.getAll()
print(returnValue)

# delete all
#filmDAO.deleteAll()
'''
