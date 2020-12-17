from flask import Flask, url_for, request, redirect, abort, jsonify
from stockDAO import stockDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')

stock =[
    {"code": 102852, "Product": "Knit Cardigan", "amount": 12, "price": 21.50},
    {"code": 115262, "Product": "Denim Jacket", "amount": 8, "price": 33.60},
    {"code": 103264, "Product": "Sweater Dress", "amount": 7, "price": 14.40}]
nextID =4

@app.route('/')
def index():
    return "hello"

# return all
@app.route('/stock')
def getAll():
    results = stockDAO.getAll()
    return jsonify(results)
  
# get by id  
@app.route('/stock/<int:code>')
def findByID(code):
    '''foundstock = list(filter (lambda t : t["code"]==id, stock))
    if len(foundstock)== 0:
        return jsonify({}), 204'''
    return jsonify(stockDAO.findByID(code))
  
# create  
@app.route('/stock', methods=['POST'])
def create():

    if not request.json:
        abort(400)
        
    stock = {
        "code": request.json["code"],
        "Product": request.json["Product"],
        "amount": request.json["amount"],
        "price": request.json["price"]}
 
    return jsonify(stockDAO.create(stock))

# update
@app.route('/stock/<int:code>', methods=['PUT'])
def update(code):
    foundstock = stockDAO.findByID(code)
    if not foundstock:
        abort(404)
    if not request.json:
        abort(404)
    currentstock = foundstock
    if 'Product' in request.json:
        currentstock['Product'] = request.json['Product']
    if 'amount' in request.json:
        currentstock['amount'] = request.json['amount']
    if 'price' in request.json:
        currentstock['price'] = request.json['price']   
    #values = (currentstock['Product'],currentstock['amount'],currentstock['price'],currentstock['code'])
    stockDAO.update(currentstock)
    return jsonify(currentstock)
    
# delete
@app.route('/stock/<int:code>', methods=['DELETE'])
def delete(code):
    #foundstock = list(filter (lambda t : t["code"]==id, stock))
    #if len(foundstock)== 0:
        #return jsonify({}), 404
    #stock.remove(foundstock[0])
        stockDAO.delete(code)
        return jsonify({"done":True})



if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    