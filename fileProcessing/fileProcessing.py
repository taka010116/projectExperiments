import flet as ft
import cv2
import os
from flet import (
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    Page,
    Row,
    Text,
    icons,
)

class mkdir:

    def __init__(self):
        self.directory_path = "hoge"

    def get_directory_result(self, e: FilePickerResultEvent):
        self.directory_path = e.path

