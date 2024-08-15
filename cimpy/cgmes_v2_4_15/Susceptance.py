from .Base import Base
from .CGMESProfile import Profile


class Susceptance(Base):
    """
    Imaginary part of admittance.

    :multiplier:  Default: None
    :unit:  Default: None
    :value:  Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "multiplier": [Profile.EQ.value, ],
        "unit": [Profile.EQ.value, ],
        "value": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value


    def __init__(self, multiplier = None, unit = None, value = 0.0):

        self.multiplier = multiplier
        self.unit = unit
        self.value = value

    def __str__(self):
        str = "class=Susceptance\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
