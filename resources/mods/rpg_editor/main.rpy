init 1 python:
	set_fps(60)
	start_screens = 'all_locations'
	
	need_save_locations = False
	save_counter = 0
	set_save_locations = SetVariable('need_save_locations', True)
	
#	clear()
	register_new_locations()
	
	for location_name in locations:
		location = locations[location_name]
		location.using = location.x is not None and location.y is not None
		
		for place_name in location.places:
			place = location.places[place_name]
			px, py, pw, ph = place.x, place.y, place.width, place.height
			
			for exit in location.exits:
				if exit.to_place_name != location_name:
					continue
				
				ex, ey, ew, eh = exit.x, exit.y, exit.width, exit.height
				
				if px == ex and pw == ew:
					if py + ph == ey:
						place.side_exit = 'down'
					elif ey + eh == py:
						place.side_exit = 'up'
						place.y -= eh
					place.height += eh
					location.exits.remove(exit)
					break
				elif py == ey and ph == eh:
					if px + pw == ex:
						place.side_exit = 'right'
					elif ex + ew == px:
						place.side_exit = 'left'
						place.x -= ew
					place.width += ew
					location.exits.remove(exit)
					break


label start:
	while True:
		python:
			save_counter += 1
			if save_counter % 10 == 0 and need_save_locations:
				need_save_locations = False
				save()
		
		pause 0.1

