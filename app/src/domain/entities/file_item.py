import os


class FileItem:

    def __init__(self, file_name: str) -> None:
        base_name, extension = os.path.splitext(file_name)
        self.file = f'{base_name}{extension}'
        self.extension = extension

    def __repr__(self):
        return f'FileItem(file_name="{self.file}")'
