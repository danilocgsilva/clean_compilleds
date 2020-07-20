from clean_compileds.Project_Not_Detected import Project_Not_Detected

class Project_Detector:

    def set_root_file_list(self, file_list: list):
        self.file_list = file_list
        return self


    def get_project_type(self):
        if not hasattr(self, "file_list"):
            raise Exception("You need set the file list in the Project_Detector.")
        if 'vendor' in self.file_list:
            return 'php'
        if 'node_modules' in self.file_list:
            return 'node'
        raise Project_Not_Detected('I could not detect the project type. Sorry.')
