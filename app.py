from flask import Flask, render_template, request, redirect, session

from game import Game, Level, Question

app = Flask(__name__)
app.secret_key = 'your_secret_key'


# Flask routes for handling game logic
@app.route('/')
def home():
    Game.getGame('124')
    return render_template('home.html')

@app.route('/levels')
def levels():
    return render_template('levels.html')


@app.route('/quiz/<level>', methods=['GET', 'POST'])
def quiz(level):
    levelObj = Game.getLevel(int(level))
    Game.currentLevel = levelObj
    if request.method == 'POST':
        emotion = request.form['emotion']
        Game.submitAnswer(emotion)
        print(Game.currentLevel.index)
        return render_template('quiz.html', level=Game.currentLevel, question = Game.currentLevel.questions[Game.currentLevel.index])
    else:
        return render_template('quiz.html', level=Game.currentLevel , question = Game.currentLevel.questions[Game.currentLevel.index])


@app.route('/game')
def game():
    return render_template('game.html')

if __name__ == '__main__':
    app.run()