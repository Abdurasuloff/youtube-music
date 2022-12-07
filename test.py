# import pywhatkit as pwt
# print(pwt.playonyt('Shokir qori'))



from youtube_search import YoutubeSearch

# results = YoutubeSearch('shokir qori', max_results=1).to_dict()


import requests
import json

# import requests

url = "https://ytstream-download-youtube-videos.p.rapidapi.com/dl"
headers = {
  "X-RapidAPI-Key": "fc59484b9bmsh9e243ddc5a3037ep1cc60ajsn4df3798ccd71",
  "X-RapidAPI-Host": "ytstream-download-youtube-videos.p.rapidapi.com"
}






def find_podcasts(query):
    results = YoutubeSearch(query, max_results=10).to_dict()
    ytid = str(results)
    print(ytid)
    # querystring = {"id":ytid}
    # response = requests.request("GET", url, headers=headers, params=querystring)
    # data = json.loads(response.text)
    # if data['status']=="OK":
    #     music = data['adaptiveFormats'][-3]['url']
    #     print(music)



find_podcasts('counting stars')


# @dp.callback_query_handler(Text(startswith="📥"))
# async def send_audio(call:CallbackQuery):
#     await call.message.answer('Yuklanmoqda...') 
#     await call.answer(cache_time=60)    
#     id = call.data[1:]
#     link = "https://www.youtube.com/watch?v="+id
#     buffer = BytesIO()
#     url = YouTube(link)
#     if url.check_availability() is None:
#         filename=url.title
#         audio = url.streams.get_audio_only()
#         audio.stream_to_buffer( buffer=buffer)
#         buffer.seek(0)
        
#         await call.message.answer_audio(audio=buffer, caption=filename)
#     else:
#         await call.message.answer('Nimadir xato ketti.') 
