from django.test import TestCase
from rest_framework.reverse import reverse


class EmployeeUrlTest(TestCase):

    def test_urls(self):
        response = self.client.get('http://example.localhost:8000' + reverse('emp'))
        print(response)
        self.assertEqual(response.status_code, 200)
