# this library wil allow us to mock django get_databse function
from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            #  this mocked ConnectionHandler will return true
            gi.return_value = True
            call_command('wait_for_db')
            #  assert that the connection was called context_processors
            self.assertEqual(gi.call_count, 1)

# we can mock the behaviour of time.sleep to not wait
# that means during test,the function wont wait the seconds or how long it has to wait. This will speed up the test
    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            #  the call failed 5 times and on 6th time was successful
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
