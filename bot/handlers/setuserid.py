import os
from .checkuser import User


def setUserID(update , context) :
    if User.getUserID() is not None:
        update.message.reply_text(
            'user id is already set use /logout and then set a new userID')
    else :
        user = update.message.from_user
        userID = update.message.text
        User.setUserID(userID.split(" ")[1])
        update.message.reply_text(
            'user id set to '+User.getUserID())
