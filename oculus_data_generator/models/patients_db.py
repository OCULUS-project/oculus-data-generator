from datetime import date
from typing import Dict


class Patient:
    """ personal and contact data of the patient """

    def __init__(
            self, _id: str, first_name: str, last_name: str, pesel: str, email: str, phone: str, password: str = ''
    ) -> None:
        self._id: str = _id
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.pesel: str = pesel
        self.email: str = email
        self.phone: str = phone
        self.password: str = password
        """ password for remote access of inference results """


class PatientMetrics:
    """ data from examination of the patient """

    def __init__(
            self, _id: str, patient: str, doctor: str, created: date, attributes: Dict[str, str], notes: str
    ) -> None:
        self._id: str = _id
        self.patient: str = patient
        """ id of examined patient """
        self.doctor: str = doctor
        """ id of doctor committing examination """
        self.created: date = created
        self.attributes: Dict[str, str] = attributes
        """ results of examination """
        self.notes: str = notes
        """ doctors notes not being part of future inference """

