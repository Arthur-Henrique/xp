def at(context):
	class At:
		func = context
		def __rmatmul__(self, arg):
			return self.func(arg)

	return At()
