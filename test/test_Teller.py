import unittest
import sys
sys.path.insert(1, "..")
from clean_compileds.Teller import Teller

class test_Teller(unittest.TestCase):

    def setUp(self):
        self.teller = Teller()

    def test_can_tell_project_type(self):
        self.teller.set_project_type("PHP")
        expected_string = "The detected project type is PHP."
        returned_string = self.teller.tell_project_type()
        self.assertEqual(expected_string, returned_string)


    def test_can_tell_project_type_another_project(self):
        self.teller.set_project_type("node")
        expected_string = "The detected project type is node."
        returned_string = self.teller.tell_project_type()
        self.assertEqual(expected_string, returned_string)


    def test_give_list_deletting_files(self):

        file_list = ["file1.txt", "file2.txt", "file3.md"]
        self.teller.set_file_list(file_list)

        expected_string = "The following files will be removed:\n"

        for file in file_list:
            expected_string += file + "\n"

        returned_string = self.teller.tell_removing_files()

        self.assertEqual(expected_string, returned_string)


    def test_error_get_project_type_without_setting_it(self):
        with self.assertRaises(Exception):
            self.teller.tell_project_type()


    def test_error_get_file_list_without_setting_it(self):
        with self.assertRaises(Exception):
            self.teller.tell_removing_files()
        

