from django.db.transaction import TransactionManagementError
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework import status

from spendings.models import Spending, SpendingCategory
from authentication.models import User
from money_heist.tests import BaseAPITest

#
# class TestSpendingsViewSet(BaseAPITest):
#
#     def setUp(self):
#         self.email = 'test_email'
#         self.password = 'test_password'
#         self.user = self.create_and_login(email=self.email, password=self.password)
#         self.spending_category = mixer.blend(SpendingCategory)
#         self.spending = mixer.blend(Spending, user=self.user, category=self.spending_category)
#
#     def test_get_list_of_spending(self):
#         response = self.client.get(reverse('v1:spendings-list'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_create_new_spending(self):
#         data = {
#             'amount': 'any_spending',
#             'description': 'any_description',
#             'user': self.user,
#             'category': self.spending_category
#         }
#         response = self.client.post(reverse('v1:spendings-list'), data=data, format="json")
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertTrue(SpendingCategory.objects.filter(pk=response.data['id']).exists())
#
#     def test_create_exists_spending(self):
#         data = {
#             'amount': 'any_spending',
#             'description': 'any_description',
#             'user': self.user,
#             'category': self.spending_category
#         }
#         self.client.post(reverse('v1:spendings-list'), data=data)
#         try:
#             self.client.post(reverse('v1:spendings-list'), data=data)
#         except TransactionManagementError:
#             response_status = status.HTTP_424_FAILED_DEPENDENCY
#         finally:
#             self.assertEqual(response_status, status.HTTP_424_FAILED_DEPENDENCY)
#
#     def test_create_spending_with_invalid_data(self):
#         data = {
#             'amount': None,
#             'description': 'any_description',
#             'user': self.user,
#             'category': self.spending_category
#         }
#         response = self.client.post(reverse('v1:spendings-list'), data=data)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#
#     def test_create_new_spending_when_logged_out(self):
#         self.logout()
#         data = {
#             'amount': 'any_spending',
#             'description': 'any_description',
#             'user': self.user,
#             'category': self.spending_category
#         }
#         response = self.client.post(reverse('v1:spendings-list'), data=data)
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
#
#     def test_delete_spending(self):
#         response = self.client.delete(reverse('v1:spendings-detail', args=(self.spending.id, )))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#
#     def test_delete_spending_of_another_user(self):
#         user = mixer.blend(User)
#         self.spending.user = user
#         self.spending.save()
#         response = self.client.delete(reverse('v1:spendings-detail', args=(self.spending.id, )))
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#
#     def test_update_spending_when_logged_out(self):
#         data1 = {
#             'amount': 'any_spending',
#             'description': 'any_description',
#             'user': self.user,
#             'category': self.spending_category
#         }
#
#         data2 = {
#             'amount': 'any_spending',
#             'description': 'any_description',
#             'user': self.user,
#             'category': self.spending_category
#         }
#         self.client.post(reverse('v1:spendings-list'), data=data1)
#         spending_id = Spending.objects.get(name='any_category').pk
#         self.logout()
#         response = self.client.post(reverse('v1:spending-detail', args=(spending_id, )), data=data2)
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)



class TestSpendingsCategoriesViewSet(BaseAPITest):

    def setUp(self):
        self.email = 'test_email'
        self.password = 'test_password'
        self.user = self.create_and_login(email=self.email, password=self.password)
        self.spending_category = mixer.blend(SpendingCategory)

    def test_get_list_of_spendings(self):
        response = self.client.get(reverse('v1:spendings:categories-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_new_category(self):
        data = {
            'name': 'new_category'
        }
        response = self.client.post(reverse('v1:spendings:categories-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(SpendingCategory.objects.filter(pk=response.data['id']).exists())

    def test_create_exists_category(self):
        data = {
            'name': 'new_category'
        }
        self.client.post(reverse('v1:spendings:categories-list'), data=data)
        try:
            self.client.post(reverse('v1:spendings:categories-list'), data=data)
        except TransactionManagementError:
            response_status = status.HTTP_424_FAILED_DEPENDENCY
        finally:
            self.assertEqual(response_status, status.HTTP_424_FAILED_DEPENDENCY)

    def test_create_category_with_invalid_data(self):
        data = {
            'name': None
        }
        response = self.client.post(reverse('v1:spendings:categories-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_new_category_when_logged_out(self):
        self.logout()
        data = {
            'name': 'any_category'
        }
        response = self.client.post(reverse('v1:spendings:categories-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_category(self):
        response = self.client.delete(reverse('v1:spendings:categories-detail', args=(self.spending_category.id, )))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_category_of_another_user(self):
        user = mixer.blend(User)
        self.spending_category.user = user
        self.spending_category.save()
        response = self.client.delete(reverse('v1:spendings:categories-detail', args=(self.spending_category.id, )))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_category_when_logged_out(self):
        data1 = {
            'name': 'any_category'
        }

        data2 = {
            'name': 'update_category'
        }
        self.client.post(reverse('v1:spendings:categories-list'), data=data1)
        category_id = SpendingCategory.objects.get(name='any_category').pk
        self.logout()
        response = self.client.post(reverse('v1:spendings:categories-detail', args=(category_id, )), data=data2)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)






