from flask import Flask
from models import User, db
import configparser
app = Flask(__name__)

config = configparser.ConfigParser()
config.read('.env')
app.config['SECRET_KEY'] = config['DEFAULT']['SECRET_KEY']
app.config['MAIL_SERVER'] = config['DEFAULT']['EMAIL_HOST']
app.config['MAIL_PORT'] = config['DEFAULT']['EMAIL_PORT']
app.config['MAIL_USE_SSL'] = config['DEFAULT']['EMAIL_SSL']
app.config['MAIL_USERNAME'] = config['DEFAULT']['EMAIL_USER']
app.config['MAIL_PASSWORD'] = config['DEFAULT']['EMAIL_PASSWORD']

@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.debug = True
    app.run()