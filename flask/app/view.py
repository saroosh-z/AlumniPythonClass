from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'index Page'

@app.route('/hello')
def hello_world():
    return 'Hello World!'

if __name__ == "__main__":
    app.run()
