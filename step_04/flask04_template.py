from flask import Flask,jsonify,render_template
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

app.run(debug=True)