import os
import shutil
from clean_compileds.Project_Detector import Project_Detector
from clean_compileds.Node_File_List import Node_File_List
from clean_compileds.PHP_File_List import PHP_File_List
from clean_compileds.Teller import Teller
from clean_compileds.Project_Not_Detected import Project_Not_Detected

def main():

    project_detector = Project_Detector().set_root_file_list(os.listdir())
    try:
        project_type = project_detector.get_project_type()
    except Project_Not_Detected:
        print("I cound not found the project type or it may already cleaned.")
        exit()

    if project_type == 'php':
        deleting_file_list = PHP_File_List()
    elif project_type == 'node':
        deleting_file_list = Node_File_List()

    teller = Teller().set_project_type(project_type)
    print(teller.tell_project_type())

    files_to_delete = deleting_file_list.get_file_list()
    teller.set_file_list(files_to_delete)
    print(teller.tell_removing_files())

    for file in files_to_delete:
        shutil.rmtree(os.path.join(os.getcwd(), file))


if __name__ == "__main__":
    main()
