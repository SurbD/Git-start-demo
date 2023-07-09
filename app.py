import os

class AppInit(object):
	active = True

	def __init__(self, instance):
		self.instance = instance if self.active else None

	def __repr__(self):
		return f"AppInit(<{self.instance}>)"

