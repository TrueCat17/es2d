init -100000 python:
	import os
	sys = os.sys
	
	if 'linux' in sys.platform:
		sys.path.append("./py_libs/linux-i686.so/")
	
	import time
	import random
	import math
	import shutil
	import pickle
	import inspect

