from flask import Flask, jsonify
from flask_cors import cross_origin

app = Flask(__name__)

@app.route('/', methods=['GET'])
@cross_origin()
def root():
	return jsonify({ 'message': u'Hello from ReAsk!' })

if __name__ == '__main__':
	# only used locally
	app.run(host='0.0.0.0', port=8080, debug=True)
