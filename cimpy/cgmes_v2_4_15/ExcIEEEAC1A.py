from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcIEEEAC1A(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type AC1A model. The model represents the field-controlled alternator-rectifier excitation systems designated Type AC1A. These excitation systems consist of an alternator main exciter with non-controlled rectifiers.  Reference: IEEE Standard 421.5-2005 Section 6.1.

    :ka: Voltage regulator gain (K).  Typical Value = 400. Default: 0.0
    :kc: Rectifier loading factor proportional to commutating reactance (K).  Typical Value = 0.2. Default: 0.0
    :kd: Demagnetizing factor, a function of exciter alternator reactances (K).  Typical Value = 0.38. Default: 0.0
    :ke: Exciter constant related to self-excited field (K).  Typical Value = 1. Default: 0.0
    :kf: Excitation control system stabilizer gains (K).  Typical Value = 0.03. Default: 0.0
    :seve1: Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 0.1. Default: 0.0
    :seve2: Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 0.03. Default: 0.0
    :ta: Voltage regulator time constant (T).  Typical Value = 0.02. Default: 0.0
    :tb: Voltage regulator time constant (T).  Typical Value = 0. Default: 0.0
    :tc: Voltage regulator time constant (T).  Typical Value = 0. Default: 0.0
    :te: Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 0.8. Default: 0.0
    :tf: Excitation control system stabilizer time constant (T).  Typical Value = 1. Default: 0.0
    :vamax: Maximum voltage regulator output (V).  Typical Value = 14.5. Default: 0.0
    :vamin: Minimum voltage regulator output (V).  Typical Value = -14.5. Default: 0.0
    :ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (V).  Typical Value = 4.18. Default: 0.0
    :ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (V).  Typical Value = 3.14. Default: 0.0
    :vrmax: Maximum voltage regulator outputs (V).  Typical Value = 6.03. Default: 0.0
    :vrmin: Minimum voltage regulator outputs (V).  Typical Value = -5.43. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "ka": [Profile.DY.value, ],
        "kc": [Profile.DY.value, ],
        "kd": [Profile.DY.value, ],
        "ke": [Profile.DY.value, ],
        "kf": [Profile.DY.value, ],
        "seve1": [Profile.DY.value, ],
        "seve2": [Profile.DY.value, ],
        "ta": [Profile.DY.value, ],
        "tb": [Profile.DY.value, ],
        "tc": [Profile.DY.value, ],
        "te": [Profile.DY.value, ],
        "tf": [Profile.DY.value, ],
        "vamax": [Profile.DY.value, ],
        "vamin": [Profile.DY.value, ],
        "ve1": [Profile.DY.value, ],
        "ve2": [Profile.DY.value, ],
        "vrmax": [Profile.DY.value, ],
        "vrmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, ka = 0.0, kc = 0.0, kd = 0.0, ke = 0.0, kf = 0.0, seve1 = 0.0, seve2 = 0.0, ta = 0.0, tb = 0.0, tc = 0.0, te = 0.0, tf = 0.0, vamax = 0.0, vamin = 0.0, ve1 = 0.0, ve2 = 0.0, vrmax = 0.0, vrmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ka = ka
        self.kc = kc
        self.kd = kd
        self.ke = ke
        self.kf = kf
        self.seve1 = seve1
        self.seve2 = seve2
        self.ta = ta
        self.tb = tb
        self.tc = tc
        self.te = te
        self.tf = tf
        self.vamax = vamax
        self.vamin = vamin
        self.ve1 = ve1
        self.ve2 = ve2
        self.vrmax = vrmax
        self.vrmin = vrmin

    def __str__(self):
        str = "class=ExcIEEEAC1A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
