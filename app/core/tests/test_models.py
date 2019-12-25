from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """test to see if create user with email is successful"""
        email = 'test@test.de'
        password = 'test123#'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test the email for a new user is normalized"""
        email = ' test@tESt.de   '
        password = 'test123#'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower().strip())

    def test_new_user_invalid_email(self):
        """tests if invalid email address fails"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """test creation of new superuser"""
        user = get_user_model().objects.create_superuser(
            'superuser@email.com',
            'test123#'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
