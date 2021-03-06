init 10 python:
	db_font = 'FixEx3'
	
	was = []
	day_num = 0
	
	def get_place_labels():
		usual_label = cur_location_name + '__' + (cur_place_name or 'unknown')
		
		res = []
		for quest in get_started_quests():
			res.extend(get_glob_labels(quest + '__' + usual_label))
		res.extend(get_glob_labels('day' + str(day_num) + '__' + usual_label))
		res.extend(get_glob_labels(usual_label))
		return res
	
	
	gate_right = get_location_objects('enter', None, 'gate_right')[0]
	gate_right.start_animation('open')
	gate_right.update_location_paths()

init 25 python:
	limit_camp_out()
	limit_rooms()
	
	def spec_start():
		global day_num
		day_num = 1
		
		init_characters()
		
		set_rpg_control(True)
		set_location('enter', 'before_gates')# {'x': 250, 'y': 250})
		me.set_dress('sport')
		
		if 1:
			characters_auto(False)
			
			show_character(mi, me)
			print mi.move_to_place(['clubs', 'enter'])


label start:
	#call day0_start
	call day1_start
	#$ spec_start()
	
	call rpg_loop
