from flask import Flask


app = Flask(__name__)

@app.route('/')

def vmname():
	return 'Kinshuk'

if __name__ == '__main__':

	app.run()
