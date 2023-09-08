from ...domain.constants.file_classification_dict import FILE_DICT
from ...domain.entities.file_item import FileItem
from ...infra.file_handler import FileHandler


class MoveFilesToClassificationFolder:

    def __init__(self, folder: str):
        self.folder = folder
        self.file_handler = FileHandler(self.folder)

    def execute(self):
        files = self.list_all_files_in_folder()
        files = [FileItem(file) for file in files]
        for file in files:
            self.move_file(file)
        print(files)

    def list_all_files_in_folder(self):
        return [f for f in self.file_handler.list_files_in_directory() if self.file_handler.is_path_a_file(f)]

    def move_file(self, file_item: FileItem):
        try:
            folder = FILE_DICT[file_item.extension]
            if not self.file_handler.is_path_exists(folder):
                self.file_handler.make_directory(folder)
            self.file_handler.move_file(file_item.file, folder)
            print(f"File '{file_item.file}' moved to '{folder}' successfully.")
        except Exception as e:
            print(f"Error moving file: {file_item.file}")
