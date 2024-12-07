import pytest
from homework_03.src.controller.controller import Controller
from homework_03.src.model.FileWork import FileWork
import os


@pytest.fixture
def create_file_and_controller():
    file = FileWork()
    controller = Controller()
    yield file, controller
    del file, controller


@pytest.fixture()
def create_and_delete_file():
    with open('1.json', 'x'):
        pass
    yield
    os.remove('1.json')


