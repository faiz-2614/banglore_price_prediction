from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/get_area_type')
def get_area_type():
    response = jsonify({
        'area_type': util.get_area_type()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def get_home_price():

    total_sqft = float(request.form['total_sqft'])
    area_type = request.form['area_type']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(area_type, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask for Home Price Prediction..")
    util.load_saved_artifacts()
    app.run()