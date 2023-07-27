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
    button_2 = types.KeyboardButton(text='Безопасность информационных технологий в правоохранительной сфере')
    button_3 = types.KeyboardButton(text='Информационная безопасность')
    button_4 = types.KeyboardButton(text='Информационная безопасность автоматизированных систем')
    button_5 = types.KeyboardButton(text='Прикладная информатика')
    keyboard.add(button_1, button_2, button_3, button_4, button_5)
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
    await message.answer(f"Вы выбрали специальность '{now_keyboard}'\n Теперь вы можете выбрать два варианта:\n"
                         "1) ВП по оригиналам - топ все подавших(размер соответствует количеству бюджетных мест), которые проходят в бюджетные места\n"
                         "2) Если кирилл подаст оригинал - напишет номер места или выведет 0 (что значит не я не прохожу)",
                         reply_markup=keyboard)

@dp.message_handler(Text(equals="Безопасность информационных технологий в правоохранительной сфере"))
async def ohr_bez(message: types.Message):
    global now_keyboard
    now_keyboard = 'Безопасность информационных технологий в правоохранительной сфере'
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text='ВП по оригиналам')
    button_2 = types.KeyboardButton(text='Если Кирилл подаст оригинал')
    button_3 = types.KeyboardButton(text='/start')
    keyboard.add(button_1, button_2, button_3)
    await message.answer(f"Вы выбрали специальность '{now_keyboard}'\n Теперь вы можете выбрать два варианта:\n"
                         "1) ВП по оригиналам - топ все подавших(размер соответствует количеству бюджетных мест; иногда может неккоректно выводиться, ибо слишком много бюджетных мест), которые проходят в бюджетные места\n"
                         "2) Если кирилл подаст оригинал - напишет номер места или выведет 0 (что значит не я не прохожу)",
                         reply_markup=keyboard)

@dp.message_handler(Text(equals="Информационная безопасность"))
async def inf_bez(message: types.Message):
    global now_keyboard
    now_keyboard = 'Информационная безопасность'
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text='ВП по оригиналам')
    button_2 = types.KeyboardButton(text='Если Кирилл подаст оригинал')
    button_3 = types.KeyboardButton(text='/start')
    keyboard.add(button_1, button_2, button_3)
    await message.answer(f"Вы выбрали специальность '{now_keyboard}'\n Теперь вы можете выбрать два варианта:\n"
                         "1) ВП по оригиналам - топ все подавших(размер соответствует количеству бюджетных мест; иногда может неккоректно выводиться, ибо слишком много бюджетных мест), которые проходят в бюджетные места\n"
                         "2) Если кирилл подаст оригинал - напишет номер места или выведет 0 (что значит не я не прохожу)",
                         reply_markup=keyboard)

@dp.message_handler(Text(equals="Информационная безопасность автоматизированных систем"))
async def avt_bez(message: types.Message):
    global now_keyboard
    now_keyboard = 'Информационная безопасность автоматизированных систем'
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text='ВП по оригиналам')
    button_2 = types.KeyboardButton(text='Если Кирилл подаст оригинал')
    button_3 = types.KeyboardButton(text='/start')
    keyboard.add(button_1, button_2, button_3)
    await message.answer(f"Вы выбрали специальность '{now_keyboard}'\n Теперь вы можете выбрать два варианта:\n"
                         "1) ВП по оригиналам - топ все подавших(размер соответствует количеству бюджетных мест; иногда может неккоректно выводиться, ибо слишком много бюджетных мест), которые проходят в бюджетные места\n"
                         "2) Если кирилл подаст оригинал - напишет номер места или выведет 0 (что значит не я не прохожу)",
                         reply_markup=keyboard)

@dp.message_handler(Text(equals="Прикладная информатика"))
async def prikl(message: types.Message):
    global now_keyboard
    now_keyboard = 'Прикладная информатика'
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text='ВП по оригиналам')
    button_2 = types.KeyboardButton(text='Если Кирилл подаст оригинал')
    button_3 = types.KeyboardButton(text='/start')
    keyboard.add(button_1, button_2, button_3)
    await message.answer(f"Вы выбрали специальность '{now_keyboard}'\n Теперь вы можете выбрать два варианта:\n"
                         "1) ВП по оригиналам - топ все подавших(размер соответствует количеству бюджетных мест, кроме прикладной информатики(на нее 129), но выводит не всех), которые проходят в бюджетные места\n"
                         "2) Если кирилл подаст оригинал - напишет номер места или выведет 0 (что значит не я не прохожу)",
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
    elif now_keyboard == 'Безопасность информационных технологий в правоохранительной сфере':
        conc = parser_for_bot.pars('https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1748205515758902582&prior=any&documentType=any&accepted=0&onlyHPAll=0&onlyHPfirst=1&acceptedEntrant=any&onlyActive=1&onlyPaid=0')
        result = ''
        result += ' '.join(conc[0]) + '\n'
        for i in range(1, len(conc)):
            result += ' '.join(conc[i]) + '\n'
        await message.answer(result)
    elif now_keyboard == 'Информационная безопасность':
        conc = parser_for_bot.pars('https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1748205535757344054&prior=any&documentType=any&accepted=0&onlyHPAll=0&onlyHPfirst=1&acceptedEntrant=any&onlyActive=1&onlyPaid=0')
        result = ''
        result += ' '.join(conc[0]) + '\n'
        for i in range(1, len(conc)):
            result += ' '.join(conc[i]) + '\n'
        await message.answer(result)
    elif now_keyboard == 'Информационная безопасность автоматизированных систем':
        conc = parser_for_bot.pars('https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1748205522704670006&prior=any&documentType=any&accepted=0&onlyHPAll=0&onlyHPfirst=1&acceptedEntrant=any&onlyActive=1&onlyPaid=0')
        result = ''
        result += ' '.join(conc[0]) + '\n'
        for i in range(1, len(conc)):
            result += ' '.join(conc[i]) + '\n'
        await message.answer(result)
    elif now_keyboard == 'Прикладная информатика':
        conc = parser_for_bot.pars('https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1748205428624334134&prior=any&documentType=any&accepted=0&onlyHPAll=0&onlyHPfirst=1&acceptedEntrant=any&onlyActive=1&onlyPaid=0')
        result = ''
        result += ' '.join(conc[0]) + '\n'
        for i in range(1, 31):
            result += ' '.join(conc[i]) + '\n'
        await message.answer(result)
    elif now_keyboard is None:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton(text='Компьютерная безопасность')
        button_2 = types.KeyboardButton(text='Безопасность информационных технологий в правоохранительной сфере')
        button_3 = types.KeyboardButton(text='Информационная безопасность')
        button_4 = types.KeyboardButton(text='Информационная безопасность автоматизированных систем')
        button_5 = types.KeyboardButton(text='Прикладная информатика')
        keyboard.add(button_1, button_2, button_3, button_4, button_5)
        await message.answer("Привет!\nЗдесь вы узнаете на каком месте Кирилл на своих специальностях в мирэа!",
                             reply_markup=keyboard)


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
    elif now_keyboard == 'Безопасность информационных технологий в правоохранительной сфере':
        conc = parser_for_bot.pars(
            'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1748205515758902582&prior=any&documentType=any&accepted=0&onlyHPAll=0&onlyHPfirst=1&acceptedEntrant=any&onlyActive=1&onlyPaid=0')
        result = 0
        for i in range(1, len(conc)):
            if int(conc[i][3]) <= 249:
                result = int(conc[i][0])
                break
        await message.answer(
            f'На специальности {now_keyboard}, если Кирилл подаст оригинал, то он будет на {result} месте')
    elif now_keyboard == 'Информационная безопасность':
        conc = parser_for_bot.pars(
            'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1748205535757344054&prior=any&documentType=any&accepted=0&onlyHPAll=0&onlyHPfirst=1&acceptedEntrant=any&onlyActive=1&onlyPaid=0')
        result = 0
        for i in range(1, len(conc)):
            if int(conc[i][3]) <= 249:
                result = int(conc[i][0])
                break
        await message.answer(
            f'На специальности {now_keyboard}, если Кирилл подаст оригинал, то он будет на {result} месте')
    elif now_keyboard == 'Информационная безопасность автоматизированных систем':
        conc = parser_for_bot.pars(
            'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1748205522704670006&prior=any&documentType=any&accepted=0&onlyHPAll=0&onlyHPfirst=1&acceptedEntrant=any&onlyActive=1&onlyPaid=0')
        result = 0
        for i in range(1, len(conc)):
            if int(conc[i][3]) <= 249:
                result = int(conc[i][0])
                break
        await message.answer(
            f'На специальности {now_keyboard}, если Кирилл подаст оригинал, то он будет на {result} месте')
    elif now_keyboard == 'Прикладная информатика':
        conc = parser_for_bot.pars(
            'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1748205428624334134&prior=any&documentType=any&accepted=0&onlyHPAll=0&onlyHPfirst=1&acceptedEntrant=any&onlyActive=1&onlyPaid=0')
        result = 0
        for i in range(1, len(conc)):
            if int(conc[i][3]) <= 249:
                result = int(conc[i][0])
                break
        await message.answer(
            f'На специальности {now_keyboard}, если Кирилл подаст оригинал, то он будет на {result} месте')
    elif now_keyboard is None:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton(text='Компьютерная безопасность')
        button_2 = types.KeyboardButton(text='Безопасность информационных технологий в правоохранительной сфере')
        button_3 = types.KeyboardButton(text='Информационная безопасность')
        button_4 = types.KeyboardButton(text='Информационная безопасность автоматизированных систем')
        button_5 = types.KeyboardButton(text='Прикладная информатика')
        keyboard.add(button_1, button_2, button_3, button_4, button_5)
        await message.answer("Привет!\nЗдесь вы узнаете на каком месте Кирилл на своих специальностях в мирэа!",
                             reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
