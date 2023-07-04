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
        self.userId = userId
        self.levels = self.populateLevels()
        self.currentLevel = None

    def getLevel(self, levelNum):
        if self.levels is not None:
            return self.levels[levelNum - 1]

    def populateLevels(self):
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
        hard_questions = [
            Question(61, 'happy1.jpg', ['happy', 'sad', 'angry', 'neutral'], 'happy'),
            Question(62, 'happy2.jpg', ['happy', 'sad', 'angry', 'neutral'], 'happy'),
            Question(63, 'happy3.jpg', ['happy', 'sad', 'angry', 'neutral'], 'happy'),
            Question(64, 'happy4.jpg', ['happy', 'sad', 'angry', 'neutral'], 'happy'),
            Question(65, 'happy5.jpg', ['happy', 'sad', 'angry', 'neutral'], 'happy'),
            Question(66, 'happy6.jpg', ['happy', 'sad', 'angry', 'neutral'], 'happy'),
            Question(67, 'happy7.jpg', ['happy', 'sad', 'angry', 'neutral'], 'happy'),
            Question(68, 'happy8.jpg', ['happy', 'sad', 'angry', 'neutral'], 'happy'),
            Question(69, 'neutral11.jpg', ['happy', 'sad', 'angry', 'neutral'], 'neutral'),
            Question(70, 'neutral1.jpg', ['happy', 'sad', 'angry', 'neutral'], 'neutral'),
            Question(71, 'neutral2.jpg', ['happy', 'sad', 'angry', 'neutral'], 'neutral'),
            Question(72, 'neutral3.jpg', ['happy', 'sad', 'angry', 'neutral'], 'neutral'),
            Question(73, 'sad1.jpg', ['happy', 'sad', 'angry', 'neutral'], 'sad'),
            Question(74, 'sad2.jpg', ['happy', 'sad', 'angry', 'neutral'], 'sad'),
            Question(75, 'sad3.jpg', ['happy', 'sad', 'angry', 'neutral'], 'sad'),
            Question(76, 'sad4.jpg', ['happy', 'sad', 'angry', 'neutral'], 'sad'),
            Question(77, 'sad5.jpg', ['happy', 'sad', 'angry', 'neutral'], 'sad'),
            Question(78, 'sad6.jpg', ['happy', 'sad', 'angry', 'neutral'], 'sad'),
            Question(79, 'sad7.jpg', ['happy', 'sad', 'angry', 'neutral'], 'sad'),
            Question(80, 'sad8.jpg', ['happy', 'sad', 'angry', 'neutral'], 'sad'),
            Question(81, 'neutral4.jpg', ['happy', 'sad', 'angry', 'neutral'], 'neutral'),
            Question(82, 'neutral5.jpg', ['happy', 'sad', 'angry', 'neutral'], 'neutral'),
            Question(83, 'neutral6.jpg', ['happy', 'sad', 'angry', 'neutral'], 'neutral'),
            Question(84, 'neutral7.jpg', ['happy', 'sad', 'angry', 'neutral'], 'neutral'),
            Question(85, 'angry1.jpg', ['happy', 'sad', 'angry', 'neutral'], 'angry'),
            Question(86, 'angry2.jpg', ['happy', 'sad', 'angry', 'neutral'], 'angry'),
            Question(87, 'angry3.jpg', ['happy', 'sad', 'angry', 'neutral'], 'angry'),
            Question(88, 'angry4.jpg', ['happy', 'sad', 'angry', 'neutral'], 'angry'),
            Question(89, 'angry5.jpg', ['happy', 'sad', 'angry', 'neutral'], 'angry'),
            Question(90, 'angry6.jpg', ['happy', 'sad', 'angry', 'neutral'], 'angry'),
            Question(91, 'angry7.jpg', ['happy', 'sad', 'angry', 'neutral'], 'angry'),
            Question(92, 'angry8.jpg', ['happy', 'sad', 'angry', 'neutral'], 'angry'),
            Question(93, 'neutral12.jpg', ['happy', 'sad', 'angry', 'neutral'], 'neutral'),
            Question(94, 'neutral8.jpg', ['happy', 'sad', 'angry', 'neutral'], 'neutral'),
            Question(95, 'neutral9.jpg', ['happy', 'sad', 'angry', 'neutral'], 'neutral'),
            Question(96, 'neutral10.jpg', ['happy', 'sad', 'angry', 'neutral'], 'neutral'),
        ]
        hard_emotions = ['happy', 'sad', 'angry', 'neutral']
        harder_questions = [
            Question(97, 'disgust1.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'disgust'),
            Question(98, 'disgust2.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'disgust'),
            Question(99, 'disgust3.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'happy'),
            Question(101, 'happy5.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'happy'),
            Question(102, 'happy6.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'happy'),
            Question(103, 'happy7.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'happy'),
            Question(104, 'happy8.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'happy'),
            Question(105, 'disgust4.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'disgust'),
            Question(106, 'disgust5.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'disgust'),
            Question(107, 'disgust6.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'disgust'),
            Question(108, 'neutral3.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'neutral'),
            Question(109, 'sad1.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'sad'),
            Question(110, 'sad2.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'sad'),
            Question(111, 'sad3.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'sad'),
            Question(112, 'sad4.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'sad'),
            Question(113, 'sad5.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'sad'),
            Question(114, 'disgust7.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'disgust'),
            Question(115, 'disgust8.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'disgust'),
            Question(116, 'sad8.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'sad'),
            Question(117, 'neutral4.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'neutral'),
            Question(118, 'neutral5.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'neutral'),
            Question(119, 'neutral6.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'neutral'),
            Question(120, 'neutral7.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'neutral'),
            Question(121, 'angry1.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'angry'),
            Question(122, 'angry2.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'angry'),
            Question(123, 'angry3.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'angry'),
            Question(124, 'angry4.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'angry'),
            Question(125, 'angry5.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'angry'),
            Question(126, 'angry6.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'angry'),
            Question(127, 'disgust9.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'disgust'),
            Question(128, 'disgust10.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'disgust'),
            Question(129, 'neutral12.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'neutral'),
            Question(130, 'neutral8.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'neutral'),
            Question(131, 'neutral9.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'neutral'),
            Question(132, 'neutral10.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'neutral'),
            Question(132, 'happy1.jpg', ['happy', 'sad', 'angry', 'neutral', 'disgust'], 'disgust')]
        harder_emotions = ['happy', 'sad', 'angry', 'neutral', 'fear', 'disgust']
        levels = [
            Level(level=1, mode='Easy', questions=random.sample(easy_questions, 12), emotions=easy_emotions),
            Level(level=2, mode='Easy', questions=random.sample(easy_questions, 12), emotions=easy_emotions),
            Level(level=3, mode='Medium', questions=random.sample(med_questions, 12), emotions=med_emotions),
            Level(level=4, mode='Medium', questions=random.sample(med_questions, 12), emotions=med_emotions),
            Level(level=5, mode='Hard', questions=random.sample(hard_questions, 12), emotions=hard_emotions),
            Level(level=6, mode='Hard', questions=random.sample(hard_questions, 12), emotions=hard_emotions),
            Level(level=7, mode='Harder', questions=random.sample(harder_questions, 12), emotions=harder_emotions),
            Level(level=8, mode='Harder', questions=random.sample(harder_questions, 12), emotions=harder_emotions)
        ]
        return levels

    def submitAnswer(self, emotion):
        SCORE_TO_LEVEL_UP = 5
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
