from datetime import date
from typing import List


class ImageFile:
    """ aggregates images from one series """

    def __init__(self, _id: str, patient: str, doctor: str, images: List[str], created: date, notes: str) -> None:
        self._id: str = _id
        self.patient: str = patient
        self.doctor: str = doctor
        self.images: List[str] = images
        self.created: date = created
        self.notes: str = notes
        """ doctors notes """


class Image:
    """ stores metadata and location of the image """

    def __init__(self, _id: str, path: str, created: date, notes: str) -> None:
        self._id: str = _id
        self.path: str = path
        """ path to the image in filesystem """
        self.created: date = created
        self.notes: str = notes
        """ doctors notes """
