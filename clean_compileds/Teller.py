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

        print("The detected project type is " + self.project_type)
        return self


    def tell_removing_files(self):
        
        return self
