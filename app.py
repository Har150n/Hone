from random import randint

from flask import Flask, render_template, request, redirect, session, url_for

from game import Game

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.debug = True



# Flask routes for handling game logic
@app.route('/')
def home():

    #   creates a game object in the db if no game exists
    game = Game.getGame(randint(10000, 99999))
    Game.updateGame(game)
    return render_template('index.html', userId = game.userId)

@app.route('/levels/<userId>', methods=['GET'])
def levels(userId):
    game = Game.getGame(userId)
    game.currentLevel = None
    game = Game.updateGame(game)
    return render_template('levels.html', userId = userId, levels = game.levels)


@app.route('/quiz/<userId>/<level>', methods=['POST', 'GET'])
def quiz(userId, level):
    game = Game.getGame(userId)

    #   assigns value to currentLevel based on clicked level
    if game.currentLevel is None and (isinstance(level, str) or isinstance(level, int)):
        game.currentLevel = game.levels[int(level)-1]

    if request.method == 'POST':

        #   receive emotion data from button clicked (ERROR CHECK)
        emotion = request.form['emotion']

        #   the player levels up
        #   completion holds whether the level is complete or not
        completion = game.submitAnswer(emotion)

        # reset score and index to 0
        if completion == 'Complete':
            game.currentLevel.score = 0
            game.currentLevel.index = 0
            game.currentLevel.levelCompleted = True

        #   update levels to reflect current level
        game.levels[int(level)-1] = game.currentLevel
        game = Game.updateGame(game)

        #   configure url for levels page
        url = url_for('levels', userId=userId)
        imageName = game.currentLevel.questions[game.currentLevel.index].imageName
        score = game.currentLevel.score

        return {'imageName': imageName, 'userId': userId,
                'level': level, 'score': score, 'completion': completion,
                'redirect': url}

    else:
        return render_template('quiz.html',  userId = userId, level=game.currentLevel ,
                               question = game.currentLevel.questions[game.currentLevel.index])

if __name__ == '__main__':
    app.run()

