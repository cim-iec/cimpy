from .WindTurbineType1or2IEC import WindTurbineType1or2IEC
from .CGMESProfile import Profile


class WindGenTurbineType1IEC(WindTurbineType1or2IEC):
    """
    Wind turbine IEC Type 1.  Reference: IEC Standard 61400-27-1, section 6.5.2.

    :WindAeroConstIEC: Wind aerodynamic model associated with this wind turbine type 1 model. Default: None
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "WindAeroConstIEC": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class WindTurbineType1or2IEC:\n" + WindTurbineType1or2IEC.__doc__

    def __init__(self, WindAeroConstIEC = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.WindAeroConstIEC = WindAeroConstIEC

    def __str__(self):
        str = "class=WindGenTurbineType1IEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
