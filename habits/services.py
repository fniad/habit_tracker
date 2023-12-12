import datetime

from django.conf import settings
import requests
from habits.models import Habit


def calculate_next_send_date(last_updated, periodicity, time):
    """ Функция для расчета даты следующего отправления """
    next_send_date = (last_updated + datetime.timedelta(days=periodicity))
    combined_datetime = datetime.datetime.combine(next_send_date, time)
    return combined_datetime


def check_if_message_should_be_sent(current_date, next_send_date):
    """ Функция для проверки, нужно ли отправлять сообщение на сегодняшнюю дату """
    return current_date >= next_send_date


def update_last_updated(current_date, pk):
    """ Функция для обновления даты последнего обновления """
    habit = Habit.objects.get(id=pk)
    habit.last_updated = current_date
    habit.save()


def send_message_tg(chat_id, text):
    """ Функция для отправки сообщения в телеграмм """
    url = f"https://api.telegram.org/bot{settings.TOKEN_TG_CHAT_BOT}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
