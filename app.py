from flask import Flask, jsonify, redirect, render_template, request, g
from db import get_db

app = Flask(__name__)

# class Urls(db.Model):
#     id = db.Column("id", db.Integer, primary_key=True)
#     longUrl = db.Column("longUrl", db.string())
#     shortUrl = db.Column("shortUrl", db.string(3))

#     def __init__(self, longUrl, shortUrl):
#         self.longUrl = longUrl
#         self.shortUrl = shortUrl

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def shorten_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choices(letters, k=3)
        rand_letters = "".join(rand_letters)
        shortUrl = cursor.execute("SELECT * FROM urls WHERE shortUrl=(?);", (shortUrl))
        if not shortUrl:
            return rand_letters

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         url_recieved = request.form["nm"]
#         foundUrl 
#         return url_recieved
#     else:
#         return render_template('home.html')


@app.route("/", methods=['GET', 'POST'])
def new_url():
    db = get_db()
    cursor = db.cursor()
    
    if request.method == 'POST':
        longUrl = request.form['nm']
        foundUrl = cursor.execute("SELECT * FROM urls WHERE longUrl=(?);", (longUrl))
        if foundUrl:
            return redirect(url_for("display_short_url", url=foundUrl.shortUrl))
        else:
            shortUrl = shorten_url()
            cursor.execute("INSERT INTO urls (longUrl, shortUrl) VALUES (?, ?);", (longUrl, shortUrl))
            db.commit()
            return redirect(url_for("display_short_url", url=shortUrl))
    else:
        return render_template('home.html')

    # cursor.execute("SELECT * from trees")
    # trees = cursor.fetchall()
    # return render_template("new.html", trees=trees)


if __name__ == '__main__':
    app.run(debug=True)