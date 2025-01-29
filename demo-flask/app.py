from flask import Flask, render_template, redirect, request, jsonify
from customer import Customer

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('content1.html')

@app.route('/customer', methods=['GET'])
def customer():
    
    return render_template('/customer.html', customers=Customer.getCustomer())

@app.route('/addCustomer', methods=['POST'])
def addCustomer():
    Customer.add_customer(request.form["name"], request.form["email"])
    return redirect('/customer')

@app.route('/getCustomer', methods=['GET'])
def getCustomer():
    return jsonify(Customer.getCustomer())
@app.route('/hello', methods=['GET'])
def hello():
    return "hello"

if __name__ == "__main__":
    app.run(debug=True)