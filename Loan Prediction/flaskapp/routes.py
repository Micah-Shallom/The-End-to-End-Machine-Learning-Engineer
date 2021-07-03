from flaskapp import app
from flask import url_for , render_template , flash , redirect
from .forms import RegisterForm , LoginForm

@app.route("/")
@app.route("/home")
def home():
    return render_template('homepage.html' , title='Homepage')

@app.route("/register" , methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(message='User Successfully Registered' , category='success')
        return redirect(url_for('login'))
    return render_template('register.html'  , title='Register' , form=form)

@app.route("/login" , methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html' , title='Login' , form=form)