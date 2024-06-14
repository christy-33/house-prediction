from flask import Flask, request, jsonify
import util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/hello')
def home():
    return "Welcome to the home page!"

@app.route('/get_locations', methods=['GET'])
def get_locations():
    print("Endpoint /get_locations was called")
    response = jsonify({
        'locations': util.get_locations()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    print("Endpoint /predict_home_price was called")
    area = float(request.form['area'])
    bhk = int(request.form['bhk'])
    resale = int(request.form['resale'])
    intercom = int(request.form['intercom'])
    vaastu = int(request.form['vaastu'])
    ppa = float(request.form['ppa'])
    location = request.form['location']
    connectivity = int(request.form['connectivity'])
    societies = int(request.form['societies'])
    apartment = int(request.form['apartment'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(area, bhk, resale, intercom, vaastu, ppa, location, connectivity, societies, apartment)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask server for Hyderabad house prediction")
    util.load_saved_artifacts()
    app.run(debug=True)

    
