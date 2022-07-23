from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '9sadhf19FA9!@@8FA9SDFAG'


from duranz import routes
