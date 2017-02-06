from io import StringIO

from django.test import TestCase

from importapp.utils import handle_upload


class ImportViewTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_view_loads_correctly(self):
        resp = self.client.get('/')
        self.assertTrue(resp.status_code, 200)


class ImportUtilsTestCase(TestCase):
    def setUp(self):
        self.test_csv = StringIO('12,waffles,anthony,food\n25,cookies,chad,food')

    def tearDown(self):
        pass

    def test_only_add_quatities_above_13(self):
        valid, invalid = handle_upload(self.test_csv)
        self.assertEqual(valid, [['25', 'cookies', 'chad', 'food']])
        self.assertEqual(invalid, [['12', 'waffles', 'anthony', 'food']])

    def test_none_added_if_none_over_13(self):
        self.test_csv = StringIO('12,waffles,anthony,food\n8,cookies,chad,food')
        valid, _ = handle_upload(self.test_csv)
        self.assertEqual(valid, [])

