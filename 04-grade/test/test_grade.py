import unittest
from unittest.mock import patch
from io import StringIO
import sys

file = "04-grade/grade.py"
test_params = [
    (['10','10'],'10 out of 10 is 100.0% (A)'),
    (['20','16'],'16 out of 20 is 80.0% (B)'),
    (['12','9'],'9 out of 12 is 75.0% (C)'),
    (['13','8'],'8 out of 13 is 61.53846153846154% (D)'),
    (['100','90'],'90 out of 100 is 90.0% (A)'),
    (['100','89'],'89 out of 100 is 89.0% (B)'),
    (['100','79'],'79 out of 100 is 79.0% (C)'),
    (['100','70'],'70 out of 100 is 70.0% (C)'),
    (['100','69'],'69 out of 100 is 69.0% (D)'),
    (['100','60'],'60 out of 100 is 60.0% (D)'),
    (['100','59'],'59 out of 100 is 59.0% (F)'),
    (['5','0'],'0 out of 5 is 0.0% (F)'),
]


class TestGradeCalculation(unittest.TestCase):

    @patch('builtins.input', create=True)  # Mocking inputs
    def test_grades(self, mock_input):
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
