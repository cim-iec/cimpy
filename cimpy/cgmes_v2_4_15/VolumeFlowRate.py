from .Base import Base
from .CGMESProfile import Profile


class VolumeFlowRate(Base):
    """
    Volume per time.

    :denominatorMultiplier:  Default: None
    :denominatorUnit:  Default: None
    :multiplier:  Default: None
    :unit:  Default: None
    :value:  Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "denominatorMultiplier": [Profile.DY.value, ],
        "denominatorUnit": [Profile.DY.value, ],
        "multiplier": [Profile.DY.value, ],
        "unit": [Profile.DY.value, ],
        "value": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value


    def __init__(self, denominatorMultiplier = None, denominatorUnit = None, multiplier = None, unit = None, value = 0.0):

        self.denominatorMultiplier = denominatorMultiplier
        self.denominatorUnit = denominatorUnit
        self.multiplier = multiplier
        self.unit = unit
        self.value = value

    def __str__(self):
        str = "class=VolumeFlowRate\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
