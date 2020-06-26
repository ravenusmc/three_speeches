from flask import Flask, jsonify, request
from flask_cors import CORS

#importing code that I wrote
from study import *
from sentiment import *

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

#This route will get the data for the charts
@app.route('/getWordCountData', methods=['GET', 'POST'])
def routeOne():
    if request.method == 'POST':
        study = Words()
        post_data = request.get_json()
        selected_speech = post_data['speech']
        chartData = study.build_word_chart(selected_speech)
        return jsonify(chartData)

#This route will get the sentiment for the charts
@app.route('/getWordCountData', methods=['GET'])
def routeOne():
    if request.method == 'POST':
        study = Words()
        post_data = request.get_json()
        selected_speech = post_data['speech']
        chartData = study.build_word_chart(selected_speech)
        return jsonify(chartData)

if __name__ == '__main__':
    app.run()
