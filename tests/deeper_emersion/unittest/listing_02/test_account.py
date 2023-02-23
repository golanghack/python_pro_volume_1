#! /usr/bin/env python3 

import unittest
from mock import Mock
from Account import Account

class TestAccoiunt(unittest.TestCase):
    """Testing simple class Account."""
    
    def test_account_returns_data_for_id_1(self) -> None:
        account_data = {'id': '1', 'name': 'test'}
        mock_data_interface = Mock()
        mock_data_interface.get.return_value = account_data
        account = Account(mock_data_interface)
        self.assertDictEqual(account_data, account.get_account(1))
    
    def test_account_when_connect_exception_raised(self) -> None:
        mock_data_interface = Mock()
        mock_data_interface.get.side_effect = ConnectionError()
        account = Account(mock_data_interface)
        
        self.assertEqual('Connection error occured. Try again.', account.get_account(1))
        
if __name__ == '__main__':
    unittest.main()