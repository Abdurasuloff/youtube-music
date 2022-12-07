from youtube_search import YoutubeSearch
import requests
import json


url = "https://ytstream-download-youtube-videos.p.rapidapi.com/dl"
headers = {
  "X-RapidAPI-Key": "fc59484b9bmsh9e243ddc5a3037ep1cc60ajsn4df3798ccd71",
  "X-RapidAPI-Host": "ytstream-download-youtube-videos.p.rapidapi.com"
}

def search(query):
    results = YoutubeSearch(query, max_results=10).to_dict()
    return results


def download_audio(id):
    querystring = {"id":id}
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    music = ''
    if data['status']=="OK":
        music = data['adaptiveFormats'][-3]['url']

    return music   


