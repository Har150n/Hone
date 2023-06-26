from flask import Flask, render_template, request, redirect, session

from game import Game, Level, Question

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.debug = True



# Flask routes for handling game logic
@app.route('/')
def home():
    #   creates a game object in the db if no game exists
    game = Game.getGame(123)
    Game.updateGame(game)
    return render_template('home.html', userId = game.userId)

@app.route('/levels/<userId>')
def levels(userId):
    game = Game.getGame(userId)
    return render_template('levels.html', userId = game.userId, levels = game.levels)


@app.route('/quiz/<userId>/<level>', methods=['GET', 'POST'])
def quiz(userId, level):
    game = Game.getGame(userId)
    game.currentLevel = game.levels[int(level)-1]
    Game.updateGame(game)
    if request.method == 'POST':
        emotion = request.form['emotion']
        print(emotion)
        return render_template('quiz.html', userId = userId, level=game.currentLevel,
                               question = game.currentLevel.questions[int(level)-1])
    else:
        return render_template('quiz.html',  userId = userId, level=game.currentLevel ,
                               question = game.currentLevel.questions[int(level)-1])


if __name__ == '__main__':
    app.run()