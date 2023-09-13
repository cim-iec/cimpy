from .IdentifiedObject import IdentifiedObject


class ControlAreaGeneratingUnit(IdentifiedObject):
	'''
	A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   It should be noted that only one instance within a control area should reference a specific generating unit.

	:ControlArea: The parent control area for the generating unit specifications. Default: None
	:GeneratingUnit: The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once. Default: None
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'ControlArea': [cgmesProfile.EQ.value, ],
						'GeneratingUnit': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, ControlArea = None, GeneratingUnit = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ControlArea = ControlArea
		self.GeneratingUnit = GeneratingUnit
		
	def __str__(self):
		str = 'class=ControlAreaGeneratingUnit\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
