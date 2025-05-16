import unittest
from unittest.mock import patch
from io import StringIO
import sys

file = "03-pay/pay.py"
test_params = [
    (['40','15.5'],'Your gross pay is $620.0'),
    (['30','15'],'Your gross pay is $450.0'),
    (['45','10.5'],'Your gross pay is $498.75'),
    (['60.5','20'],'Your gross pay is $1415.0'),
    (['0','10.5'],'Your gross pay is $0.0'),
    (['45','0'],'Your gross pay is $0'),
    (['10.5','10'],'Your gross pay is $105.0'),
    (['-5','10'],'Hours and rate should be positive'),
    (['5','-10'],'Hours and rate should be positive'),
    (['-5','-10'],'Hours and rate should be positive'),
]

class TestGrossPayCalculation(unittest.TestCase):

    @patch('builtins.input', create=True)  # Mocking inputs
    def test_gross_pay_output(self, mock_input):
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
                f"\nFor inputs {test_input}, I expected:\n'{expected_output}'\nbut I saw:\n'{output}'"
            )

if __name__ == '__main__':
    unittest.main()
