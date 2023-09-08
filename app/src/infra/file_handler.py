import os
import shutil


class FileHandler:
    def __init__(self, folder: str):
        self.folder = folder

    def list_files_in_directory(self):
        return os.listdir(self.folder)

    def is_path_a_file(self, path):
        return os.path.isfile(os.path.join(self.folder, path))

    def is_path_exists(self, path):
        return os.path.exists(os.path.join(self.folder, path))

    def make_directory(self, path):
        return os.makedirs(os.path.join(self.folder, path))

    def move_file(self, file, destination_folder):
        shutil.move(
            os.path.join(self.folder, file),
            os.path.join(self.folder, destination_folder)
        )
