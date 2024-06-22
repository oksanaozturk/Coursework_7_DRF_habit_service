import requests
from django.conf import settings


def send_tg_message(telegram_id, message):
    """
    Функция отправки сообщения в Телеграмм-бот.
    :param telegram_id: id чата с пользователем в Telegram
    :param message: сообщение, которое будет отправлено пользователю
    :return:
    """
    params = {
        "text": message,
        "chat_id": telegram_id,
    }
    response = requests.post(
        f"{settings.TELEGRAM_URL}{settings.BOT_TOKEN}/sendMessage", params=params
    )
    print(response.json())
    response_data = response.json()
    if not response_data.get("ok"):
        print(f"Ошибка отправки: {response_data}")
    return response_data
