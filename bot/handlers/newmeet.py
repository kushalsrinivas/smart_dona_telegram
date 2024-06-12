
def newmeet(update, context):
    """
    /newmeet {meeting link}:

    """
    from .index import index
    text = f'<b>New Meeting Link:{"lsdksl"} </b>\n'
    for k, v in index().items():
        text += v.__doc__
    update.message.reply_text(text, parse_mode='HTML')
