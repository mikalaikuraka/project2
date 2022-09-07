from django.test import TestCase

class SearchFormTestCase(TestCase):
    """Тест страниц"""

    def test_chat_room_status_code(self):
        response = self.client.get('/chat/1/')
        self.assertEquals(response.status_code, 200)

    def test_chat_page_status_code(self):
        response = self.client.get('/chat/')
        self.assertEquals(response.status_code, 200)

    def test_chat_home_status_code(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)