from django.test import TestCase
from django.urls import reverse

class IndexViewTestCase(TestCase):
    
    def test_index_view(self):
        # Issue a GET request to the index view
        response = self.client.get(reverse('index'))
        
        # Check that the response is successful
        self.assertEqual(response.status_code, 200)
        
        # Check that the 'index.html' template is used
        self.assertTemplateUsed(response, 'index.html')

