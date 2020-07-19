import os
import shutil
from clean_compileds.Project_Detector import Project_Detector
from clean_compileds.Node_File_List import Node_File_List
from clean_compileds.PHP_File_List import PHP_File_List

def main():

    project_type = Project_Detector().set_root_file_list(os.listdir()).get_project_type()

    if project_type == 'php':
        deleting_file_list = PHP_File_List()
    elif project_type == 'node':
        deleting_file_list = Node_File_List()

    for file in deleting_file_list.get_file_list():
        shutil.rmtree(os.path.join(os.getcwd(), file))


if __name__ == "__main__":
    main()