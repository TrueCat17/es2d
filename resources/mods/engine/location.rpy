init -1002 python:
	
	location_ext = 'png'
	
	
	location_start_time = 0
	location_fade_time = 0.5
	
	
	location_was_show = True
	def location_showed():
		return location_was_show
	can_exec_next_check_funcs.append(location_showed)
	
	def location_show():
		global location_start_time
		location_start_time = time.time() - location_fade_time * 2
	can_exec_next_skip_funcs.append(location_show)
	
	
	cur_location = None
	cur_location_name = None
	cur_place_name = None
	cur_to_place = None
	
	
	cam_object = None
	cam_object_old = None
	cam_object_start_moving = 0.0
	cam_object_end_moving = 1.0
	cam_object_align = (0.5, 0.5)
	cam_object_align_old = (0.5, 0.5)
	cam_object_zoom = 1.0
	cam_object_zoom_old = 1.0
	
	def cam_to(obj, moving_time = 1.0, align = None, zoom = None):
		global cam_object
		old = cam_object
		
		if isinstance(obj, str):
			if cur_location is None:
				out_msg('cam_to', 'Current location is not defined, need to call set_location')
				return
			place = cur_location.get_place(obj)
			if not place:
				out_msg('cam_to', 'Place <' + obj + '> not found in location <' + cur_location.name + '>')
				return
			cam_object = place
		else:
			cam_object = obj
		
		global cam_object_old, cam_object_start_moving, cam_object_end_moving
		if cam_object is not None:
			cam_object_old = old
			cam_object_start_moving = time.time()
			cam_object_end_moving = time.time() + moving_time
		
		if align is not None:
			global cam_object_align, cam_object_align_old
			if type(align) not in (list, tuple):
				align = {
					'left':   (0.0, 0.5),
					'right':  (1.0, 0.5),
					'up':     (0.5, 0.0),
					'down':   (0.5, 1.0),
					'center': (0.5, 0.5)
				}[align]
			cam_object_align_old = cam_object_align
			cam_object_align = align
		
		if zoom is not None:
			global cam_object_zoom, cam_object_zoom_old
			cam_object_zoom_old = cam_object_zoom
			cam_object_zoom = zoom
	
	
	def cam_object_moved():
		return cam_object_end_moving < time.time()
	can_exec_next_check_funcs.append(cam_object_moved)
	
	def cam_object_move():
		global cam_object_start_moving, location_cutscene_start, cam_object_end_moving, location_cutscene_end
		cam_object_start_moving = location_cutscene_start = 0.0
		cam_object_end_moving = location_cutscene_end = 1.0
	can_exec_next_skip_funcs.append(cam_object_move)
	
	
	location_zoom_main = 1.0
	location_zoom_extra = 1.0
	location_zoom = 1.0 # main * extra
	
	upd_loc_stage_size = None
	def update_location_zoom():
		global upd_loc_stage_size
		if upd_loc_stage_size == get_stage_size():
			return
		stage_width, stage_height = upd_loc_stage_size = get_stage_size()
		
		round_part = 4
		spec_floor = lambda n: math.floor(n * round_part) / round_part
		spec_ceil  = lambda n: math.ceil( n * round_part) / round_part
		
		global location_zoom_main
		location_zoom_main = 1.0
		
		for location_name in locations.keys():
			location = locations[location_name]
			if location.is_room:
				scale = min(stage_width / location.xsize, stage_height / location.ysize) # increase to width OR height
				scale = spec_floor(scale) # round to down
			else:
				scale = max(stage_width / location.xsize, stage_height / location.ysize) # increase to width AND height
				scale = spec_ceil(scale)  # round to up
			
			location_zoom_main = max(location_zoom_main, scale)
		
		if location_zoom_main > 2.5:
			location_zoom_main = 2.5
	
	
	
	locations = dict()
	
	def register_location(name, path_to_images, is_room, xsize, ysize):
		if locations.has_key(name):
			out_msg('register_location', 'Location <' + name + '> already registered')
		else:
			location = Location(name, path_to_images, is_room, xsize, ysize)
			locations[name] = location
	
	def register_place(location_name, place_name, x, y, xsize, ysize, to_side = None):
		if not locations.has_key(location_name):
			out_msg('register_place', 'Location <' + location_name + '> not registered')
			return
		
		location = locations[location_name]
		if location.get_place(place_name):
			out_msg('register_place', 'Place <' + place_name + '> in location <' + self.name + '> already exists')
			return
		
		place = Place(place_name, x, y, xsize, ysize, to_side)
		location.add_place(place, place_name)
	
	def register_exit(location_name, to_location_name, to_place_name, x, y, xsize, ysize):
		if not locations.has_key(location_name):
			out_msg('register_exit', 'Location <' + location_name + '> not registered')
			return
		
		location = locations[location_name]
		exit = Exit(to_location_name, to_place_name, x, y, xsize, ysize)
		location.add_exit(exit)
	
	
	
	def set_location(location_name, place):
		if not locations.has_key(location_name):
			out_msg('set_location', 'Location <' + location_name + '> not registered')
			return
		
		if type(place) is str:
			if not locations[location_name].get_place(place):
				out_msg('set_location', 'Place <' + place + '> in location <' + location_name + '> not found')
				return
		
		if not has_screen('location'):
			show_screen('location')
			show_screen('inventory')
		
		global location_start_time, location_was_show
		location_start_time = time.time()
		location_was_show = False
		
		global cur_location, cur_location_name, cur_to_place
		cur_location = locations[location_name]
		cur_location_name = location_name
		cur_to_place = place
		
		main = cur_location.main()
		real_width, real_height = get_image_size(main)
		reg_width, reg_height = cur_location.xsize, cur_location.ysize
		
		global location_changed, draw_location
		global was_out_exit, cam_object
		if draw_location is None:
			location_start_time -= location_fade_time
			
			location_changed = True
			draw_location = cur_location
			
			was_out_exit = False
			cam_object = me
		else:
			cam_object = {'x': me.x, 'y': me.y}
		
		show_character(me, cur_to_place)
		
		if reg_width != real_width or reg_height != real_height:
			reg_size = str(reg_width) + 'x' + str(reg_height)
			real_size = str(real_width) + 'x' + str(real_height)
			out_msg('set_location', 
					'Location sizes on registration (' + reg_size + ') not equal to real sizes (' + real_size + ')\n' + 
					'Location: <' + cur_location.name + '>\n' + 
					'Main image: <' + main + '>')
	
	def hide_location():
		global cur_location, cur_location_name, cur_to_place
		cur_location = cur_location_name = None
		cur_to_place = None
		
		global draw_location
		draw_location = None
	
	
	
	def get_location_image(obj, directory, name, name_postfix, ext, is_free, need = True):
		if obj.cache is None:
			obj.cache = dict()
		
		mode = times['current_name']
		key = name, name_postfix, mode
		if obj.cache.has_key(key):
			return obj.cache[key]
		
		if name_postfix:
			name_postfix = '_' + name_postfix
		file_name = name + name_postfix
		
		path = directory + file_name + '_' + mode + '.' + ext
		if not os.path.exists(path):
			path = directory + file_name + '.' + ext
			if os.path.exists(path):
				if not is_free:
					r, g, b = location_time_rgb
					path = im.recolor(path, r, g, b)
			else:
				if need:
					out_msg('get_location_image', 'File <' + path + '> not found')
				path = None
		
		obj.cache[key] = path
		return path
	
	
	class Location(Object):
		def __init__(self, name, directory, is_room, xsize, ysize):
			Object.__init__(self)
			
			self.name = name
			self.directory = directory + ('' if directory.endswith('/') else '/')
			
			self.is_room = is_room
			self.xsize, self.ysize = xsize, ysize
			
			self.places = dict()
			self.exits = []
			
			self.objects = []
		
		def main(self):
			return get_location_image(self, self.directory, 'main', '', location_ext, False)
		def over(self):
			return get_location_image(self, self.directory, 'over', '', location_ext, False, False)
		def free(self):
			return get_location_image(self, self.directory, 'free', '', location_ext, True, False)
		
		def preload(self):
			for image in self.main(), self.over(), self.free():
				if image:
					load_image(image)
		
		def add_place(self, place, place_name):
			self.places[place_name] = place
		
		def get_place(self, place_name):
			return self.places.get(place_name, None)
		
		def add_exit(self, exit):
			self.exits.append(exit)
		
		
		def update_pos(self):
			reverse = location_cutscene_state == 'off'
			k = get_k_between(cam_object_start_moving, cam_object_end_moving, time.time(), location_cutscene_state == 'off')
			if cam_object_end_moving < time.time():
				global cam_object_align_old, cam_object_zoom_old
				cam_object_align_old = cam_object_align
				cam_object_zoom_old = cam_object_zoom
			
			if cam_object_old is None or cam_object is None or cam_object_end_moving < time.time():
				if cam_object is None:
					cam_object_x, cam_object_y = 0, 0
				else:
					cam_object_x, cam_object_y = get_place_center(cam_object, cam_object_align)
			else:
				ax = interpolate(cam_object_align_old[0], cam_object_align[0], k, reverse)
				ay = interpolate(cam_object_align_old[1], cam_object_align[1], k, reverse)
				
				from_x, from_y = get_place_center(cam_object_old, (ax, ay))
				to_x, to_y = get_place_center(cam_object, (ax, ay))
				
				cam_object_x = interpolate(from_x, to_x, k)
				cam_object_y = interpolate(from_y, to_y, k)
			
			update_location_zoom()
			global location_zoom_extra, location_zoom
			location_zoom_extra = interpolate(cam_object_zoom_old, cam_object_zoom, k, reverse)
			location_zoom = location_zoom_main * location_zoom_extra
			
			cam_object_x *= location_zoom
			cam_object_y *= location_zoom
			
			
			stage_width = get_stage_width()
			main_width = self.xsize * location_zoom
			if main_width < stage_width or cam_object is None:
				self.x = (stage_width - main_width) / 2
			else:
				xalign = interpolate(cam_object_align_old[0], cam_object_align[0], k, reverse)
				indent = stage_width * xalign
				indent_right = stage_width - indent
				
				if cam_object_x <= indent:
					self.x = 0
				elif cam_object_x >= main_width - indent_right:
					self.x = stage_width - main_width
				else:
					self.x = indent - cam_object_x
			
			stage_height = get_stage_height() - location_cutscene_up - location_cutscene_down
			main_height = self.ysize * location_zoom
			if main_height < stage_height or cam_object is None:
				self.y = (stage_height - main_height) / 2
			else:
				yalign = interpolate(cam_object_align_old[1], cam_object_align[1], k, reverse)
				indent = stage_height * yalign
				indent_down = stage_height - indent
				
				if cam_object_y <= indent:
					self.y = 0
				elif cam_object_y >= main_height - indent_down :
					self.y = stage_height - main_height
				else:
					self.y = indent - cam_object_y
			self.y += location_cutscene_up
			
			self.x = int(round(self.x))
			self.y = int(round(self.y))
	
	
	class Place(Object):
		def __init__(self, name, x, y, xsize, ysize, to_side):
			Object.__init__(self)
			self.name = name
			self.x, self.y = x, y
			self.xsize, self.ysize = xsize, ysize
			self.to_side = to_side
		
		def inside(self, x, y):
			return self.x <= x and x <= self.x + self.xsize and self.y <= y and y <= self.y + self.ysize
	
	class Exit(Object):
		def __init__(self, to_location_name, to_place_name, x, y, xsize, ysize):
			Object.__init__(self)
			self.to_location_name = to_location_name
			self.to_place_name = to_place_name
			self.x, self.y = x, y
			self.xsize, self.ysize = xsize, ysize
		
		def inside(self, x, y):
			return self.x <= x and x <= self.x + self.xsize and self.y <= y and y <= self.y + self.ysize
	
	
	def get_place_center(place, align = (0.5, 0.5)):
		x, y = place['x'], place['y']
		
		w = place['xsize'] if place.has_key('xsize') else 0
		h = place['ysize'] if place.has_key('ysize') else 0
		
		xa = get_absolute(place['xanchor'], w) if place.has_key('xanchor') else 0
		ya = get_absolute(place['yanchor'], h) if place.has_key('yanchor') else 0
		
		return (x - xa + align[0] * w), (y - ya + align[1] * h)
	
	
	exec_action = False
	was_out_exit = False
	was_out_place = False
	
	def get_location_exit():
		global was_out_exit, was_out_place
		
		for exit in cur_location.exits:
			if exit.inside(me.x, me.y):
				if not was_out_exit:
					continue
				
				can_exit = not globals().has_key('can_exit_to') or can_exit_to(exit.to_location_name, exit.to_place_name)
				if can_exit:
					was_out_exit = False
					was_out_place = True
					return exit
				return None
		else:
			was_out_exit = True
		
		return None
	
	def get_location_place():
		global exec_action, was_out_place
		
		for place_name in cur_location.places.keys():
			place = cur_location.places[place_name]
			if place.inside(me.x, me.y):
				if was_out_place:
					exec_action = False
				if exec_action or was_out_place:
					was_out_place = False
					return place_name
				return None
		else:
			was_out_place = True
		
		return None
	

