from flask import Flask, url_for, request, redirect, abort, jsonify, render_template
from stockDAO import stockDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')

stock =[
    {"code": 102852, "Product": "Knit Cardigan", "amount": 12, "price": 21.50},
    {"code": 115262, "Product": "Denim Jacket", "amount": 8, "price": 33.60},
    {"code": 103264, "Product": "Sweater Dress", "amount": 7, "price": 14.40}]
nextID =4

@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'password':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect('stock.html')
    return render_template('login.html', error=error)

# return all
@app.route('/stock')
def getAll():
    results = stockDAO.getAll()
    return jsonify(results)

@app.route('/timetable')
def getHours():
    results = stockDAO.getHours()
    return jsonify(results)

# get stock by id  
@app.route('/stock/<int:code>')
def findByID(code):
    '''foundstock = list(filter (lambda t : t["code"]==id, stock))
    if len(foundstock)== 0:
        return jsonify({}), 204'''
    return jsonify(stockDAO.findByID(code))
    
# get hours by employee  
@app.route('/timetable/<string:employee>')
def findByEmp(employee):
    '''foundemp = list(filter (lambda t : t["employee"]==id, hours))
    if len(foundhours)== 0:
        return jsonify({}), 204'''
    return jsonify(stockDAO.findByEmp(employee))
    
# create stock
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

# create hours
@app.route('/timetable', methods=['POST'])
def createHours():
    if not request.json:
        abort(400)
    hours = {
        "employee": request.json["employee"],
        "monday": request.json["monday"],
        "tuesday": request.json["tuesday"],
        "wednesday": request.json["wednesday"],
        "thursday": request.json["thursday"],
        "friday": request.json["friday"],
        "saturday": request.json["saturday"]}    
 
    return jsonify(stockDAO.createHours(hours))

# update stock
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

# update hours
@app.route('/timetable/<string:employee>', methods=['PUT'])
def updateHours(hours):
    foundhours = stockDAO.findByEmp(employee)
    if not foundhours:
        abort(404)
    if not request.json:
        abort(404)
    currenthours = foundhours
    if 'monday' in request.json:
        currenthours['monday'] = request.json['monday']
    if 'tuesday' in request.json:
        currenthours['tuesday'] = request.json['tuesday']
    if 'wednesday' in request.json:
        currenthours['wednesday'] = request.json['wednesday']
    if 'thursday' in request.json:
        currenthours['thursday'] = request.json['thursday']
    if 'friday' in request.json:
        currenthours['friday'] = request.json['friday']
    if 'saturday' in request.json:
        currenthours['saturday'] = request.json['saturday']        
    #values = (currentstock['Product'],currentstock['amount'],currentstock['price'],currentstock['code'])
    stockDAO.updateHours(currenthours)
    return jsonify(currenthours)

# delete
@app.route('/stock/<int:code>', methods=['DELETE'])
def delete(code):
    #foundstock = list(filter (lambda t : t["code"]==id, stock))
    #if len(foundstock)== 0:
        #return jsonify({}), 404
    #stock.remove(foundstock[0])
        stockDAO.delete(code)
        return jsonify({"done":True})

# delete hours
@app.route('/timetable/<string:employee>', methods=['DELETE'])
def deleteHours(employee):
    #foundstock = list(filter (lambda t : t["code"]==id, stock))
    #if len(foundstock)== 0:
        #return jsonify({}), 404
    #stock.remove(foundstock[0])
        stockDAO.deleteHours(employee)
        return jsonify({"done":True})


if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    