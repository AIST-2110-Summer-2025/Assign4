import unittest
from unittest.mock import patch
from io import StringIO
import sys

file = "02-password/password.py"
test_params = [
    (['password123','password123'],'Passwords match'),
    (['password123','Password123'],'Passwords do not match'),
    (['password123','password'],'Passwords do not match'),
    (['',''],'Passwords match'),
]

class TestPasswordMatcher(unittest.TestCase):

    @patch('builtins.input', create=True)  # Mocking inputs
    def test_passwords(self, mock_input):
        for params in test_params:
            test_input = params[0]
            mock_input.side_effect = test_input

            expected_output = params[1].strip()

            # Redirect stdout to capture prints
            captured_output = StringIO()
            sys.stdout = captured_output
            
            # Execute script
            exec(open(file).read())
            
            sys.stdout = sys.__stdout__
            
            # Get the output and strip any extra newlines or spaces
            output = captured_output.getvalue().strip()
            
            # Check if the output is the expected string
            self.assertIn(
                expected_output.lower(),
                output.lower(),
                f"\nFor inputs {test_input}, I expected:\n'{expected_output}'\nbut I saw: '{output}'"
            )

if __name__ == '__main__':
    unittest.main()
