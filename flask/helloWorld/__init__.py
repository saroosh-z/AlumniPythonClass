from flask import Flask, render_template
app = Flask(__name__)

#create a url
@app.route('/')
def index():
    name = 'user'
    day = 'saturday'
    return render_template('index.html',
                        user = name,
                        day = day)



if __name__ == '__main__':
    app.run(debug = True)
