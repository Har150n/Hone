from enum import Enum
import random


# Level class to represent each level in the game
#Easy has two emotion (str) options, Med has three, Hard has four
class Level:
    Difficulty = Enum('Difficulty', ['EASY', 'MED', 'HARD'])
    def __init__(self, level, mode, questions, emotions):
        self.level = level
        self.mode = mode
        self.questions = questions  # List of Question objects
        self.emotions = emotions
        self.index = 0              #question index
        self.score = 0              #number of corret answers


# Question class to represent each question in a level
class Question:
    def __init__(self, qId, imageName, options, answer):
        self.qId = qId
        self.imageName = imageName
        self.emotionData = None
        self.options = options                      #list of options
        self.answer = answer      #list of correct emotion options

# Game class to manage the overall game state
class Game:
    easy_questions = [
        Question(1, 'happy1.jpg', ['happy', 'sad'], 'happy'),
        Question(2, 'happy2.jpg', ['happy', 'sad'], 'happy'),
        Question(3, 'happy3.jpg', ['happy', 'sad'], 'happy'),
        Question(4, 'happy4.jpg', ['happy', 'sad'], 'happy'),
        Question(5, 'happy5.jpg', ['happy', 'sad'], 'happy'),
        Question(6, 'happy6.jpg', ['happy', 'sad'], 'happy'),
        Question(7, 'happy7.jpg', ['happy', 'sad'], 'happy'),
        Question(8, 'happy8.jpg', ['happy', 'sad'], 'happy'),
        Question(9, 'happy9.jpg', ['happy', 'sad'], 'happy'),
        Question(10, 'happy10.jpg', ['happy', 'sad'], 'happy'),
        Question(11, 'happy11.jpg', ['happy', 'sad'], 'happy'),
        Question(12, 'happy12.jpg', ['happy', 'sad'], 'happy'),
        Question(13, 'sad1.jpg', ['happy', 'sad'], 'sad'),
        Question(14, 'sad2.jpg', ['happy', 'sad'], 'sad'),
        Question(15, 'sad3.jpg', ['happy', 'sad'], 'sad'),
        Question(16, 'sad4.jpg', ['happy', 'sad'], 'sad'),
        Question(17, 'sad5.jpg', ['happy', 'sad'], 'sad'),
        Question(18, 'sad6.jpg', ['happy', 'sad'], 'sad'),
        Question(19, 'sad7.jpg', ['happy', 'sad'], 'sad'),
        Question(20, 'sad8.jpg', ['happy', 'sad'], 'sad'),
        Question(21, 'sad9.jpg', ['happy', 'sad'], 'sad'),
        Question(22, 'sad10.jpg', ['happy', 'sad'], 'sad'),
        Question(23, 'sad11.jpg', ['happy', 'sad'], 'sad'),
        Question(24, 'sad12.jpg', ['happy', 'sad'], 'sad')
    ]
    easy_emotions = ['happy', 'sad']

    med_questions = [
        Question(25, 'happy1.jpg', ['happy', 'sad', 'angry'], 'happy'),
        Question(26, 'happy2.jpg', ['happy', 'sad', 'angry'], 'happy'),
        Question(27, 'happy3.jpg', ['happy', 'sad', 'angry'], 'happy'),
        Question(28, 'happy4.jpg', ['happy', 'sad', 'angry'], 'happy'),
        Question(29, 'happy5.jpg', ['happy', 'sad', 'angry'], 'happy'),
        Question(30, 'happy6.jpg', ['happy', 'sad', 'angry'], 'happy'),
        Question(31, 'happy7.jpg', ['happy', 'sad', 'angry'], 'happy'),
        Question(32, 'happy8.jpg', ['happy', 'sad', 'angry'], 'happy'),
        Question(33, 'happy9.jpg', ['happy', 'sad', 'angry'], 'happy'),
        Question(34, 'happy10.jpg', ['happy', 'sad', 'angry'], 'happy'),
        Question(35, 'happy11.jpg', ['happy', 'sad', 'angry'], 'happy'),
        Question(36, 'happy12.jpg', ['happy', 'sad', 'angry'], 'happy'),
        Question(37, 'sad1.jpg', ['happy', 'sad', 'angry'], 'sad'),
        Question(38, 'sad2.jpg', ['happy', 'sad', 'angry'], 'sad'),
        Question(39, 'sad3.jpg', ['happy', 'sad', 'angry'], 'sad'),
        Question(40, 'sad4.jpg', ['happy', 'sad', 'angry'], 'sad'),
        Question(41, 'sad5.jpg', ['happy', 'sad', 'angry'], 'sad'),
        Question(42, 'sad6.jpg', ['happy', 'sad', 'angry'], 'sad'),
        Question(43, 'sad7.jpg', ['happy', 'sad', 'angry'], 'sad'),
        Question(44, 'sad8.jpg', ['happy', 'sad', 'angry'], 'sad'),
        Question(45, 'sad9.jpg', ['happy', 'sad', 'angry'], 'sad'),
        Question(46, 'sad10.jpg', ['happy', 'sad', 'angry'], 'sad'),
        Question(47, 'sad11.jpg', ['happy', 'sad', 'angry'], 'sad'),
        Question(48, 'sad12.jpg', ['happy', 'sad', 'angry'], 'sad'),
        Question(49, 'angry1.jpg', ['happy', 'sad', 'angry'], 'angry'),
        Question(50, 'angry2.jpg', ['happy', 'sad', 'angry'], 'angry'),
        Question(51, 'angry3.jpg', ['happy', 'sad', 'angry'], 'angry'),
        Question(52, 'angry4.jpg', ['happy', 'sad', 'angry'], 'angry'),
        Question(53, 'angry5.jpg', ['happy', 'sad', 'angry'], 'angry'),
        Question(54, 'angry6.jpg', ['happy', 'sad', 'angry'], 'angry'),
        Question(55, 'angry7.jpg', ['happy', 'sad', 'angry'], 'angry'),
        Question(56, 'angry8.jpg', ['happy', 'sad', 'angry'], 'angry'),
        Question(57, 'angry9.jpg', ['happy', 'sad', 'angry'], 'angry'),
        Question(58, 'angry10.jpg', ['happy', 'sad', 'angry'], 'angry'),
        Question(59, 'angry11.jpg', ['happy', 'sad', 'angry'], 'angry'),
        Question(60, 'angry12.jpg', ['happy', 'sad', 'angry'], 'angry'),
    ]
    med_emotions = ['happy', 'sad', 'angry']
    levels = [
        Level(level=1, mode='Easy', questions=random.sample(easy_questions, 12), emotions=easy_emotions),
        Level(level=2, mode='Easy', questions=random.sample(easy_questions, 12),  emotions=easy_emotions),
        Level(level=3, mode='Medium', questions=random.sample(med_questions, 12),  emotions=med_emotions),
        Level(level=4, mode='Medium', questions=random.sample(med_questions, 12),  emotions=med_emotions)
    ]
    currentLevel = None

    def getLevel(levelNum):
        if Game.levels is not None:
            return Game.levels[levelNum-1]

    def submitAnswer(emotion):
        currentQuestion = Game.currentLevel.questions[Game.currentLevel.index]
        if emotion == currentQuestion.answer:
            Game.currentLevel.score += 1
            Game.currentLevel.index += 1
            print(Game.currentLevel.score)
        else:
            print('Wrong Answer')


