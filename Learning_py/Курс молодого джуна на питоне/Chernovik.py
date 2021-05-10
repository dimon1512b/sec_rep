class NonPositiveError(Exception):
	pass


class PositiveList(list):
	def append(self, x):
		if x < 0:
			raise NonPositiveError()
		else:
			super(PositiveList, self).append(x)


lst = PositiveList()
lst.append(25)
lst.append(20)
lst.append(10)
print(lst)
