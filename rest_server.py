from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__, static_url_path='', static_folder='staticpages')

books =[
    {"id": 1, "Title": "Harry Potter", "Author": "JK Rowling", "Price": 2500},
    {"id": 2, "Title": "twilight", "Author": "Stephanie", "Price": 500},
    {"id": 3, "Title": "Coding for Dummies", "Author": "Jon Hancock", "Price": 5300}]
nextID =4

@app.route('/')
def index():
    return "hello"

# return all
@app.route('/books')
def getAll():
    return jsonify(books)
  
# get by id  
@app.route('/books/<int:id>')
def findByID(id):
    foundBooks = list(filter (lambda t : t["id"]==id, books))
    if len(foundBooks)== 0:
        return jsonify({}), 204
    return jsonify(foundBooks[0])
  
# create  
@app.route('/books', methods=['POST'])
def create():
    global nextID
    if not request.json:
        abort(400)
        
    book = {
        "id": nextID,
        "Title": request.json["Title"],
        "Author": request.json["Author"],
        "Price": request.json["Price"] 
    }
    books.append(book)
    nextID += 1
    return jsonify(book)

# update
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    foundBooks = list(filter (lambda t : t["id"]==id, books))
    if len(foundBooks)== 0:
        return jsonify({}), 404
    currentBook = foundBooks[0]
    if 'Title' in request.json:
        currentBook['Title'] = request.json['Title']
    if 'Author' in request.json:
        currentBook['Author'] = request.json['Author']
    if 'Price' in request.json:
        currentBook['Price'] = request.json['Price']   
    return jsonify(currentBook)
    
# delete
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    foundBooks = list(filter (lambda t : t["id"]==id, books))
    if len(foundBooks)== 0:
        return jsonify({}), 404
    books.remove(foundBooks[0])
    return jsonify({"done":True})


if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    