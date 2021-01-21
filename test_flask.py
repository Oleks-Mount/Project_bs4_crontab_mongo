from flask import Flask,render_template
from pymongo import MongoClient


app = Flask(__name__)
app.config.from_object(__name__)



app.config.update(dict(
    #DATABASE = db,
    DEBUG =True,
    SECRET_KEY = 'development key'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/')
def show_news():
    client = MongoClient('localhost', 27017)
    my_db = client['News']
    mycollection = my_db['Soccer']
    data = mycollection.find()
    return render_template('main_page.html',magazine=data)






if __name__ == '__main__':
    app.run(debug =True)