import os

from .application.use_cases.move_files_to_classification_folder import MoveFilesToClassificationFolder
from .infra.watchdog.file_watcher import FileCreatedHandler, FileWatcher

FOLDER_PATH = os.path.abspath('../test-folder')

if __name__ == '__main__':
    move_file_to_classification_folder = MoveFilesToClassificationFolder(FOLDER_PATH)
    file_created_handler = FileCreatedHandler(move_file_to_classification_folder)
    file_watcher = FileWatcher()
    file_watcher.start(FOLDER_PATH, file_created_handler)
