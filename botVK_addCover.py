
import vk_api
import datetime
import time
import setings
import requests
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from vk_api import VkUpload 
from PIL import Image, ImageDraw, ImageFont

# vk token
vk_session = vk_api.VkApi(token = setings.vkMTFapi)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

# Настройка шрифтов
font = ImageFont.truetype('9622.ttf', size = 30)
fontWeek = ImageFont.truetype('ArialRoundedMTProCyr-Bold.otf', size = 35) 

while True:
    # Настройка счетчика 
    dateNow = datetime.datetime.now()
    dateThen = datetime.datetime(2020, 10, 30, 0, 00, 0)
    timer = dateThen - dateNow
    timerSecond = timer.total_seconds()
    timerMinute = (timerSecond % 3600) // 60
    timerHour = (timerSecond % 86400) // 3600
    parityWeek = "Числитель" if datetime.datetime.now().isocalendar()[1] % 2 == 0 else "Знаменатель"
    getTimer = "{}д.  {}ч.  {}мин.".format(timer.days, round(timerHour), round(timerMinute))

    im = Image.open('/Users/igorgerasimov/Desktop/Python/DdKGTA/Cover/coverMTF.jpg')
    draw_text = ImageDraw.Draw(im)

    draw_text.text(
        (196, 321),
        'До стипендии осталось :',
        # Добавляем шрифт к изображению
        font = font,
        fill = (255,255,255,128))

    draw_text.text(
        (1038, 321),
        getTimer,
        font = font,
        fill = (255,255,255,128))

    draw_text.text(
        (549, 142),
        'Эта неделя : ',
        font = font,
        fill = (255,255,255,128))

    draw_text.text(
        (550, 200),
        parityWeek,
        font = fontWeek,
        fill = (255,255,255,128))

    im.save('coverMTF2.jpg')
    print("Сохранение фото")
    # a = vk.photos.getOwnerCoverPhotoUploadServer(photo = 'coverMTF2.jpg', # DdKGTA group
    #                                              group_id = 194390511, 
    #                                              crop_x = 1, 
    #                                              crop_y = 1,
    #                                              crop_x2 = 1499, 
    #                                              crop_y2 = 378)
    a = vk.photos.getOwnerCoverPhotoUploadServer(photo = 'coverMTF2.jpg', 
                                                group_id = 16035652, # MTF group
                                                crop_x = 1, 
                                                crop_y = 1,
                                                crop_x2 = 1499, 
                                                crop_y2 = 378)
    print ('Получение ссылки ...')

    img = {'photo': ('coverMTF2.jpg', open(r'coverMTF2.jpg', 'rb'))}
    print("Получение положения фото")

    reg = requests.post(a['upload_url'], files = img)
    v = reg.json()

    print ("Загрузка фото")
    a = vk.photos.saveOwnerCoverPhoto(hash = v['hash'], photo = v['photo'])
    time.sleep(90)
    # im.show()

