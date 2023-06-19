import requests
import json


def insta(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"
    querystring = {"url": link}
    headers = {
        "X-RapidAPI-Key": "d07b8dbf6bmsh873b8e48b1c7157p1377e6jsnc2c5230dba74",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)

    rest = json.loads(response.text)
    data = {}

    if rest['Type'] == 'Post-Video':
        data['media'] = rest['media']
        data['type'] = 'video'
    elif rest['Type'] == 'Carousel':
        data['media'] = rest['media']
        data['type'] = 'carousel'
    elif rest['Type'] == 'Post-Images':
        data['media'] = rest['media']
        data['type'] = 'image'
    else:
        data['type'] = 'error'
    return data


# insta('https://www.instagram.com/p/CXogAGgMg8j/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA==')
