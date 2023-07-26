import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import parser_for_bot

API_TOKEN = '5997815252:AAHf7IQTv_FR7x2Emt5FiEKlKLa5fBljutE'


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
now_keyboard = None


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    global now_keyboard
    now_keyboard = None
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text='Компьютерная безопасность')
    keyboard.add(button_1)
    await message.answer("Привет!\nЗдесь вы узнаете на каком месте Кирилл на своих специальностях в мирэа!",
                         reply_markup=keyboard)


@dp.message_handler(Text(equals="Компьютерная безопасность"))
async def komp_bez(message: types.Message):
    global now_keyboard
    now_keyboard = 'Компьютерная безопасность'
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text='ВП по оригиналам')
    button_2 = types.KeyboardButton(text='Если Кирилл подаст оригинал')
    button_3 = types.KeyboardButton(text='/start')
    keyboard.add(button_1, button_2, button_3)
    await message.answer("Вы выбрали специальность компьютерная безопасность\n Теперь вы можете выбрать два варианта:\n"
                         "1) ВП по оригиналам - топ все подавших, которые проходят в бюджетные места\n"
                         "2) Если кирилл подаст оригинал - напишет номер места или выведет не проходит",
                         reply_markup=keyboard)


@dp.message_handler(Text(equals="ВП по оригиналам"))
async def vp_po_orig(message: types.Message):
    global now_keyboard
    if now_keyboard == 'Компьютерная безопасность':
        conc = parser_for_bot.pars(
            'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1748205531612323126&prior=any&documentType=any&accepted=0&onlyHPAll=0&onlyHPfirst=1&acceptedEntrant=any&onlyActive=1&onlyPaid=0')
        result = ''
        result += ' '.join(conc[0]) + '\n'
        for i in range(1, len(conc)):
            result += ' '.join(conc[i]) + '\n'
        await message.answer(result)


@dp.message_handler(Text(equals="Если Кирилл подаст оригинал"))
async def if_kirill(message: types.Message):
    global now_keyboard
    if now_keyboard == 'Компьютерная безопасность':
        conc = parser_for_bot.pars(
            'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1748205531612323126&prior=any&documentType=any&accepted=0&onlyHPAll=0&onlyHPfirst=1&acceptedEntrant=any&onlyActive=1&onlyPaid=0')
        result = 0
        for i in range(1, len(conc)):
            if int(conc[i][3]) <= 249:
                result = int(conc[i][0])
                break
        await message.answer(f'На специальности {now_keyboard}, если Кирилл подаст оригинал, то он будет на {result} месте')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
