# from django.test import TestCase, Client, SimpleTestCase
# from django.urls import reverse
# from users.forms import UserRegisterForm, UserUpdateForm

# class TestForms_Registration(TestCase):
#     def test_registration_form_with_data(self):
#         form = UserRegisterForm(data={
#             'username':'UserTest',
#             'email':'userTest@email.com',
#             'password1':'1234redbottle',
#             'password2':'1234redbottle'
#         })
#         self.assertTrue(form.is_valid())

#     def test_registration_form_no_data(self):
#         form = UserRegisterForm(data={})
#         self.assertFalse(form.is_valid())
#         self.assertEquals(len(form.errors), 4)

# class TestForms_UserUpdate(TestCase):
#     def test_userupdate_form_no_data(self):
#         form = UserUpdateForm(data={
#             'username':'userTest',
#             'email':'userTest@email.com'
#         })
#         self.assertTrue(form.is_valid())
#         self.assertEquals(len(form.errors), 0)