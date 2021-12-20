from django.test import TestCase

from lists.models import Item, List

# Create your tests here.
class NewListTest(TestCase):

    def test_can_save_a_POST_request(self):
        self.client.post('/lists/new', data={'id_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    
    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new', data={'id_text': 'A new list item'})
        new_list = List.objects.first()
        self.assertRedirects(response, f'/lists/{new_list.id}/')


    def test_invalid_list_items_arent_saved(self):
        self.client.post('/lists/new', data={'id_text': ''})
        self.assertEqual(List.objects.count(), 0)
        self.assertEqual(Item.objects.count(), 0)