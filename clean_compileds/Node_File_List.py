from clean_compileds.Removing_Files_Interface import Removing_Files_Interface

class Node_File_List(Removing_Files_Interface):

    def get_file_list(self) -> list:
        return ["node_modules"]
