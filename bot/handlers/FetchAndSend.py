import requests
from telegram import  ParseMode
import os
from .checkuser import User
def fetchAndSend(update, context , start_date , end_date):
    print("from fetch and send : "+User.getUserID())
    data = getMeetingInstance(User.getUserID(),start_date,end_date)
    print(data)
    for instance in data['data']:
        try:
            callInstanceID = instance['callInstanceId']
            meetingInfo = getMeetingInfo(callInstanceID)
            thumbnail = meetingInfo['data'][0]['host_image']
            speakers = meetingInfo['data'][0]['speakers']
            speaker_name = [speaker['name'] for speaker in speakers]
            recording = meetingInfo['data'][0]['recordings'][0]['recorded_video_url']

            try:
                actionItems = "\n".join([f"• {actionitem['action_item']}" for actionitem in
                                       meetingInfo['data'][0]['summary']['action_items2']])
                tldr = meetingInfo['data'][0]['summary']['tldr'][1]
            except Exception as e:
                actionItems = "N/A (try again after sometime)"
                tldr = "N/A (try again after sometime)"

            context.bot.send_video(chat_id=update.message.chat_id, video=recording)
            context.bot.send_photo(chat_id=update.message.chat_id, photo=thumbnail)
            update.message.reply_text(
                "<b>SPEAKERS</b>\n"
                "{}\n\n"
                "<b>ACTION ITEMS</b>\n"
                "{}\n\n"
                "<b>TL;DR</b>\n"
                "{}"
                .format(" ,".join(speaker_name[2:]), actionItems, tldr),parse_mode=ParseMode.HTML,
                )

        except Exception as e:
            print(e)
            pass

def talk_to_ai(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="You clicked: Talk to AI")
def getMeetingInstance(currentUserId,start_date,end_date):
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
    url = "https://api.goodmeetings.ai/v2/call/get-meeting-instance-info?callInstanceId=" + callInstanceID
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
