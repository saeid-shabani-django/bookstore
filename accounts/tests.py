from django.test import TestCase
from django.urls import reverse
class HomePageTest(TestCase):
    def test_home_page_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)
    def test_home_word_available(self):
        resp = self.client.get(reverse('home'))
        self.assertContains(resp,'Home Page')

    def test_home_url(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code,200)
    def test_home_page_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response,'home.html')



