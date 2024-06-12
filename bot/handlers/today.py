from .FetchAndSend import fetchAndSend
from datetime import datetime, timedelta

def today(update, context):
    """
    /hello
    just say hello and reply
    """
    today = datetime.now().date()
    # Get yesterday's date
    yesterday = today - timedelta(days=1)

    # Format dates in ISO format (YYYY-MM-DD)
    start_date = yesterday.isoformat()
    end_date = today.isoformat()
    fetchAndSend(update,context,start_date,end_date)

