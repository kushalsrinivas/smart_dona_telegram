def whoami(update, context):
    user = update.message.from_user
    first_name = user.first_name
    last_name = user.last_name
    username = user.username
    userid = user.id

    name = "<b>"+first_name +"</b>"
    if last_name:
        name += " <b>"+last_name + "</b>"
    if username:
        name += "\n🤗 @"+username

    text = "You are:\n👤 {}\n🆔 {}".format(name, str(user.id))

    if 'group' in update.message.chat.type:
        text += "\n👥 " +update.message.chat.title

    update.message.reply_text(text, parse_mode='HTML')