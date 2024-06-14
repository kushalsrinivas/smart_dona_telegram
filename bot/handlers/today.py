from .FetchAndSend import fetchAndSend
from datetime import datetime, timedelta
from .checkuser import User
def today(update, context):
    """
    /hello
    just say hello and reply
    """
    if User.checkUser(update,context):
        print("user id is set :",User.getUserID())
        today = datetime.now().date()
        # Get yesterday's date
        yesterday = today - timedelta(days=1)

        # Format dates in ISO format (YYYY-MM-DD)
        start_date = yesterday.isoformat()
        end_date = today.isoformat()
        fetchAndSend(update,context,start_date,end_date)

