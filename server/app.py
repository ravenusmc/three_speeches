from flask import Flask, jsonify, request
from flask_cors import CORS

#importing code that I wrote
from study import *

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

#This route will get the data for the charts
@app.route('/getSpeechData', methods=['GET', 'POST'])
def routeOne():
    if request.method == 'POST':
        study = Data()
        post_data = request.get_json()
        study.build_word_chart(speech)
        #I'll have the speech
        return jsonify(first_chart_data)

if __name__ == '__main__':
    app.run()
