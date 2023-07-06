import random, game_controller as gc


class Level:
    def __init__(self, level, mode, questions, emotions, index=0, score=0, levelCompleted=False):
        self.level = level
        self.mode = mode
        self.questions = questions  # List of Question objects
        self.emotions = emotions
        self.index = int(index)
        self.score = int(score)
        self.levelCompleted = levelCompleted

    def toDict(self):
        questionsDict = [question.toDict() for question in self.questions]
        levelDict = {
            "level": self.level,
            "mode": self.mode,
            "questions": questionsDict,
            "emotions": self.emotions,
            "index": self.index,
            "score": self.score,
            "levelCompleted": self.levelCompleted
        }
        return levelDict

    @classmethod
    def fromDict(cls, levelDict):
        level = int(levelDict["level"])
        mode = levelDict["mode"]
        questions = [Question.fromDict(q) for q in levelDict["questions"]]
        emotions = levelDict["emotions"]
        index = int(levelDict["index"])
        score = int(levelDict["score"])
        levelCompleted = levelDict["levelCompleted"]
        return cls(level, mode, questions, emotions, index, score, levelCompleted)


# Question class to represent each question in a level
class Question:
    def __init__(self, qId, imageName, options, answer):
        self.qId = qId
        self.imageName = imageName
        self.emotionData = None
        self.options = options  # list of options
        self.answer = answer  # list of correct emotion options

    def toDict(self):
        questionDict = {
            "qId": self.qId,
            "imageName": self.imageName,
            "emotionData": self.emotionData,
            "options": self.options,
            "answer": self.answer
        }
        return questionDict

    @classmethod
    def fromDict(cls, questionDict):
        qId = int(questionDict["qId"])
        imageName = questionDict["imageName"]
        emotionData = questionDict["emotionData"]
        options = questionDict["options"]
        answer = questionDict["answer"]
        return cls(qId, imageName, options, answer)



# Game class to manage the overall game state
class Game:
    def __init__(self, userId):
        #   userId 123 is for demo players
        self.userId = userId
        self.levels = populateLevels()
        self.currentLevel = None

        if int(userId) == 1000000:
            self.levels = self.levels[0:2]


    def getLevel(self, levelNum):
        if self.levels is not None:
            return self.levels[levelNum - 1]




    def submitAnswer(self, emotion):
        SCORE_TO_LEVEL_UP = 10
        currentQuestion = self.currentLevel.questions[self.currentLevel.index]
        if currentQuestion.answer in emotion:
            #   check if over index
            if (self.currentLevel.index + 1) == len(self.currentLevel.questions):
                self.currentLevel.index = 0
            else:
                self.currentLevel.index += 1

            self.currentLevel.score += 1
            if self.currentLevel.score >= SCORE_TO_LEVEL_UP:
                #   completion status is updated in parent function
                return 'Complete'
            else:
                return 'Incomplete'

        else:
            return 'Wrong answer'


    def toDict(self):
        currentLevelDict = self.currentLevel.toDict() if self.currentLevel is not None else None
        gameDict = {
            "userId": self.userId,
            "levels": [level.toDict() for level in self.levels],
            "currentLevel": currentLevelDict
        }
        return gameDict


    @classmethod
    def fromDict(cls, gameDict):
        userId = gameDict["userId"]
        levels = [Level.fromDict(level) for level in gameDict["levels"]]
        currentLevelDict = gameDict["currentLevel"]
        currentLevel = Level.fromDict(currentLevelDict) if currentLevelDict is not None else None
        game = cls(userId)
        game.levels = levels
        game.currentLevel = currentLevel
        return game


    # Input: (str) userId
    # Output: (game obj) game
    # returns a game object of the user's current game state given a userId
    @staticmethod
    def getGame(userId):
        if isinstance(userId, str):
            userId = int(userId)
        game = gc.retrieveGame(userId)
        if game == -1:
            newGame = Game(userId)
            gc.newGame(newGame)  # inserts a new game into the table
            return newGame
        else:
            deserializedObj = Game.fromDict(game)
            return deserializedObj


    # Input: userId, (game obj) game
    # Output: return the game
    @staticmethod
    def updateGame(game):
        return gc.newGame(game)


def populateLevels():
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
            Question(101, 'happy1.jpg', ['happy', 'sad', 'angry'], 'happy'),
            Question(102, 'happy2.jpg', ['happy', 'sad', 'angry'], 'happy'),
            Question(103, 'happy3.jpg', ['happy', 'sad', 'angry'], 'happy'),
            Question(104, 'happy4.jpg', ['happy', 'sad', 'angry'], 'happy'),
            Question(105, 'happy5.jpg', ['happy', 'sad', 'angry'], 'happy'),
            Question(106, 'happy6.jpg', ['happy', 'sad', 'angry'], 'happy'),
            Question(107, 'happy7.jpg', ['happy', 'sad', 'angry'], 'happy'),
            Question(108, 'happy8.jpg', ['happy', 'sad', 'angry'], 'happy'),
            Question(109, 'happy9.jpg', ['happy', 'sad', 'angry'], 'happy'),
            Question(110, 'happy10.jpg', ['happy', 'sad', 'angry'], 'happy'),
            Question(111, 'happy11.jpg', ['happy', 'sad', 'angry'], 'happy'),
            Question(112, 'happy12.jpg', ['happy', 'sad', 'angry'], 'happy'),
            Question(113, 'sad1.jpg', ['happy', 'sad', 'angry'], 'sad'),
            Question(114, 'sad2.jpg', ['happy', 'sad', 'angry'], 'sad'),
            Question(115, 'sad3.jpg', ['happy', 'sad', 'angry'], 'sad'),
            Question(116, 'sad4.jpg', ['happy', 'sad', 'angry'], 'sad'),
            Question(117, 'sad5.jpg', ['happy', 'sad', 'angry'], 'sad'),
            Question(118, 'sad6.jpg', ['happy', 'sad', 'angry'], 'sad'),
            Question(119, 'sad7.jpg', ['happy', 'sad', 'angry'], 'sad'),
            Question(120, 'sad8.jpg', ['happy', 'sad', 'angry'], 'sad'),
            Question(121, 'sad9.jpg', ['happy', 'sad', 'angry'], 'sad'),
            Question(122, 'sad10.jpg', ['happy', 'sad', 'angry'], 'sad'),
            Question(123, 'sad11.jpg', ['happy', 'sad', 'angry'], 'sad'),
            Question(124, 'sad12.jpg', ['happy', 'sad', 'angry'], 'sad'),
            Question(125, 'angry1.jpg', ['happy', 'sad', 'angry'], 'angry'),
            Question(126, 'angry2.jpg', ['happy', 'sad', 'angry'], 'angry'),
            Question(127, 'angry3.jpg', ['happy', 'sad', 'angry'], 'angry'),
            Question(128, 'angry4.jpg', ['happy', 'sad', 'angry'], 'angry'),
            Question(129, 'angry5.jpg', ['happy', 'sad', 'angry'], 'angry'),
            Question(130, 'angry6.jpg', ['happy', 'sad', 'angry'], 'angry'),
            Question(131, 'angry7.jpg', ['happy', 'sad', 'angry'], 'angry'),
            Question(132, 'angry8.jpg', ['happy', 'sad', 'angry'], 'angry'),
            Question(133, 'angry9.jpg', ['happy', 'sad', 'angry'], 'angry'),
            Question(134, 'angry10.jpg', ['happy', 'sad', 'angry'], 'angry'),
            Question(135, 'angry11.jpg', ['happy', 'sad', 'angry'], 'angry'),
            Question(136, 'angry12.jpg', ['happy', 'sad', 'angry'], 'angry'),
        ]
        med_emotions = ['happy', 'sad', 'angry']
        hard_questions = [
            Question(200, 'happy1.jpg', ['happy', 'sad', 'angry', 'neutral'], 'happy'),
            Question(201, 'happy2.jpg', ['happy', 'sad', 'angry', 'neutral'], 'happy'),
            Question(202, 'happy3.jpg', ['happy', 'sad', 'angry', 'neutral'], 'happy'),
            Question(203, 'happy4.jpg', ['happy', 'sad', 'angry', 'neutral'], 'happy'),
            Question(204, 'happy5.jpg', ['happy', 'sad', 'angry', 'neutral'], 'happy'),
            Question(205, 'happy6.jpg', ['happy', 'sad', 'angry', 'neutral'], 'happy'),
            Question(206, 'happy7.jpg', ['happy', 'sad', 'angry', 'neutral'], 'happy'),
            Question(207, 'happy8.jpg', ['happy', 'sad', 'angry', 'neutral'], 'happy'),
            Question(208, 'neutral11.jpg', ['happy', 'sad', 'angry', 'neutral'], 'neutral'),
            Question(209, 'neutral1.jpg', ['happy', 'sad', 'angry', 'neutral'], 'neutral'),
            Question(210, 'neutral2.jpg', ['happy', 'sad', 'angry', 'neutral'], 'neutral'),
            Question(211, 'neutral3.jpg', ['happy', 'sad', 'angry', 'neutral'], 'neutral'),
            Question(212, 'sad1.jpg', ['happy', 'sad', 'angry', 'neutral'], 'sad'),
            Question(213, 'sad2.jpg', ['happy', 'sad', 'angry', 'neutral'], 'sad'),
            Question(214, 'sad3.jpg', ['happy', 'sad', 'angry', 'neutral'], 'sad'),
            Question(215, 'sad4.jpg', ['happy', 'sad', 'angry', 'neutral'], 'sad'),
            Question(216, 'sad5.jpg', ['happy', 'sad', 'angry', 'neutral'], 'sad'),
            Question(217, 'sad6.jpg', ['happy', 'sad', 'angry', 'neutral'], 'sad'),
            Question(218, 'sad7.jpg', ['happy', 'sad', 'angry', 'neutral'], 'sad'),
            Question(219, 'sad8.jpg', ['happy', 'sad', 'angry', 'neutral'], 'sad'),
            Question(220, 'neutral4.jpg', ['happy', 'sad', 'angry', 'neutral'], 'neutral'),
            Question(221, 'neutral5.jpg', ['happy', 'sad', 'angry', 'neutral'], 'neutral'),
            Question(222, 'neutral6.jpg', ['happy', 'sad', 'angry', 'neutral'], 'neutral'),
            Question(223, 'neutral7.jpg', ['happy', 'sad', 'angry', 'neutral'], 'neutral'),
            Question(224, 'angry1.jpg', ['happy', 'sad', 'angry', 'neutral'], 'angry'),
            Question(225, 'angry2.jpg', ['happy', 'sad', 'angry', 'neutral'], 'angry'),
            Question(226, 'angry3.jpg', ['happy', 'sad', 'angry', 'neutral'], 'angry'),
            Question(227, 'angry4.jpg', ['happy', 'sad', 'angry', 'neutral'], 'angry'),
            Question(228, 'angry5.jpg', ['happy', 'sad', 'angry', 'neutral'], 'angry'),
            Question(229, 'angry6.jpg', ['happy', 'sad', 'angry', 'neutral'], 'angry'),
            Question(230, 'angry7.jpg', ['happy', 'sad', 'angry', 'neutral'], 'angry'),
            Question(231, 'angry8.jpg', ['happy', 'sad', 'angry', 'neutral'], 'angry'),
            Question(232, 'neutral12.jpg', ['happy', 'sad', 'angry', 'neutral'], 'neutral'),
            Question(233, 'neutral8.jpg', ['happy', 'sad', 'angry', 'neutral'], 'neutral'),
            Question(234, 'neutral9.jpg', ['happy', 'sad', 'angry', 'neutral'], 'neutral'),
            Question(235, 'neutral10.jpg', ['happy', 'sad', 'angry', 'neutral'], 'neutral')
        ]
        hard_emotions = ['happy', 'sad', 'angry', 'neutral']
        harder_questions = [
            Question(300, 'disgust1.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'disgust'),
            Question(301, 'disgust2.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'disgust'),
            Question(302, 'disgust3.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'disgust'),
            Question(303, 'happy5.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'happy'),
            Question(304, 'happy6.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'happy'),
            Question(305, 'happy7.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'happy'),
            Question(306, 'happy8.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'happy'),
            Question(307, 'disgust4.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'disgust'),
            Question(308, 'disgust5.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'disgust'),
            Question(309, 'disgust6.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'disgust'),
            Question(310, 'neutral3.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'neutral'),
            Question(311, 'sad1.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'sad'),
            Question(312, 'sad2.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'sad'),
            Question(313, 'sad3.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'sad'),
            Question(314, 'sad4.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'sad'),
            Question(315, 'sad5.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'sad'),
            Question(316, 'disgust7.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'disgust'),
            Question(317, 'disgust8.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'disgust'),
            Question(318, 'sad8.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'sad'),
            Question(319, 'neutral4.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'neutral'),
            Question(320, 'neutral5.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'neutral'),
            Question(321, 'neutral6.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'neutral'),
            Question(322, 'neutral7.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'neutral'),
            Question(323, 'angry1.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'angry'),
            Question(324, 'angry2.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'angry'),
            Question(325, 'angry3.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'angry'),
            Question(326, 'angry4.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'angry'),
            Question(327, 'angry5.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'angry'),
            Question(328, 'angry6.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'angry'),
            Question(329, 'disgust9.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'disgust'),
            Question(330, 'disgust10.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'disgust'),
            Question(331, 'neutral12.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'neutral'),
            Question(332, 'neutral8.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'neutral'),
            Question(333, 'neutral9.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'neutral'),
            Question(334, 'neutral10.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'neutral'),
            Question(335, 'happy1.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'happy')]
        harder_emotions = ['happy', 'sad', 'angry', 'neutral', 'fear', 'disgust']
        levels = [
            Level(level=1, mode='Easy', questions=random.sample(easy_questions, 10), emotions=easy_emotions),
            Level(level=2, mode='Easy', questions=random.sample(easy_questions, 10), emotions=easy_emotions),
            Level(level=3, mode='Easy', questions=random.sample(easy_questions, 10), emotions=easy_emotions),
            Level(level=4, mode='Easy', questions=random.sample(easy_questions, 10), emotions=easy_emotions),
            Level(level=5, mode='Easy', questions=random.sample(easy_questions, 10), emotions=easy_emotions),
            Level(level=6, mode='Medium', questions=random.sample(med_questions, 10), emotions=med_emotions),
            Level(level=7, mode='Medium', questions=random.sample(med_questions, 10), emotions=med_emotions),
            Level(level=8, mode='Medium', questions=random.sample(med_questions, 10), emotions=med_emotions),
            Level(level=9, mode='Medium', questions=random.sample(med_questions, 10), emotions=med_emotions),
            Level(level=10, mode='Medium', questions=random.sample(med_questions, 10), emotions=med_emotions),
            Level(level=11, mode='Hard', questions=random.sample(hard_questions, 10), emotions=hard_emotions),
            Level(level=12, mode='Hard', questions=random.sample(hard_questions, 10), emotions=hard_emotions),
            Level(level=13, mode='Hard', questions=random.sample(hard_questions, 10), emotions=hard_emotions),
            Level(level=14, mode='Hard', questions=random.sample(hard_questions, 10), emotions=hard_emotions),
            Level(level=15, mode='Hard', questions=random.sample(hard_questions, 10), emotions=hard_emotions),
            Level(level=16, mode='Harder', questions=random.sample(harder_questions, 10), emotions=harder_emotions),
            Level(level=17, mode='Harder', questions=random.sample(harder_questions, 10), emotions=harder_emotions),
            Level(level=18, mode='Harder', questions=random.sample(harder_questions, 10), emotions=harder_emotions),
            Level(level=19, mode='Harder', questions=random.sample(harder_questions, 10), emotions=harder_emotions),
            Level(level=20, mode='Harder', questions=random.sample(harder_questions, 10), emotions=harder_emotions)

        ]

        return levels
