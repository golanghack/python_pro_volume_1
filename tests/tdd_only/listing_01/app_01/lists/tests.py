
from django.test import TestCase
from lists.models import Item 

class HomeTest(TestCase):
    """Home page test"""

    def test_uses_home_template(self):
        """-> used home template""" 

        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        """-> may be save post-request?""" 
        
        member = 'A new list item'
        response = self.client.post('/', data={'item_text': member})
        container = response.content.decode()

        self.assertIn(member, container)
        self.assertTemplateUsed(response, 'home.html')

        new_item = Item.objects.first()

        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual(new_item.text, member)
        self.assertIn(member, container)
        self.assertTemplateUsed(response, 'home.html')


class TestModelItem(TestCase):
    """-> model item of list""" 

    def test_saving_and_retrieving_items(self):
        """-> save and get element of list""" 

        first_item = Item() 
        first_item.text = 'One'
        first_item.save()

        second_item = Item()
        second_item.text = 'Two'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'One')
        self.assertEqual(second_saved_item.text, 'Two')


