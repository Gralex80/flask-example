from flask import Flask,jsonify,render_template
import requests
app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/healthcheck")
def api():
    json_out=[{'status':'started'}]
    return jsonify(json_out), 200

@app.route("/")
def index():
    text='Привет мир!'
    return render_template('index.html',txt=text)

@app.route('/users', methods=['GET']) 
def get_run_requests():
    response=requests.get('https://reqres.in/api/users?page=1')
    txt=response.json()
    txt=txt['data']
    return render_template('get.html',out_json=txt)



app.run(debug=True)