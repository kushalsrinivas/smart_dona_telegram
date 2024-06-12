import requests


def join(update, context):
    """
    /hello
    just say hello and reply
    """
    user = update.message.from_user
    url = update.message.text
    data = join_meeting(url ,user.id)
    update.message.reply_text(
        'joining  {} in a few moments'.format(update.message.text))


def join_meeting(meeting_url, client_client_id, ):
    url = "https://api.goodmeetings.ai/v2/call/join"
    payload = {
        "meetingUrl": meeting_url,
        "botName": "Smart Donna Ai",
        "client_client_id": client_client_id,
        "workspace": "Smart_donna"
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
