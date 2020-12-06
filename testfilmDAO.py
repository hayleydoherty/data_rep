from filmDAO import filmDAO
import mysql.connector
from mysql.connector import cursor

film1 = {

    'title': 'Elf',
    'director': 'Jon Favreau',
    'year': 2003
}

film2 = {

    'title': 'Home Alone',
    'director': 'Chris Columbus',
    'year': 1990
}

film3 = {

    'title': 'Die Hard',
    'director': 'John McTiernan',
    'year': 1988
}

#create
first = filmDAO.create(film1)
#print(returnValue)

# find by id
result = filmDAO.findByID(first)
print(result)

second = filmDAO.create(film2)

# get all
returnValue = filmDAO.getAll()
print(returnValue)

#update
returnValue= filmDAO.update(id)
print('Update done')

# get all
returnValue = filmDAO.getAll()
print(returnValue)

# delete
returnValue= filmDAO.delete(second)
print('Delete done')

# get all
returnValue = filmDAO.getAll()
print(returnValue)

# delete all
#filmDAO.deleteAll()

