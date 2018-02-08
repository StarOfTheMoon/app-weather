from flask import Flask
from flask import request, render_template
from apixu.client import ApixuClient, ApixuException


app = Flask(__name__)

api_key = 'fa6bb918d26a48d9954143058180502'
client = ApixuClient(api_key)

# current weather
@app.route('/')
def index(current=None):
	# geolocalisation
	def geolocalisation():
		print('coucou')
	geolocalisation()
	current = client.getCurrentWeather(q='Paris')
	return render_template('index.html', current=current)

@app.route('/search', methods=['POST','GET'])
def search(current=None):
	if request.method == 'POST':
		if request.form['city']:
			city = request.form['city']
	current = client.getCurrentWeather(q=city)
	return render_template('index.html', current=current)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)

