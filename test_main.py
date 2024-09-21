import unittest
import sys
from unittest.mock import patch, MagicMock
import main

class TestMain(unittest.TestCase):
    @patch('main.run_script')
    def test_mern_stack(self, mock_run_script):
        test_args = ["main.py", "MERN", "my_project"]
        with patch.object(sys, 'argv', test_args):
            main.main()
            mock_run_script.assert_called_once_with("mern.py", "my_project", "/frontend-stack-automation/templates/server")

    @patch('main.run_script')
    def test_mevn_stack(self, mock_run_script):
        test_args = ["main.py", "MEVN", "my_project"]
        with patch.object(sys, 'argv', test_args):
            main.main()
            mock_run_script.assert_called_once_with("mevn.py", "my_project", "/frontend-stack-automation/templates/server")

    @patch('main.run_script')
    def test_mean_stack(self, mock_run_script):
        test_args = ["main.py", "MEAN", "my_project"]
        with patch.object(sys, 'argv', test_args):
            main.main()
            mock_run_script.assert_called_once_with("mean.py", "my_project", "/frontend-stack-automation/templates/server")

    def test_invalid_stack(self):
        test_args = ["main.py", "INVALID", "my_project"]
        with patch.object(sys, 'argv', test_args), patch('builtins.print') as mocked_print, patch('sys.exit') as mock_exit:
            main.main()
            mocked_print.assert_called_with("Invalid stack name. Please choose MERN, MEVN or MEAN.")
            mock_exit.assert_called_once_with(1)

if __name__ == '__main__':
    unittest.main()
