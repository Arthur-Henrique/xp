class Object:

	def __init__(self, **kwargs):
		assert kwargs['name'], 'Name is required'
		self.__dict__.update(kwargs)

	@property
	def type(self):
		return self.__class__.__name__

	def __str__(self):
		pass
		return f"\n\t{self.id}:\t{self.type}, {self.name}"

	def __getitem__(self, key):
		return self.__dict__[key]
