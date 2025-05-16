import unittest
from unittest.mock import patch
from io import StringIO
import sys
import re

file = "01-parity/parity.py"
test_params = [
    ([10],'even'),
    ([15],'odd'),
    ([0],'even'),
    ([-2],'even'),
    ([-51],'odd'),
]

class TestEvenOrOdd(unittest.TestCase):

    @patch('builtins.input', create=True)
    def test_nums(self, mock_input):
        for params in test_params:
            test_input = params[0]
            mock_input.side_effect = test_input

            test_output = params[1]
            expected_output = f"{test_input[0]} is {test_output}."
            expected_re = re.compile(
                rf'{test_input[0]}\s.*{test_output}',
                re.IGNORECASE
            )

            # Redirect stdout to capture prints
            captured_output = StringIO()
            sys.stdout = captured_output
            
            # Execute script
            exec(open(file).read())
            sys.stdout = sys.__stdout__
            
            # Get the output 
            output = captured_output.getvalue()
            
            # Check the output
            self.assertRegex(output,
                             expected_re,
                             f"\nFor values {test_input}, I expected:\n{expected_output}\nbut I saw:\n{output}")

if __name__ == '__main__':
    unittest.main()
