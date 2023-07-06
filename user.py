import random
from datetime import datetime


class User:
    def __init__(self, userId, name, email, age, subscription):
        self.userId = userId  # int
        self.name = name
        self.email = email  # string
        self.age = age  # int
        self.dateCreated = datetime.now().isoformat()  # date
        self.subscription = subscription  # string

    def toDict(self):
        return {
            "userId": self.userId,
            "email": self.email,
            "age": self.age,
            "dateCreated": self.dateCreated,
            "subscription": self.subscription
        }

    @classmethod
    def fromDict(cls, user_dict):
        userId = user_dict.get("userId")
        name = user_dict.get("name")
        email = user_dict.get("email")
        age = user_dict.get("age")
        dateCreated = user_dict.get("dateCreated")
        subscription = user_dict.get("subscription")
        user = cls(userId, name, email, age, subscription)
        user.dateCreated = dateCreated
        return user
