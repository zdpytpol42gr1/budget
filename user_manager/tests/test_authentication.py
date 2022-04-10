from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.user = {
            'email': 'testemail@gmail.com',
            'username': 'username',
            'password': 'password',
            'password2': 'password2',
        }
        self.user_short_password = {
            'email': 'testemail@gmail.com',
            'username': 'username',
            'password': 'tes',
            'password2': 'tes',
        }
        self.user_not_fit_password = {
            'email': 'testemail@gmail.com',
            'username': 'username',
            'password': 'tes1',
            'password2': 'tes2',
        }
        return super().setUp()


class RegisterTest(BaseTest):

    def test_can_view_page_correctly(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'register.html')

    def test_can_register_user(self):
        response = self.client.post(self.register_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 200)

    def test_cant_register_user_with_short_password(self):
        response = self.client.post(self.register_url, self.user_short_password, format='text/html')
        self.assertEqual(response.status_code, 200)

    def test_cant_register_user_with_not_fit_password(self):
        response = self.client.post(self.register_url, self.user_not_fit_password, format='text/html')
        self.assertEqual(response.status_code, 200)


class LoginTest(BaseTest):
    def test_can_access_page(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_manager/login.html')

    def test_login_success(self):
        self.client.post(self.register_url, self.user, format='text/html')
        user = User.objects.filter(email=self.user['email']).first()
        user.is_active = True
        user.save()
        response = self.client.post(self.login_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 302)

    def test_cant_login_with_out_username(self):
        response = self.client.post(self.register_url, {'password': 'password'}, format='text/html')
        self.assertEqual(response.status_code, 401)

    def test_cant_login_with_out_password(self):
        response = self.client.post(self.register_url, {'username': 'name', 'password': ''}, format='text/html')
        self.assertEqual(response.status_code, 401)
