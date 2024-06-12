import requests
from datetime import datetime, timedelta

def oneweek(update, context):
    """
    /hello
    just say hello and reply
    """
    user = update.message.from_user
    data = getMeetingInstance(user.id)
    callInstanceID= data['data'][0]['callInstanceId']
    for instance in data['data']:
        callInstanceID = instance['callInstanceId']
        meetingInfo = getMeetingInfo(callInstanceID)
        # transcription = getTranscription(callInstanceID)
        # transcription  = " ".join([""+item['text'] for item in transcription['data']])
        thumbnail =meetingInfo['data'][0]['host_image']
        speakers = meetingInfo['data'][0]['speakers']
        speaker_name = [speaker['name'] for speaker in speakers]
        recording  = meetingInfo['data'][0]['recordings'][0]['recorded_video_url']
        actionItems = "".join([f"\n {actionitem['action_item']} " for actionitem in meetingInfo['data'][0]['summary']['action_items2']])
        tldr = meetingInfo['data'][0]['summary']['tldr'][1]

        context.bot.send_video(chat_id=update.message.chat_id, video=recording)
        context.bot.send_photo(chat_id=update.message.chat_id, photo =thumbnail)
        update.message.reply_text(
            "*SPEAKERS*\n"
            "{}\n\n"
            "*ACTION ITEMS*\n"
            "{}\n\n"
            "*TL;DR*\n"
            "{}"
            .format(" ,".join(speaker_name[2:]),actionItems,tldr))
def getMeetingInstance(currentUserId):
    today = datetime.now().date()
    # Get yesterday's date
    yesterday = today - timedelta(days=31)

    # Format dates in ISO format (YYYY-MM-DD)
    start_date = yesterday.isoformat()
    end_date = today.isoformat()
    url = "https://api.goodmeetings.ai/v2/call/search-recording-based-client-email"
    payload = {
    "start_date": start_date,
    "end_date": end_date,
    "client_client_id": currentUserId
}
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NjU0MmYwZjU0Yjg4MjAwMGU0NzE0ZDQiLCJpYXQiOjE3MTY4MTA0NTQsImV4cCI6MTc0ODM0NjQ1NCwidHlwZSI6ImFjY2VzcyJ9.OQLGGqS4jShahdC3wTaJ5yj4g4MYkeXv-jBXi-AD1sM"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def getMeetingInfo(callInstanceID):
    url = "https://api.goodmeetings.ai/v2/call/get-meeting-instance-info?callInstanceId="+callInstanceID
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NjU0MmYwZjU0Yjg4MjAwMGU0NzE0ZDQiLCJpYXQiOjE3MTY4MTA0NTQsImV4cCI6MTc0ODM0NjQ1NCwidHlwZSI6ImFjY2VzcyJ9.OQLGGqS4jShahdC3wTaJ5yj4g4MYkeXv-jBXi-AD1sM"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


def getTranscription(callInstanceID):
    url = "https://api.goodmeetings.ai/v2/transcript/get?callInstanceId=" + callInstanceID
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NjU0MmYwZjU0Yjg4MjAwMGU0NzE0ZDQiLCJpYXQiOjE3MTY4MTA0NTQsImV4cCI6MTc0ODM0NjQ1NCwidHlwZSI6ImFjY2VzcyJ9.OQLGGqS4jShahdC3wTaJ5yj4g4MYkeXv-jBXi-AD1sM"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()