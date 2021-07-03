from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '346e6858d7cab7ae4f529a27567ed57948a684c089db7c9553f2fe521dd9e27f'


from flaskapp import routes

