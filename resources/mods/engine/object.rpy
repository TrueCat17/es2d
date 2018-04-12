init -100000 python:
	persistent_updates = False
	
	class Object:
		def __init__(self, obj = None, **kwords):
			self.in_persistent = False
			
			if obj is not None:
				for k in obj.__dict__.keys():
					self.__dict__[k] = obj.__dict__[k]
			for k in kwords.keys():
				self.__dict__[k] = kwords[k]
		
		
		def has_key(self, attr):
			return self.__dict__.has_key(attr)
		def has_attr(self, attr):
			return self.__dict__.has_key(attr)
		
		def __getattr__(self, attr):
			if self.__dict__.has_key(attr) or persistent_updates:
				return self.__dict__[attr]
			return None
		
		def __setattr__(self, attr, value):
			self.__dict__[attr] = value
			
			if self.in_persistent:
				if isinstance(value, Object):
					value.in_persistent = True
					
				global persistent_need_save
				persistent_need_save = True
		
		def __delattr__(self, attr):
			del self.__dict__[attr]
			if self.in_persistent:
				global persistent_need_save
				persistent_need_save = True
		
		def __getitem__(self, item):
			return self.__getattr__(item)
		def __setitem__(self, item, value):
			self.__setattr__(item, value)
		def __delitem__(self, item):
			self.__delattr__(item)
		
		
		def __nonzero__(self):
			return True
		def __str__(self):
			return '<Object ' + str(type(self)) + '>'
		def __repr__(self):
			return str(self)
		def __hash__(self):
			return hash(object.__repr__(self))
		
		def __eq__(self, other):
			return self is other
		
		def get_props(self):
			keys = self.__dict__.keys()
			keys.remove('in_persistent')
			
			return ' '.join(keys)
		
		
		# for pickle
		def __getstate__(self):
			return self.__dict__
		def __setstate__(self, new_dict):
			self.__dict__.update(new_dict)

