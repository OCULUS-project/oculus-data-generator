from datetime import date
from enum import Enum
from typing import List


class JobStatus(Enum):
    """ representation of :Job status """
    NEW = 0
    WORKING = 1
    DONE = 2


class Job:
    def __init__(
            self, _id: str, status: JobStatus, owner: str, patient: str, image_file: str,
            facts: List[str], conclusions: List[str], created: date, updated: date
    ) -> None:
        self._id: str = _id
        self.status: JobStatus = status
        self.owner: str = owner
        """ id of creator of the job """
        self.patient: str = patient
        """ id of patient who is examined in the job """
        self.image_file: str = image_file
        """ id of image file used in the examination """
        self.facts: List[str] = facts
        """ ids of facts used as input of the job """
        self.conclusions: List[str] = conclusions
        """ ids of conclusions of the job """
        self.created: date = created
        self.updated: date = updated
