import requests
from datetime import datetime, timedelta
from .FetchAndSend import fetchAndSend
from .checkuser import checkUser

def onemonth(update, context):
    """
    /hello
    just say hello and reply
    """
    if checkUser(update , context):
        today = datetime.now().date()
        # Get yesterday's date
        yesterday = today - timedelta(days=31)

        # Format dates in ISO format (YYYY-MM-DD)
        start_date = yesterday.isoformat()
        end_date = today.isoformat()
        fetchAndSend(update,context,start_date,end_date)