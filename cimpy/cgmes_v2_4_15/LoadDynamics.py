from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class LoadDynamics(IdentifiedObject):
    """
    Load whose behaviour is described by reference to a standard model   A standard feature of dynamic load behaviour modelling is the ability to associate the same behaviour to multiple energy consumers by means of a single aggregate load definition.  Aggregate loads are used to represent all or part of the real and reactive load from one or more loads in the static (power flow) data. This load is usually the aggregation of many individual load devices and the load model is approximate representation of the aggregate response of the load devices to system disturbances. The load model is always applied to individual bus loads (energy consumers) but a single set of load model parameters can used for all loads in the grouping.

    :EnergyConsumer: Energy consumer to which this dynamics load model applies. Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "EnergyConsumer": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, EnergyConsumer = "list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.EnergyConsumer = EnergyConsumer

    def __str__(self):
        str = "class=LoadDynamics\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
