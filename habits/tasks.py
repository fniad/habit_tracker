from celery import shared_task
import datetime

from habits.models import Habit
from habits.services import calculate_next_send_date, check_if_message_should_be_sent, update_last_updated, \
    send_message_tg
import logging

logger = logging.getLogger(__name__)


@shared_task
def send_message_tg_if_due():
    """ Функция для отправки сообщения в телеграмм """
    logger.info('Начало работы рассылки.')
    habits = Habit.objects.filter()
    logger.info(f'Привычки: {habits}')
    for habit in habits:
        time = habit.time
        periodicity = habit.periodicity
        last_updated = habit.last_updated
        current_date = datetime.datetime.now()
        next_send_date = calculate_next_send_date(last_updated, periodicity, time)
        if check_if_message_should_be_sent(current_date, next_send_date):
            send_message_tg(habit.user.chat_id, habit.habit_text)
            logger.info(f'Сообщение для привычки {habit.action} отправлено.')
            update_last_updated(current_date, habit.pk)
            logger.info(f'Дата обновлена у привычки {habit.action}')
    logger.info('Рассылка завершена.')
