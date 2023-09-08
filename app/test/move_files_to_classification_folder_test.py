# Criar a pasta (test_folder)
# Rodar monitoramento
# Adicionar arquivo de txt na pasta
# Verificar se arquivo foi movido
# Prosseguir para proximo tipo de arquivo
# Excluir pasta com todos os seus componentes internos
import os
import unittest

from app.src.application.use_cases.move_files_to_classification_folder import MoveFilesToClassificationFolder
from app.src.infra.file_handler import FileHandler

FOLDER_PATH = os.path.abspath('./test/test_folder')
TEXT_FOLDER = FOLDER_PATH + '/Text'
IMAGE_FOLDER = FOLDER_PATH + '/Image'


def move_folder_content_to_parent_folder(folder: str):
    file_handler = FileHandler(folder)
    files_in_directory_text = file_handler.list_files_in_directory()
    for file in files_in_directory_text:
        file_handler.move_file(file, '../')


def get_items_in_the_folder(folder: str) -> [str]:
    file_handler = FileHandler(folder)
    return file_handler.list_files_in_directory()


class TestStringMethod(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(FOLDER_PATH)
        move_file_to_classification_folder = MoveFilesToClassificationFolder(FOLDER_PATH)
        move_file_to_classification_folder.execute()

    def test_text_files_exists(self):
        files_in_directory = get_items_in_the_folder(TEXT_FOLDER)
        self.assertEqual(len(files_in_directory), 1)

    def test_image_files_exists(self):
        files_in_directory = get_items_in_the_folder(IMAGE_FOLDER)
        self.assertEqual(len(files_in_directory), 1)

    @classmethod
    def tearDownClass(cls):
        move_folder_content_to_parent_folder(TEXT_FOLDER)
        move_folder_content_to_parent_folder(IMAGE_FOLDER)


if __name__ == '__main__':
    unittest.main()
