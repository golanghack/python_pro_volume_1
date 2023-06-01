from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home

class HomeTest(TestCase):
    """Home page test"""

    def test_root_url_resolves_to_home_page_view(self):
        """-> root url to view for home page""" 

        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_home_page_returns_corect_html_template(self):
        """Correct html template""" 

        request = HttpRequest()
        response = home(request)
        html_template = response.content.decode('UTF-8')
        member = '<title>To-do</title>'
        container = self.browser.title

        self.assertTrue(html.startswith('<html>'))
        self.assertIn(member, container)
        self.assertTrue(html.endswith('</html>'))
