from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
	return 'Hello from ReAsk!'

if __name__ == '__main__':
	# only used locally
	app.run(host='127.0.0.1', port=8080, debug=True)
