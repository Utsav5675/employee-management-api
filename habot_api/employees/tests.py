from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Employee


class EmployeeAPITests(APITestCase):

    def setUp(self):
        # Create user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        # Get token
        token_url = reverse('token_obtain_pair')
        response = self.client.post(token_url, {
            'username': 'testuser',
            'password': 'testpass123'
        })

        self.access_token = response.data['access']
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.access_token
        )

        # Create one employee
        self.employee = Employee.objects.create(
            name='Test Employee',
            email='test@example.com',
            department='HR',
            role='Manager'
        )

    def test_create_employee(self):
        data = {
            'name': 'New Employee',
            'email': 'new@example.com',
            'department': 'Sales',
            'role': 'Executive'
        }
        response = self.client.post('/api/employees/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_duplicate_email(self):
        data = {
            'name': 'Duplicate',
            'email': 'test@example.com',
            'department': 'HR',
            'role': 'Manager'
        }
        response = self.client.post('/api/employees/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_employees(self):
        response = self.client.get('/api/employees/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_employee(self):
        response = self.client.get(f'/api/employees/{self.employee.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_employee(self):
        response = self.client.delete(f'/api/employees/{self.employee.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

