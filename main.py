import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from translate import Translator
def send_some_msg(id, some_text):
    vk_session.method("messages.send", {"user_id":id, "message":some_text,"random_id":0})

qes = input('Введите 1 для перевода в сообществе (online) | или 2 для превода в консоли (offline)')
print('Введите язык ввода/перевода:\n----------------------------------\n ·Русский - ru\n ·Английский - en\n ·Французский - fr\n ·Испанский - es\n ·Корейский - ko\n ·Арабский - ar\n ·Польский - pl\n ·Китайский(традиционный) - zh-tw\n ·Казахский - kk\n ·Японсикй - ja\n ·Немецкий - de\n ·Индийский - hi\n ·Шведский - sv\n ·Таджикский - tg\n ·Африканский - af\n ·Белорусский - be\n ·Узбекский - uz\n ·Украинский - ua\n ·Вьетнамский - vi\n ·Тайский - th')
langs = ['ru', 'en', 'fr', 'es', 'ko', 'ar', 'pl', 'zh-tw', 'kk', 'ja', 'de', 'hi', 'sv', 'tg', 'af', 'be', 'uz', 'ua', 'vi', 'th']
lang_in = input('Язык ввода:')  # язык ввода

while lang_in not in langs:  # Проверка на корректность ввода
    lang_in = input('Язык ввода:')

lang_out= input('Язык перевода:')  # язык перевода

while lang_out not in langs:  # Проверка на корректность ввода
    lang_out = input('Язык перевода:')


if qes == '1':
    vk_session = vk_api.VkApi(
        token="vk1.a.O3lK33axSxY2-Mvb_kyGr91uyUbrDKex8eKkeoY_6esgufNr0rAV0_6FnhIemyTTOz8d5x5suAbp4a6dpNOVZ3EjamHVdDxZVSTQxPR357jh9NQ9duzeCY-fm3D6piW_DfWyQZcHcuQrmGlaWhMqxI0Q7Uwd47I0MwnhTXrGGo3KiKWGRJfOmY3-Fyj8efKv7yPNe5kQUH6ZyGkeHNnE5A")
    session_api = vk_session.get_api()
    longpool = VkLongPoll(vk_session)

    for event in longpool.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                msg = event.text.lower()
                id = event.user_id
                if msg != '':
                    translator = Translator(from_lang=lang_in, to_lang=lang_out)
                    translation = translator.translate(msg)
                    send_some_msg(id, translation)
else:
    msg = input('Введите сообщение:')
    while msg != '0':
        translator = Translator(from_lang=lang_in, to_lang=lang_out)
        translation = translator.translate(msg)
        print(translation)
        msg = input('Введите сообщение:')