from flask import Flask,jsonify,render_template,request,redirect
from flask_sqlalchemy  import SQLAlchemy
from flask_login import LoginManager, current_user, login_user, login_required, UserMixin, logout_user
import requests, os
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.secret_key = "super secret key"


login_manager = LoginManager(app)
#login_manager.login_view = 'login'
login_manager.init_app(app)

db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True ) 
    email = db.Column(db.String(30),  unique=True )     

def create_db():
    try:
        db.create_all()
        user = User(id=1,username='admin',email='admin@mail.ru')
        guest = User(id=2,username='guest',email='vova@gmail.com')
        db.session.add(user)
        db.session.add(guest)
        db.session.commit()
    except:
        None

#Отвечает за сессию пользователей. Запрещает доступ к роутам, перед которыми указано @login_required
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

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

@app.route('/users/<page>', methods=['GET']) 
def get_run_requests_page(page):
    response=requests.get('https://reqres.in/api/users?page='+page)
    txt=response.json()
    pages=int(txt['total_pages'])
    txt=txt['data']
    return render_template('get.html',out_json=txt,pages=pages)

@app.route('/form',methods=['GET','POST']) 
def form():
    text=''
    if request.method == 'POST' :
        text = request.form.get('input_text')
    return render_template('form.html',text=text)

@app.route('/admin',methods=['GET','POST']) 
def admin():
    name = email =''

    if request.method == 'POST' :
        name = request.form.get('name')
        email = request.form.get('email')
        try:
            user = User(username=name,email=email)
            db.session.add(user)
            db.session.commit()
        except:
            return('При добавлении пользователя произошла ошибка')
    users = User.query.all()
    return render_template('admin.html',users=users,name=name,email=email)


if __name__ == "__main__":
    app.run(debug=True)