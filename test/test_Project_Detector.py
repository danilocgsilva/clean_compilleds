import unittest
import sys
sys.path.insert(1, "..")
from clean_compileds.Project_Detector import Project_Detector

class test_Project_Detector(unittest.TestCase):

    def test_can_detect_php_project(self):
        project_detector = Project_Detector()
        file_list = ['file1.txt', 'readme.md', 'vendor']
        project_detector.set_root_file_list(file_list)
        expected_response = 'php'
        object_response = project_detector.get_project_type()
        self.assertEqual(expected_response, object_response)

    def test_can_detect_node_project(self):
        project_detector = Project_Detector()
        file_list = ['file1.txt', 'readme.md', 'node_modules']
        project_detector.set_root_file_list(file_list)
        expected_response = 'node'
        object_response = project_detector.get_project_type()
        self.assertEqual(expected_response, object_response)

    def test_error_when_not_exists(self):
        project_detector = Project_Detector()
        file_list = ['file1.txt', 'readme.md', 'another_one_file.txt']
        project_detector.set_root_file_list(file_list)
        with self.assertRaises(Exception):
            project_detector.get_project_type()

    def test_error_when_forgot_set_file_list(self):
        project_detector =  Project_Detector()
        with self.assertRaises(Exception):
            project_detector.get_project_type()

