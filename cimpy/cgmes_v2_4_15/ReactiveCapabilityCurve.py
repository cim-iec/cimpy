from .Curve import Curve
from .CGMESProfile import Profile


class ReactiveCapabilityCurve(Curve):
    """
    Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.

    :EquivalentInjection: The reactive capability curve used by this equivalent injection. Default: "list"
    :InitiallyUsedBySynchronousMachines: The default reactive capability curve for use by a synchronous machine. Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "EquivalentInjection": [Profile.EQ.value, ],
        "InitiallyUsedBySynchronousMachines": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class Curve:\n" + Curve.__doc__

    def __init__(self, EquivalentInjection = "list", InitiallyUsedBySynchronousMachines = "list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.EquivalentInjection = EquivalentInjection
        self.InitiallyUsedBySynchronousMachines = InitiallyUsedBySynchronousMachines

    def __str__(self):
        str = "class=ReactiveCapabilityCurve\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
