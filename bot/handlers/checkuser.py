import os
def checkUser(update , context):
    if os.getenv("userId") is None:
        print(os.getenv("userId"))
        update.message.reply_text('send your login at app.smartdonna.com and update your userID using /setUserID')
        return False
    else :
        print(os.getenv("userId"))
        return True

