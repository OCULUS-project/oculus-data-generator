from enum import Enum
from typing import List, Set


class GrfIrf:
    """ factor of reliability of an entity """

    def __init__(self, grf: float, irf: float) -> None:
        self.grf: float = grf
        """ level of the dependence of a rule’s conclusion on rule’s premises """
        self.irf: float = irf
        """ quality of the underlying rule """


class FactSourceType(Enum):
    """ types of facts sources """
    METRICS = 'METRICS'
    IMAGE = 'IMAGE'


class FactSource:
    """ explains the source from which the fact was inferred or generated """

    def __init__(self, source_type: FactSourceType, _id: str) -> None:
        self.source_type: FactSourceType = source_type
        self._id: str = _id
        """  id of source entity """


class Rule:
    """ rule on which the inference is based """

    def __init__(self, _id: str, premises: List[str], conclusions: List[str], grf_irf: GrfIrf) -> None:
        self._id: str = _id
        self.premises: List[str] = premises
        self.conclusions: List[str] = conclusions
        self.grf_irf: GrfIrf = grf_irf


class Premise:
    """ premise for a rule """

    def __init__(self, _id: str, head: str, premise_set: Set[str], conjunction: bool) -> None:
        self._id: str = _id
        self.head: str = head
        self.premise_set: Set[str] = premise_set
        self.conjunction: bool = conjunction


class Fact(Premise):
    """ premise with GrfIrf """

    def __init__(self, _id: str, head: str, premise_set: Set[str], conjunction: bool, grf_irf: GrfIrf) -> None:
        self.grf_irf: GrfIrf = grf_irf
        super().__init__(_id, head, premise_set, conjunction)


class SourceFact(Fact):
    """ fact generated from some source """

    def __init__(
            self, _id: str, head: str, premise_set: Set[str], conjunction: bool, grf_irf: GrfIrf,
            job: str, source: FactSource
    ) -> None:
        self.job: str = job
        """ id of job the facts belongs to """
        self.source: FactSource = source
        """ source from which the fact was inferred or generated """
        super().__init__(_id, head, premise_set, conjunction, grf_irf)


class Conclusion(Fact):
    """ fact generated from a job """
    def __init__(
            self, _id: str, head: str, premise_set: Set[str], conjunction: bool, grf_irf: GrfIrf,
            job: str
    ) -> None:
        self.job: str = job
        """ id of job the conclusion belongs to """
        super().__init__(_id, head, premise_set, conjunction, grf_irf)


class AttributeUnit(Enum):
    """ the unit of the value of the datatype """
    # length
    METER = 'METER',
    CENTIMETER = 'CENTIMETER',

    # weight
    KILOGRAM = 'KILOGRAM',
    GRAM = 'GRAM',

    # angle
    DEGREE = 'DEGREE',

    # other
    UNIT = 'UNIT',
    PERCENT = 'PERCENT',
    NONE = 'NONE'


class AttributeType(Enum):
    """ data type of the value of the attribute """
    INT = 'INT',
    UINT = 'UINT',
    FLOAT = 'FLOAT',
    UFLOAT = 'UFLOAT',
    STRING = 'STRING'


class AttributeTemplate:
    """ an entity that can be converted into fact """

    def __init__(
            self, _id: str, name: str, unit: AttributeUnit, attribute_type: AttributeType, regex: str, values: Set[str],
            value_range: {
                min: str,
                max: str
            },
            description: str
    ) -> None:
        self.name = name
        self.unit = unit
        self.attribute_type = attribute_type
        self.regex = regex
        self.values = values
        """ values to choose from """
        self.value_range = value_range
        """ range of number values <min, max> """
        self.description = description
        """ explanation of the attribute """
