import unittest
from unittest.mock import patch

import main


# Tester
class MyTestClass(unittest.TestCase):

    # Shall start with 'test_'
    def test_my_test_method(self):
        mock = patch('main.FunctionName').start()
        mock.return_value = 2
        
        ToPatchedThisValue = 3
        patch('main.FieldName', ToPatchedThisValue).start()
        
        # Exec the tests
        test_fieldname = main.FieldName
        function_returnvalue = main.FunctionName()
        
        # Test
        self.assertEqual(function_returnvalue, 2)
        self.assertEqual(test_fieldname, 3)
        



if __name__ == '__main__':
    unittest.main()

