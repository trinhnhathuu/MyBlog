from django.test import TestCase,SimpleTestCase

class SimpleTest(SimpleTestCase):
    def test_home_page_status(self):
        reponse = self.client.get('/')
        self.assertEquals(reponse.status_code,200)

# Create your tests here.
