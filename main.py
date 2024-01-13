#Code here
from flask import Flask, request, render_template
from animals import cat

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cat')
def catt():
    image = cat()[0]['url']
    return render_template('animals.html', image=image)

if __name__=="__main__":
    app.run(debug=True, port=5000)