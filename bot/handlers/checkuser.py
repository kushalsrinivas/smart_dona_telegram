import os


class UserClass:
    def __init__(self):
        self.userid = None

    def checkUser(self, update, context):
        if self.userid is None:
            update.message.reply_text('send your login at app.smartdonna.com and update your userID using /setUserID')
            return False
        else:
            return True

    def setUserID(self, userID):
        self.userid = userID

    def getUserID(self):
        return self.userid


User = UserClass()
