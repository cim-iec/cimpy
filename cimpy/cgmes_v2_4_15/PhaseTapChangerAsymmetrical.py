from .PhaseTapChangerNonLinear import PhaseTapChangerNonLinear
from .CGMESProfile import Profile


class PhaseTapChangerAsymmetrical(PhaseTapChangerNonLinear):
    """
    Describes the tap model for an asymmetrical phase shifting transformer in which the difference voltage vector adds to the primary side voltage. The angle between the primary side voltage and the difference voltage is named the winding connection angle. The phase shift depends on both the difference voltage magnitude and the winding connection angle.

    :windingConnectionAngle: The phase angle between the in-phase winding and the out-of -phase winding used for creating phase shift. The out-of-phase winding produces what is known as the difference voltage.  Setting this angle to 90 degrees is not the same as a symmemtrical transformer. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.SSH.value, ],
        "windingConnectionAngle": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class PhaseTapChangerNonLinear:\n" + PhaseTapChangerNonLinear.__doc__

    def __init__(self, windingConnectionAngle = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.windingConnectionAngle = windingConnectionAngle

    def __str__(self):
        str = "class=PhaseTapChangerAsymmetrical\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
