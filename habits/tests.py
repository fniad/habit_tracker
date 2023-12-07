""" Тесты для приложения habits """

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """ Тесты для привычек """

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='user',
            password='test',
            chat_id=248719216)
        self.client.force_authenticate(user=self.user)

        self.related_habit = Habit.objects.create(
            user=self.user,
            place="Дом",
            time="12:30:00",
            duration="00:01:50",
            action="Выпить воды",
            is_pleasant=True,
            is_public=True,
            periodicity=7,
            last_updated="2023-12-06",
        )

        self.habit = Habit.objects.create(
            user=self.user,
            place="Дом",
            time="12:30:00",
            duration="00:01:50",
            action="Подтянуться 5 раз",
            related_habit=self.related_habit,
            is_pleasant=False,
            is_public=True,
            reward=None,
            periodicity=2,
            last_updated="2023-12-06",
        )

    def test_get_habit_list(self):
        """ Тест получение списка привычек """
        response = self.client.get(
            '/habit/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK, )

        self.assertEqual(response.data['count'], 2)

        self.assertEqual(
            response.json(),
            {"count": 2,
                    "next": None,
                    "previous": None,
                    "results": [
                        {'id': self.related_habit.id,
                         'user': self.user.id,
                         'place': self.related_habit.place,
                         'time': self.related_habit.time,
                         'duration': self.related_habit.duration,
                         'action': self.related_habit.action,
                         'related_habit': self.related_habit.related_habit,
                         'is_pleasant': self.related_habit.is_pleasant,
                         'is_public': self.related_habit.is_public,
                         'reward': self.related_habit.reward,
                         'periodicity': self.related_habit.periodicity,
                         'last_updated': str(self.related_habit.last_updated)},

                        {'id': self.habit.id,
                         'user': self.user.id,
                         'place': self.habit.place,
                         'time': self.habit.time,
                         'duration': self.habit.duration,
                         'action': self.habit.action,
                         'related_habit': self.habit.related_habit.id,
                         'is_pleasant': self.habit.is_pleasant,
                         'is_public': self.habit.is_public,
                         'reward': self.habit.reward,
                         'periodicity': self.habit.periodicity,
                         'last_updated': str(self.habit.last_updated)},
                    ]
             }
        )

    def test_habit_create(self):
        """ Тест создание привычки """

        data = {
            "place": "Дом",
            "time": "12:30:00",
            "duration": "PT110S",
            "action": "Подтянуться 5 раз",
            "related_habit": self.related_habit.id,
            "is_pleasant": "False",
            "is_public": "True",
            "periodicity": 2
        }

        response = self.client.post(
            '/habit/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertEqual(
            Habit.objects.all().count(),
            3
        )

    def test_habit_retrieve(self):
        """ Тест получение привычки """

        response = self.client.get(
            f'/habit/{self.habit.id}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "id": self.habit.id,
                "user": self.user.id,
                "place": self.habit.place,
                "time": self.habit.time,
                "duration": self.habit.duration,
                "action": self.habit.action,
                "related_habit": self.related_habit.id,
                "is_pleasant": self.habit.is_pleasant,
                "is_public": self.habit.is_public,
                "reward": self.habit.reward,
                "periodicity": self.habit.periodicity,
                "last_updated": str(self.habit.last_updated)
            }
        )

    def test_habit_update_patch(self):
        """ Тест обновление привычки (изменение одного поля) """

        data = {
            'place': 'Работа'
        }

        response = self.client.patch(
            f'/habit/update/{self.habit.id}/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_habit_update_put(self):
        """ Тест полного замещения привычки,
        изменение всех полей (полезная привычка и вознаграждение вместе) """

        data = {
                "id": self.habit.id,
                "user": self.user.id,
                "place": self.habit.place,
                "time": self.habit.time,
                "duration": self.habit.duration,
                "action": "Полить цветы",
                "related_habit": self.habit.related_habit.id,
                "is_pleasant": self.habit.is_pleasant,
                "is_public": self.habit.is_public,
                "reward": "Скушать финик",
                "periodicity": self.habit.periodicity,
                "last_updated": self.habit.last_updated
            }
        response = self.client.put(
            f'/habit/update/{self.habit.id}/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST     # Нельзя чтобы одновременно были и полезная привычка и вознаграждение
        )

    def test_habit_delete(self):
        """ Тест удаления привычки """

        response = self.client.delete(
            f'/habit/delete/{self.habit.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def tearDown(self):
        Habit.objects.all().delete()
        User.objects.all().delete()
        super().tearDown()
