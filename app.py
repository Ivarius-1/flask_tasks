from flask import Flask, render_template
from models import Game, Studio, db
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Связываем приложение и SQLAlchemy
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/games')
def games():
    games_list = Game.query.all()
    return render_template('games.html', games=games_list)


if __name__ == '__main__':
    app.run(debug=True)
