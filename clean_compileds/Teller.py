class Teller:

    def set_project_type(self, project_type: str):
        self.project_type = project_type
        return self


    def set_file_list(self, file_list: list):
        self.file_list = file_list
        return self


    def tell_project_type(self):

        if not hasattr(self, "project_type"):
            raise Exception("There's no project_type setted in the Teller object.")

        return "The detected project type is " + self.project_type + "."


    def tell_removing_files(self):

        if not hasattr(self, "file_list"):
            raise Exception("There's no project_type setted in the Teller object.")

        string_to_return = "The following files will be removed:\n"

        for removing_file in self.file_list:
            string_to_return += removing_file + "\n"

        return string_to_return
