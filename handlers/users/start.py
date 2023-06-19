from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from instagramdownloader import insta
from tiktokdownloader import tiktok
from loader import dp
from aiogram.dispatcher.filters import Text


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")


@dp.message_handler(Text(startswith='https://www.instagram.com'))
async def test(message: types.Message):
    url = message.text
    result = insta(url)
    if result['type'] == 'error':
        await message.answer("Uzur buhavola bilan Malumot topilmadi")
    if result['type'] == 'video':
        await message.answer_video(video=result['media'], caption=url)
    if result['type'] == 'image':
        await message.answer_photo(photo=result['media'], caption=url)
    if result['type'] == 'carousel':
        for i in result['media']:
            await message.answer_document(document=i, caption=url)


@dp.message_handler(Text(startswith='https://www.tiktok.com'))
async def test(message: types.Message):
    link = message.text
    result = tiktok(link)
    if result['media'] == 'error':
        await message.answer("Uzur buhavola bilan Malumot topilmadi")
    else:
        await message.answer_video(result['media'])


@dp.message_handler(Text(startswith='https://vt.tiktok.com'))
async def test(message: types.Message):
    link = message.text
    result = tiktok(link)
    if result['media'] == 'error':
        await message.answer("Uzur buhavola bilan Malumot topilmadi")
    else:
        await message.answer_video(result['media'])
