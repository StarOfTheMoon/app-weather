import requests
from flask import Flask
from flask import request, render_template


app = Flask(__name__)
api_key = '12d601c64703986d2035b59334bfa3bb'
url_google = "https://maps.googleapis.com/maps/api/place/autocomplete/json?input="
url_weather = "http://api.openweathermap.org/data/2.5/weather?"
gkey = "AIzaSyCpQ9JYs7L8EKaOwOIl_deELvYaOviWPw0"

# current weather
@app.route('/')
def index(current=None):
	current = requests.get(url_weather +"q=Paris&APPID="+api_key+"&units=metric&lang=fr").json()
	print(current)
	return render_template('index.html', current=current)

@app.route('/search', methods=['POST','GET'])
def search(current=None):
	city = ""
	predictions = [];
	if request.method == 'POST':
		if request.form['city']:
			city = request.form['city']
	else: 
		city = "Paris"
	current = requests.get(url_weather+"q="+city+"&APPID="+api_key+"&units=metric&lang=fr").json()
	print(current)
	return render_template('index.html', current=current)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8001)

