import logging
from aiogram import Bot, Dispatcher, executor, types
from api import search, download_audio
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters  import Text
from aiogram.dispatcher.filters.builtin import CallbackQuery
from io import BytesIO
from pytube import YouTube
from aiogram.types.input_file import InputFile
import os


API_TOKEN = '5928153110:AAE4DaH_UyEBk3lK0ym6-nLRN-rT17tllGU'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum. \nMen sizga xar-hil podkastlarni yuklab olishingizga yordam beraman. \nKalit so'zni kiriting. Masalan: Shukurulloh domla , Ota-Ona haqida masalalar. \nDasturchi: @Abdura5u10ff")




@dp.message_handler()
async def echo(message: types.Message):
    result = search(message.text)
    index = 0
    await message.answer("Kalit so'z bo'yicha qidiruvlar")
    for i in result:
        index += 1
        btn =  InlineKeyboardMarkup(
            inline_keyboard=[ 
                                [
                                    InlineKeyboardButton(text="Audioni yuklash", callback_data=f"📥{i['id']}")
                                ]
                             ]
        )
        await message.answer(str(index)+". " + "https://youtube.com"+i['url_suffix'], reply_markup=btn)
       
        
    


@dp.callback_query_handler(Text(startswith="📥"))
async def send_audio(call:CallbackQuery):
    pre  = await  call.message.answer('Yuklanmoqda. Bu bir oz vaqt olishi mumkin...') 
    id = call.data[1:]
    link = "https://www.youtube.com/watch?v="+id
    print(link)
    url = YouTube(link)
    t = url.streams.get_audio_only()
    path = t.download('static/')
    await call.message.reply_audio(audio=InputFile(path), caption=url.title)
    os.remove(path)
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)