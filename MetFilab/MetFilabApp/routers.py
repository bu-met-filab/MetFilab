
class DbRouter(object):
	"""This is for Django Multi-Db"""
		
	def db_for_read(self, model, **hints):
		if model._meta.app_label == 'filab':
			return 'filab'

		if model._meta.app_label == 'filab_brazil':
			return 'filab_brazil'

		return 'default'


	def db_for_write(self, model, **hints):
		if model._meta.app_label == 'filab':
			return 'filab'

		if model._meta.app_label == 'filab_brazil':
			return 'filab_brazil'

		return 'default'

	def allow_relation(self, obj1, obj2, **hints):
		if obj1._meta.app_label == obj2._meta.app_label:
			return True
		return False

	def allow_migrate(self, db, app_label, model=None, **hints):
		if app_label == 'filab':
			return False

		if app_label == 'filab_brazil':
			return False

		return True