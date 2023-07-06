import random
from datetime import datetime
class User:
    def __init__(self, name, email, age, subscription):
        self.userId = random.randint(10000, 99999)  #int
        self.name = name
        self.email = email      # string
        self.age = age          # int
        self.dateCreated = datetime.now().isoformat()     #date
        self.subscription = subscription    #string

    def toDict(user):
        return {
            "userId": user.userId,
            "email": user.email,
            "age": user.age,
            "dateCreated": user.dateCreated,
            "subscription": user.subscription
        }


