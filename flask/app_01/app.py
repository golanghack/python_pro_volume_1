from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to gues string'
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name: str):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(err):
    return render_template('404.html'), 404 

@app.errorhandler(500)
def initial_server_error(err):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)