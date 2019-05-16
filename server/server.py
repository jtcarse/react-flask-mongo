from flask import Flask, jsonify
from flask_cors import cross_origin
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
client = MongoClient('mongo', 27017)
db = client.db

@app.route('/', methods=['GET'])
@cross_origin()
def root():
	db.hits.insert_one({ 'time': datetime.utcnow() })
	message = 'This page has been visited {} times.'.format(db.hits.count())
	return jsonify({ 'message': message })

if __name__ == '__main__':
	# only used locally
	app.run(host='0.0.0.0', port=8080, debug=True)
