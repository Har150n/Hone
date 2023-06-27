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
    if game.currentLevel is None and (isinstance(level, str) or isinstance(level, int)):
        game.currentLevel = game.levels[int(level)-1]

    if request.method == 'POST':
        emotion = request.form['emotion']
        game.submitAnswer(emotion)
        #update levels to reflect answer submission
        game.levels[int(level)-1] = game.currentLevel
        game = Game.updateGame(game)
        print(game.currentLevel.index)
        return render_template('quiz.html', userId = userId, level=game.currentLevel,
                               question = game.currentLevel.questions[game.currentLevel.index])
    else:
        return render_template('quiz.html',  userId = userId, level=game.currentLevel ,
                               question = game.currentLevel.questions[game.currentLevel.index])


if __name__ == '__main__':
    app.run()

