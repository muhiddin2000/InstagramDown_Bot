import requests
import json


def tiktok(link):
    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "d07b8dbf6bmsh873b8e48b1c7157p1377e6jsnc2c5230dba74",
        "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = {}
    if response.status_code == 200:
        rest = json.loads(response.text)

        data['media'] = rest['video'][0]
        data['music'] = rest['music'][0]
        return data
    else:
        data['media'] = 'error'
        return data
