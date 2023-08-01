import os


class FileItem:

    def __init__(self, file_name: str) -> None:
        base_name, extension = os.path.splitext(file_name)
        self.file = f'{base_name}{extension}'
        self.extension = extension

    def __str__(self):
        return self.file
