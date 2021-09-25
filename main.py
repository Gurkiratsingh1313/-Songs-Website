from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from werkzeug.utils import redirect
from form import FlaskForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

cafeform = FlaskForm

DB_URL = 'sqlite:///songs.db'

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.String(250), unique=False, nullable=False)
    link = db.Column(db.String(250), unique=True, nullable=False)
    explicit = db.Column(db.String(250), unique=False, nullable=False)
    genre = db.Column(db.String(250), unique=False, nullable=False)


    def __repr__(self):
        # This will allow each song object to be identified by its title when printed.
        return f'<Song: {self.name}>'

db.create_all()

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_song():
    form = cafeform()
    if form.validate_on_submit():
        new_song = Songs(
            name=form.song_name.data,
            link=form.link.data,
            rating=form.song_rating.data,
            explicit=form.explicit.data,
            genre=form.genre.data
        )
        db.session.add(new_song)
        db.session.commit()
        return redirect(url_for('songs'))
    return render_template('add.html', form=form)


@app.route('/songs')
def songs():
    songs = Songs.query.all()
    return render_template('songs.html', songs=songs)

@app.route('/song-delete/<int:song_id>')
def delete(song_id):
    song_to_delete = Songs.query.get(song_id)
    db.session.delete(song_to_delete)
    db.session.commit()
    return redirect(url_for('songs'))


if __name__ == '__main__':
    app.run(debug=True)
