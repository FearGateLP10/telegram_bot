import datetime
import ephem
from glob import glob
import logging
from random import choice

from utils import get_user_emo, get_keyboard


def greet_user(bot, update, user_data):
    emo = get_user_emo(user_data)
    user_data['emo'] = emo
    text = 'Привет {}'.format(emo)
    logging.info(text)
    update.message.reply_text(text, reply_markup=get_keyboard())


def get_planet(bot, update, user_data):
    text = 'Вызван /ephem'
    logging.info(text)
    try:
        planet_name = update.message.text.split()[1]
        date = datetime.datetime.now()
        ephem_planet = getattr(ephem, planet_name)(datetime.datetime.now().strftime('%Y/%m/%d'))    # (datetime.datetime.today())
        update.message.reply_text(planet_name)
        update.message.reply_text(ephem.constellation(ephem_planet))
    except AttributeError:
        text_except = ('Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Phobos', 'Deimos', 'Jupiter', 'Io', 'Europa', 
            'Ganymede', 'Callisto', 'Saturn', 'Mimas', 'Enceladus', 'Tethys', 'Dione', 'Rhea', 'Titan', 'Hyperion', 
            'Iapetus', 'Uranus', 'Ariel', 'Umbriel', 'Titania', 'Oberon', 'Miranda', 'Neptune', 'Pluto'
            )
        update.message.reply_text('Введите название планеты из списка: {}'.format(text_except), reply_markup=get_keyboard())


def talk_to_me(bot, update, user_data):
    emo = get_user_emo(user_data)
    user_text = 'Привет, {} {}! Ты написал {}'.format(update.message.chat.first_name, emo, update.message.text)
    logging.info('User: {}, Chat id: {}, message: {}'.format(update.message.chat.username, 
                                                            update.message.chat.id, update.message.text))
    update.message.reply_text(user_text, reply_markup=get_keyboard())


def send_cat_picture(bot, update, user_data):
    update.message.reply_text('Держи котика!', reply_markup=get_keyboard())
    cat_list = glob('images/cat*.jpg')
    cat_pic = choice(cat_list)
    bot.send_photo(chat_id=update.message.chat.id, photo=open(cat_pic, 'rb'))


def change_avatar(bot, update, user_data):
    if 'emo' in user_data:
        del user_data['emo']
    emo = get_user_emo(user_data)
    update.message.reply_text('Готово: {}'.format(emo), reply_markup=get_keyboard())


def get_contact(bot, update, user_data):
    print(update.message.contact)
    update.message.reply_text('Спасибо {}'.format(get_user_emo(user_data)), reply_markup=get_keyboard())


def get_location(bot, update, user_data):
    print(update.message.location)
    update.message.reply_text('Спасибо {}'.format(get_user_emo(user_data)), reply_markup=get_keyboard())
