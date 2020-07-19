import abc

class Removing_Files_Interface(abc.ABC):

    @abc.abstractmethod
    def get_file_list(self) -> list:
        pass
