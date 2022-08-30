from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
    

@app.route('/process', methods=['POST'])
def process():

	email = request.form['email']
	name = request.form['name']

	if name and email:
		newName = name[::]
		newEmail = email[::]

		return jsonify({'name' : newName, 'email' : newEmail})

	return jsonify({'error' : 'Missing data!'})

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True, port=5001)
