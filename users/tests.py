from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from users.models import User


class UserTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='user',
            password='test',
            chat_id=248719216,
            is_staff=True)
        self.client.force_authenticate(user=self.user)

        self.test_user = User.objects.create_user(
            username='test',
            password='test',
            chat_id=248719216
        )

    def test_user_delete(self):
        """ Тест удаления пользователя """

        response = self.client.delete(
            f'/user/delete/{self.test_user.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_user_update(self):
        """ Тест обновления пользователя (своего профиля)"""

        data = {
            'username': 'user',
            'password': 'test',
        }

        response = self.client.put(
            f'/user/update/{self.user.id}/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_user_update_another_user(self):
        """ Тест обновления пользователя (чужого профиля)"""

        data = {
            'username': 'user',
            'password': 'test',
        }

        response = self.client.put(
            f'/user/update/{self.test_user.id}/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN   # Пользователь не является владельцем
        )

    def test_user_list(self):
        """ Тест получения списка пользователей """

        response = self.client.get(
            '/user/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_user_retrieve(self):
        """ Тест получения пользователя """

        response = self.client.get(
            f'/user/{self.user.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_user_retrieve_another_user(self):
        """ Тест получения другого пользователя """

        response = self.client.get(
            f'/user/{self.test_user.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_user_create(self):
        """ Тест создания пользователя """

        data = {
            'username': 'test23',
            'password': 'test',
        }

        response = self.client.post(
            '/user/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def tearDown(self):
        User.objects.all().delete()
        super().tearDown()
