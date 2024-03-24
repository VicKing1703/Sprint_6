from datetime import date


class Data:

    # URL-адрес
    URL_SCOOTER = 'https://qa-scooter.praktikum-services.ru/'
    URL_DZEN = 'https://dzen.ru/'

    # Разрешение окна
    WINDIW_SIZE = '--window-size=1920,1080'  # для Chrome
    WINDIW_SIZE = 'start-maximized'  # для Firefox

    # Имя и фамилия
    NAME = 'Иван'
    SURNAME = 'Петров'

    # Адрес
    ADDRESS = 'ул. Тверская, д. 5'

    # Станция метро
    METRO_STATION = 'Тверская'

    # Телефон
    PHONE = '+79998887766'

    # Комментарий
    COMMENT = 'Какой-то комментарий'

    # Дата
    CURRENT_DATE = date.today()
