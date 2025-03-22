from flask import Flask
from models import Game, Studio, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # Создаём тестовые игры
        game1 = Game(name='Half-Life 2')
        game2 = Game(name='Portal 2')
        game3 = Game(name='The Binding of Isaac')
        game4 = Game(name='Team Fortress 2')

        db.session.add_all([game1, game2, game3, game4])
        db.session.commit()

        # Создаём тестовые студии
        studio1 = Studio(name='Valve', year='2004', game=game1)
        studio2 = Studio(name='Valve', year='2011', game=game2)
        studio3 = Studio(name='Edmund McMillen', year='2011', game=game3)
        studio4 = Studio(name='Valve', year='2007', game=game4)

        db.session.add_all([studio1, studio2, studio3, studio4])
        db.session.commit()

        print("База данных успешно заполнена!")
