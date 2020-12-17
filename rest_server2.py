from flask import Flask, url_for, request, redirect, abort, jsonify
from filmDAO import filmDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')

films =[
    {"id": 1, "title": "Love Actually", "director": "Richard Curtis", "year": 2003},
    {"id": 2, "title": "Elf", "director": "Jon Favreau", "year": 2003},
    {"id": 3, "title": "Home Alone", "director": "Chris Columbus", "year": 1990}]
nextID =4

@app.route('/')
def index():
    return "hello"

# return all
@app.route('/films')
def getAll():
    results = filmDAO.getAll()
    return jsonify(results)
  
# get by id  
@app.route('/films/<int:id>')
def findByID(id):
    '''foundfilms = list(filter (lambda t : t["id"]==id, films))
    if len(foundfilms)== 0:
        return jsonify({}), 204'''
    return jsonify(filmDAO.findByID(id))
  
# create  
@app.route('/films', methods=['POST'])
def create():

    if not request.json:
        abort(400)
        
    film = {
        #"id": request.json["id"],
        "title": request.json["title"],
        "director": request.json["director"],
        "year": request.json["year"] 
    }

    return jsonify(filmDAO.create(film))

# update
@app.route('/films/<int:id>', methods=['PUT'])
def update(id):
    foundFilm = filmDAO.findByID(id)
    if not foundFilm:
        abort(404)
    if not request.json:
        abort(404)
    
    if 'title' in request.json:
        foundFilm['title'] = request.json['title']
    if 'director' in request.json:
        foundFilm['director'] = request.json['director']
    if 'year' in request.json:
        foundFilm['year'] = request.json['year']   
    values = (foundFilm['title'],foundFilm['director'],foundFilm['year'],foundFilm['id'])
    filmDAO.update(values)
    return jsonify(foundFilm)
    
# delete
@app.route('/films/<int:id>', methods=['DELETE'])
def delete(id):
    foundFilms = list(filter (lambda t : t["id"]==id, films))
    if len(foundFilms)== 0:
        return jsonify({}), 404
    films.remove(foundFilms[0])
    filmDAO.delete(id)
    return jsonify({"done":True})



if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    