import unittest
import os
import sys
from unittest.mock import patch, MagicMock
from file_manager import parse_arguments, main

class TestFileManager(unittest.TestCase):

    def setUp(self):
        self.original_argv = sys.argv
        self.test_dir = os.path.join(os.getcwd(), 'test_dir')
        if not os.path.exists(self.test_dir):
            os.mkdir(self.test_dir)
    
    def tearDown(self):
        sys.argv = self.original_argv
        if os.path.exists(self.test_dir):
            os.rmdir(self.test_dir)

    def test_parse_arguments_basic_mode(self):
        test_args = ['file_manager.py', '-m', 'basic']
        with patch.object(sys, 'argv', test_args):
            mode, directory = parse_arguments()
            self.assertEqual(mode, 'basic')
            self.assertIsNone(directory)

    def test_parse_arguments_elevated_with_mode_directory(self):
        test_args = ['file_manager.py', '-m', 'elevated', '-d', self.test_dir]
        with patch.object(sys, 'argv', test_args):
            mode, directory = parse_arguments()
            self.assertEqual(mode, 'elevated')
            self.assertEqual(directory, self.test_dir)

    def test_parse_arguments_admin_mode(self):
        test_args = ['file_manager.py', '-m', 'admin']
        with patch.object(sys, 'argv', test_args):
            mode, directory = parse_arguments()
            self.assertEqual(mode, 'admin')
            self.assertIsNone(directory)

    def test_main_basic_mode(self):
        test_args = ['file_manager.py', '-m', 'basic']
        with patch.object(sys, 'argv', test_args):
            with patch('builtins.input', side_effect=['3']):
                main()

    def test_main_elevated_mode(self):
        test_args = ['file_manager.py', '-m', 'elevated']
        with patch.object(sys, 'argv', test_args):
            with patch('builtins.input', side_effect=['4']):
                main()


    def test_main_admin_mode(self):
        test_args = ['file_manager.py', '-m', 'admin']
        with patch.object(sys, 'argv', test_args):
            with patch('builtins.input', side_effect=['6']):
                main()


if __name__ == '__main__':
    unittest.main()