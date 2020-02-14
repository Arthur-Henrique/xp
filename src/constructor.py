from .for_attr import *

class AllArgsInit:
	required = None

	def __init__(self, required=False):
		self.required = required

	def __call__(self, cls):
		def constructor(obj, *args, **kwargs):
			nonPresentArgs = []

			@forAttr(cls=cls)
			def setAttributes(obj, __attr__, *args, **kwargs):
				try:
					setattr(obj, __attr__, kwargs[__attr__])
				except KeyError:
					nonPresentArgs.append(__attr__)

			setAttributes(obj, *args, **kwargs)

			if self.required and nonPresentArgs:
				raise ValueError(str(nonPresentArgs) + ' are required')

		setattr(cls, "__init__", constructor)
		return cls
