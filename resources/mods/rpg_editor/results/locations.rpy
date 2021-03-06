init python:
	
	register_location("admin", "images/locations/admin/", False, 1376, 1344)
	register_place(   "admin", "bench_left_pos", 870, 455, 2, 2)
	register_place(   "admin", "closed-1", 420, 750, 120, 30)
	register_place(   "admin", "closed-2", 670, 630, 40, 70)
	register_place(   "admin", "closed-3", 1015, 315, 55, 30)
	register_place(   "admin", "lamp_pos-1", 977, 372, 2, 2)
	register_place(   "admin", "lamp_pos-2", 977, 540, 2, 2)
	register_place(   "admin", "lamp_pos-3", 978, 987, 2, 2)
	register_place(   "admin", "lamp_pos-4", 611, 987, 2, 2)
	register_place(   "admin", "lamp_pos-5", 348, 987, 2, 2)
	register_place(   "admin", "clubs", 0, 990, 40, 120, to=["left", "clubs", "admin"])
	register_place(   "admin", "square", 1336, 990, 40, 120, to=["right", "square", "admin"])
	
	register_location("bath", "images/locations/bath/", False, 647, 1000)
	register_place(   "bath", "bath_rails_left_pos", 304, 587, 2, 2)
	register_place(   "bath", "bath_rails_right_pos", 432, 587, 2, 2)
	register_place(   "bath", "crossroad", 180, 960, 190, 40, to=["down", "crossroad", "bath"])
	
	register_location("beach", "images/locations/beach/", False, 1792, 1408)
	register_place(   "beach", "boat_station", 0, 328, 40, 150, to=["left", "boat_station", "beach"])
	register_place(   "beach", "stadium", 800, 0, 350, 40, to=["up", "stadium", "beach"])
	
	register_location("boat_station", "images/locations/boat_station/", False, 1536, 1664)
	register_place(   "boat_station", "closed-1", 520, 405, 70, 30)
	register_place(   "boat_station", "closed-2", 892, 1210, 35, 20)
	register_place(   "boat_station", "closed-3", 995, 1210, 35, 20)
	register_place(   "boat_station", "closed-4", 1085, 1210, 35, 20)
	register_place(   "boat_station", "closed-5", 1150, 1210, 35, 20)
	register_place(   "boat_station", "pier_start", 410, 700, 10, 10)
	register_place(   "boat_station", "pier_start_sit", 440, 770, 10, 10)
	register_place(   "boat_station", "sand_down", 1020, 610, 100, 40)
	register_place(   "boat_station", "beach", 1496, 350, 40, 255, to=["right", "beach", "boat_station"])
	register_place(   "boat_station", "houses_2", 0, 540, 40, 320, to=["left", "houses_2", "boat_station"])
	register_place(   "boat_station", "square", 370, 0, 90, 40, to=["up", "square", "boat_station"])
	
	register_location("bunker", "images/locations/bunker/", True, 276, 253)
	register_place(   "bunker", "bunker_enter", 60, 223, 70, 30, to=["down", "bunker_enter", "bunker"])
	register_place(   "bunker", "old_camp", 160, 223, 40, 30, to=["down", "old_camp", "bunker"])
	
	register_location("bunker_enter", "images/locations/bunker_enter/", True, 130, 258)
	register_place(   "bunker_enter", "bunker", 30, 95, 70, 30, to=["up", "bunker", "bunker_enter"])
	
	register_location("canteen", "images/locations/canteen/", True, 1152, 832)
	register_place(   "canteen", "canteen_column_back_pos-1", 143, 319, 2, 2)
	register_place(   "canteen", "canteen_column_back_pos-2", 431, 319, 2, 2)
	register_place(   "canteen", "canteen_column_back_pos-3", 655, 319, 2, 2)
	register_place(   "canteen", "canteen_column_pos-1", 143, 607, 2, 2)
	register_place(   "canteen", "canteen_column_pos-2", 431, 607, 2, 2)
	register_place(   "canteen", "canteen_column_pos-3", 655, 607, 2, 2)
	register_place(   "canteen", "canteen_door_pos", 948, 734, 2, 2)
	register_place(   "canteen", "chair_backward_pos-01", 660, 689, 2, 2)
	register_place(   "canteen", "chair_backward_pos-02", 694, 689, 2, 2)
	register_place(   "canteen", "chair_backward_pos-03", 742, 689, 2, 2)
	register_place(   "canteen", "chair_backward_pos-04", 776, 689, 2, 2)
	register_place(   "canteen", "chair_backward_pos-05", 824, 689, 2, 2)
	register_place(   "canteen", "chair_backward_pos-06", 858, 689, 2, 2)
	register_place(   "canteen", "chair_backward_pos-07", 660, 513, 2, 2)
	register_place(   "canteen", "chair_backward_pos-08", 694, 513, 2, 2)
	register_place(   "canteen", "chair_backward_pos-09", 742, 513, 2, 2)
	register_place(   "canteen", "chair_backward_pos-10", 776, 513, 2, 2)
	register_place(   "canteen", "chair_backward_pos-11", 824, 513, 2, 2)
	register_place(   "canteen", "chair_backward_pos-12", 858, 513, 2, 2)
	register_place(   "canteen", "chair_forward_pos-01", 660, 722, 2, 2)
	register_place(   "canteen", "chair_forward_pos-02", 694, 722, 2, 2)
	register_place(   "canteen", "chair_forward_pos-03", 742, 722, 2, 2)
	register_place(   "canteen", "chair_forward_pos-04", 776, 722, 2, 2)
	register_place(   "canteen", "chair_forward_pos-05", 824, 722, 2, 2)
	register_place(   "canteen", "chair_forward_pos-06", 858, 722, 2, 2)
	register_place(   "canteen", "chair_forward_pos-07", 660, 546, 2, 2)
	register_place(   "canteen", "chair_forward_pos-08", 694, 546, 2, 2)
	register_place(   "canteen", "chair_forward_pos-09", 742, 546, 2, 2)
	register_place(   "canteen", "chair_forward_pos-10", 776, 546, 2, 2)
	register_place(   "canteen", "chair_forward_pos-11", 824, 546, 2, 2)
	register_place(   "canteen", "chair_forward_pos-12", 858, 546, 2, 2)
	register_place(   "canteen", "table_h_pos-1", 677, 705, 2, 2)
	register_place(   "canteen", "table_h_pos-2", 759, 705, 2, 2)
	register_place(   "canteen", "table_h_pos-3", 841, 705, 2, 2)
	register_place(   "canteen", "table_h_pos-4", 677, 529, 2, 2)
	register_place(   "canteen", "table_h_pos-5", 759, 529, 2, 2)
	register_place(   "canteen", "table_h_pos-6", 841, 529, 2, 2)
	register_place(   "canteen", "square", 640, 802, 55, 30, to=["down", "square", "canteen"])
	
	register_location("clubs", "images/locations/clubs/", False, 1152, 1664)
	register_place(   "clubs", "before_clubs", 340, 1190, 50, 130)
	register_place(   "clubs", "before_porch", 447, 1280, 2, 2)
	register_place(   "clubs", "closed", 100, 1530, 20, 60)
	register_place(   "clubs", "cluster", 200, 1300, 2, 2)
	register_place(   "clubs", "mus_club_column_pos-1", 773, 400, 2, 2)
	register_place(   "clubs", "mus_club_column_pos-2", 836, 400, 2, 2)
	register_place(   "clubs", "mus_club_column_pos-3", 899, 400, 2, 2)
	register_place(   "clubs", "mus_club_column_pos-4", 962, 400, 2, 2)
	register_place(   "clubs", "mus_club_column_pos-5", 1025, 400, 2, 2)
	register_place(   "clubs", "mus_club_rails_pos-1", 804, 400, 2, 2)
	register_place(   "clubs", "mus_club_rails_pos-2", 867, 400, 2, 2)
	register_place(   "clubs", "mus_club_rails_pos-3", 930, 400, 2, 2)
	register_place(   "clubs", "mus_club_rails_pos-4", 1056, 400, 2, 2)
	register_place(   "clubs", "porch", 447, 1200, 2, 2)
	register_place(   "clubs", "porch_cleft", 425, 1200, 2, 2)
	register_place(   "clubs", "porch_left", 410, 1200, 2, 2)
	register_place(   "clubs", "toilet", 340, 670, 120, 30)
	register_place(   "clubs", "admin", 1112, 1190, 40, 130, to=["right", "admin", "clubs"])
	register_place(   "clubs", "enter", 0, 1190, 40, 130, to=["left", "enter", "clubs"])
	register_place(   "clubs", "houses_2", 780, 1624, 100, 40, to=["down", "houses_2", "clubs"])
	register_place(   "clubs", "mus_club", 970, 340, 50, 30, to=["up", "mus_club", "clubs"])
	register_place(   "clubs", "radio_club", 390, 1120, 120, 30, to=["up", "radio_club", "clubs"])
	register_place(   "clubs", "washbasins", 620, 0, 145, 40, to=["up", "washbasins", "clubs"])
	
	register_location("crossroad", "images/locations/crossroad/", False, 700, 700)
	register_place(   "crossroad", "bath", 305, 0, 80, 40, to=["up", "bath", "crossroad"])
	register_place(   "crossroad", "houses_1", 660, 335, 40, 70, to=["right", "houses_1", "crossroad"])
	register_place(   "crossroad", "washbasins", 0, 335, 40, 70, to=["left", "washbasins", "crossroad"])
	
	register_location("enter", "images/locations/enter/", False, 960, 992)
	register_place(   "enter", "before_gates", 415, 305, 130, 50)
	register_place(   "enter", "before_gates_close", 415, 210, 130, 80)
	register_place(   "enter", "behind_gates", 415, 250, 130, 10)
	register_place(   "enter", "bench_desc", 530, 450, 60, 60)
	register_place(   "enter", "bench_right_place", 555, 500, 10, 10)
	register_place(   "enter", "dream_start", 540, 460, 10, 40)
	register_place(   "enter", "gate_left_pos", 449, 279, 2, 2)
	register_place(   "enter", "gate_right_pos", 509, 279, 2, 2)
	register_place(   "enter", "ikarus_place", 293, 590, 2, 2)
	register_place(   "enter", "lamp_desc", 400, 480, 50, 40)
	register_place(   "enter", "lamp_place", 420, 495, 10, 10)
	register_place(   "enter", "sign", 370, 380, 60, 40)
	register_place(   "enter", "square_center", 460, 460, 40, 40)
	register_place(   "enter", "square_down", 460, 840, 40, 40)
	register_place(   "enter", "uv_dream_place", 473, 263, 2, 2)
	register_place(   "enter", "clubs", 410, 0, 140, 40, to=["up", "clubs", "enter", to_right])
	register_place(   "enter", "forest_path-5", 920, 565, 40, 160, to=["right", "forest_path-5", "enter", to_back])
	register_place(   "enter", "forest_path-9", 0, 555, 40, 160, to=["left", "forest_path-9", "enter", to_forward])
	register_place(   "enter", "ikarus", 400, 590, 40, 30, to=["up", "ikarus", "enter"])
	
	register_location("flat", "images/locations/flat/", True, 192, 272)
	register_place(   "flat", "armchair_pos", 80, 143, 2, 2)
	register_place(   "flat", "bed", 130, 155, 20, 70)
	register_place(   "flat", "before_window", 125, 110, 40, 30)
	register_place(   "flat", "books", 30, 132, 20, 25)
	register_place(   "flat", "center", 70, 170, 40, 40)
	register_place(   "flat", "computer", 60, 135, 70, 20)
	register_place(   "flat", "dress_place", 161, 260, 2, 2)
	register_place(   "flat", "dust_place", 130, 80, 30, 70)
	register_place(   "flat", "exit", 23, 252, 30, 20)
	register_place(   "flat", "lamp_light_pos", 109, 112, 2, 2)
	register_place(   "flat", "monitor_pos", 80, 94, 2, 2)
	register_place(   "flat", "table", 30, 175, 20, 30)
	register_place(   "flat", "to_dress", 140, 245, 30, 27)
	register_place(   "flat", "window", 65, 25, 100, 60)
	
	register_location("forest_path-1", "images/locations/forest_path-1/", False, 1088, 832)
	register_place(   "forest_path-1", "forest_path-2", 720, 0, 120, 40, to=["up", "forest_path-2", "forest_path-1"])
	register_place(   "forest_path-1", "left", 0, 690, 40, 90, to=["left", "forest_path-1", "right"])
	register_place(   "forest_path-1", "old_camp", 605, 792, 110, 40, to=["down", "old_camp", "forest_path-1", to_forward])
	register_place(   "forest_path-1", "right", 1048, 120, 40, 60, to=["right", "forest_path-1", "left"])
	
	register_location("forest_path-2", "images/locations/forest_path-2/", False, 768, 576)
	register_place(   "forest_path-2", "forest_path-1", 120, 536, 80, 40, to=["down", "forest_path-1", "forest_path-2"])
	register_place(   "forest_path-2", "forest_path-3", 728, 270, 40, 90, to=["right", "forest_path-3", "forest_path-2"])
	
	register_location("forest_path-3", "images/locations/forest_path-3/", False, 640, 416)
	register_place(   "forest_path-3", "forest_path-2", 0, 310, 40, 60, to=["left", "forest_path-2", "forest_path-3"])
	register_place(   "forest_path-3", "houses_2", 500, 0, 90, 40, to=["up", "houses_2", "forest_path-3"])
	
	register_location("forest_path-4", "images/locations/forest_path-4/", False, 544, 416)
	register_place(   "forest_path-4", "forest_path-5", 120, 0, 180, 40, to=["up", "forest_path-5", "forest_path-4"])
	register_place(   "forest_path-4", "forest_path-9", 120, 376, 180, 40, to=["down", "forest_path-9", "forest_path-4"])
	
	register_location("forest_path-5", "images/locations/forest_path-5/", False, 544, 416)
	register_place(   "forest_path-5", "enter", 120, 0, 180, 40, to=["up", "enter", "forest_path-5", to_left])
	register_place(   "forest_path-5", "forest_path-4", 120, 376, 180, 40, to=["down", "forest_path-4", "forest_path-5"])
	register_place(   "forest_path-5", "stadium", 504, 215, 40, 145, to=["right", "stadium", "forest_path-5", to_left])
	
	register_location("forest_path-6", "images/locations/forest_path-6/", False, 544, 416)
	register_place(   "forest_path-6", "forest_path-7", 504, 210, 40, 90, to=["right", "forest_path-7", "forest_path-6"])
	register_place(   "forest_path-6", "left", 0, 120, 40, 80, to=["left", "forest_path-6", "up", to_back])
	register_place(   "forest_path-6", "tennis", 150, 376, 90, 40, to=["down", "tennis", "forest_path-6"])
	register_place(   "forest_path-6", "up", 310, 0, 90, 40, to=["up", "forest_path-6", "left", to_right])
	
	register_location("forest_path-7", "images/locations/forest_path-7/", False, 544, 416)
	register_place(   "forest_path-7", "forest_path-6", 0, 180, 40, 90, to=["left", "forest_path-6", "forest_path-7"])
	register_place(   "forest_path-7", "forest_path-8", 220, 376, 80, 40, to=["down", "forest_path-8", "forest_path-7"])
	register_place(   "forest_path-7", "right", 504, 80, 40, 90, to=["right", "forest_path-7", "up", to_back])
	register_place(   "forest_path-7", "up", 210, 0, 90, 40, to=["up", "forest_path-7", "right", to_left])
	
	register_location("forest_path-8", "images/locations/forest_path-8/", False, 544, 416)
	register_place(   "forest_path-8", "down", 210, 376, 90, 40, to=["down", "forest_path-8", "right", to_left])
	register_place(   "forest_path-8", "forest_path-7", 400, 0, 100, 40, to=["up", "forest_path-7", "forest_path-8"])
	register_place(   "forest_path-8", "right", 504, 120, 40, 90, to=["right", "forest_path-8", "down", to_forward])
	register_place(   "forest_path-8", "tennis", 0, 210, 40, 90, to=["left", "tennis", "forest_path-8"])
	
	register_location("forest_path-9", "images/locations/forest_path-9/", False, 544, 416)
	register_place(   "forest_path-9", "enter", 120, 376, 180, 40, to=["down", "enter", "forest_path-9", to_right])
	register_place(   "forest_path-9", "forest_path-4", 120, 0, 180, 40, to=["up", "forest_path-4", "forest_path-9"])
	
	register_location("hospital", "images/locations/hospital/", True, 224, 256)
	register_place(   "hospital", "library_and_hospital", 120, 226, 34, 30, to=["down", "library_and_hospital", "hospital"])
	
	register_location("house_dv", "images/locations/house_dv/", True, 512, 512)
	register_place(   "house_dv", "houses_2", 250, 386, 55, 30, to=["down", "houses_2", "house_dv"])
	
	register_location("house_mt", "images/locations/house_mt/", True, 512, 512)
	register_place(   "house_mt", "houses_1", 209, 400, 54, 30, to=["down", "houses_1", "house_mt"])
	
	register_location("house_sl", "images/locations/house_sl/", True, 512, 512)
	register_place(   "house_sl", "houses_1", 229, 378, 54, 30, to=["down", "houses_1", "house_sl"])
	
	register_location("house_un", "images/locations/house_un/", True, 512, 512)
	register_place(   "house_un", "houses_1", 229, 378, 54, 30, to=["down", "houses_1", "house_un"])
	
	register_location("houses_1", "images/locations/houses_1/", False, 1632, 1152)
	register_place(   "houses_1", "house-01", 130, 980, 60, 20)
	register_place(   "houses_1", "house-02", 355, 980, 55, 20)
	register_place(   "houses_1", "house-04", 770, 980, 60, 20)
	register_place(   "houses_1", "house-05", 1090, 980, 60, 20)
	register_place(   "houses_1", "house-06", 1380, 980, 55, 20)
	register_place(   "houses_1", "house-07", 165, 660, 55, 20)
	register_place(   "houses_1", "house-08", 390, 660, 55, 20)
	register_place(   "houses_1", "house-09", 770, 660, 60, 20)
	register_place(   "houses_1", "house-10", 963, 660, 60, 20)
	register_place(   "houses_1", "house-11", 1220, 660, 60, 20)
	register_place(   "houses_1", "house-14", 450, 340, 60, 20)
	register_place(   "houses_1", "house-15", 675, 340, 55, 20)
	register_place(   "houses_1", "house-16", 870, 340, 55, 20)
	register_place(   "houses_1", "house_sh", 550, 980, 55, 20)
	register_place(   "houses_1", "crossroad", 0, 700, 40, 70, to=["left", "crossroad", "houses_1"])
	register_place(   "houses_1", "house_mt", 1085, 350, 70, 30, to=["up", "house_mt", "houses_1"])
	register_place(   "houses_1", "house_sl", 1405, 660, 70, 30, to=["up", "house_sl", "houses_1"])
	register_place(   "houses_1", "house_un", 190, 340, 70, 30, to=["up", "house_un", "houses_1"])
	register_place(   "houses_1", "lib_and_hosp-up", 1592, 700, 40, 70, to=["right", "library_and_hospital", "houses_1-up"])
	register_place(   "houses_1", "library_and_hospital", 1592, 1020, 40, 110, to=["right", "library_and_hospital", "houses_1"])
	register_place(   "houses_1", "square", 827, 1112, 520, 40, to=["down", "square", "houses_1"])
	
	register_location("houses_2", "images/locations/houses_2/", False, 2112, 1920)
	register_place(   "houses_2", "house-18", 960, 340, 60, 20)
	register_place(   "houses_2", "house-20", 1380, 340, 60, 20)
	register_place(   "houses_2", "house-21", 1600, 340, 65, 20)
	register_place(   "houses_2", "house-22", 480, 790, 60, 20)
	register_place(   "houses_2", "house-23", 640, 800, 60, 20)
	register_place(   "houses_2", "house-24", 870, 790, 55, 20)
	register_place(   "houses_2", "house-25", 1090, 790, 60, 20)
	register_place(   "houses_2", "house-26", 1345, 790, 60, 20)
	register_place(   "houses_2", "house-27", 1570, 790, 60, 20)
	register_place(   "houses_2", "house-28", 385, 1235, 60, 20)
	register_place(   "houses_2", "house-29", 575, 1235, 65, 20)
	register_place(   "houses_2", "house-30", 800, 1235, 60, 20)
	register_place(   "houses_2", "toilet", 1330, 1115, 120, 30)
	register_place(   "houses_2", "boat_station", 2072, 1080, 40, 170, to=["right", "boat_station", "houses_2"])
	register_place(   "houses_2", "clubs", 540, 0, 130, 40, to=["up", "clubs", "houses_2"])
	register_place(   "houses_2", "forest_path-3", 160, 1880, 100, 40, to=["down", "forest_path-3", "houses_2"])
	register_place(   "houses_2", "house_dv", 1180, 340, 70, 30, to=["up", "house_dv", "houses_2"])
	register_place(   "houses_2", "square", 1921, 0, 130, 40, to=["up", "square", "houses_2"])
	
	register_location("ikarus", "images/locations/ikarus/", True, 478, 154)
	register_place(   "ikarus", "before_sit_place", 409, 76, 2, 2)
	register_place(   "ikarus", "before_sit_place-2", 410, 100, 10, 10)
	register_place(   "ikarus", "sit_place", 397, 71, 2, 2)
	register_place(   "ikarus", "enter", 407, 124, 30, 30, to=["down", "enter", "ikarus"])
	
	register_location("liaz", "images/locations/liaz/", True, 432, 216)
	register_place(   "liaz", "liaz_bench_left_pos1", 58, 131, 2, 2)
	register_place(   "liaz", "liaz_bench_left_pos2", 58, 207, 2, 2)
	register_place(   "liaz", "liaz_bench_left_pos3", 405, 127, 2, 2)
	register_place(   "liaz", "liaz_bench_middle_pos", 18, 142, 2, 2)
	register_place(   "liaz", "liaz_bench_right_pos1", 84, 131, 2, 2)
	register_place(   "liaz", "liaz_bench_right_pos10", 261, 127, 2, 2)
	register_place(   "liaz", "liaz_bench_right_pos11", 307, 127, 2, 2)
	register_place(   "liaz", "liaz_bench_right_pos12", 352, 127, 2, 2)
	register_place(   "liaz", "liaz_bench_right_pos2", 84, 207, 2, 2)
	register_place(   "liaz", "liaz_bench_right_pos3", 160, 207, 2, 2)
	register_place(   "liaz", "liaz_bench_right_pos4", 205, 207, 2, 2)
	register_place(   "liaz", "liaz_bench_right_pos5", 245, 207, 2, 2)
	register_place(   "liaz", "liaz_bench_right_pos6", 283, 207, 2, 2)
	register_place(   "liaz", "liaz_bench_right_pos7", 128, 127, 2, 2)
	register_place(   "liaz", "liaz_bench_right_pos8", 173, 127, 2, 2)
	register_place(   "liaz", "liaz_bench_right_pos9", 218, 127, 2, 2)
	register_place(   "liaz", "liaz_chair_forward_pos", 408, 208, 2, 2)
	register_place(   "liaz", "liaz_enter", 320, 196, 70, 20)
	register_place(   "liaz", "lights_place", 0, 10, 432, 60)
	
	register_location("library", "images/locations/library/", True, 384, 512)
	register_place(   "library", "cupboard_1_pos", 214, 389, 2, 2)
	register_place(   "library", "cupboard_2_pos", 214, 317, 2, 2)
	register_place(   "library", "cupboard_3_pos", 215, 248, 2, 2)
	register_place(   "library", "library_and_hospital", 240, 470, 55, 40, to=["down", "library_and_hospital", "library"])
	
	register_location("library_and_hospital", "images/locations/library_and_hospital/", False, 1408, 1312)
	register_place(   "library_and_hospital", "closed", 715, 300, 90, 40)
	register_place(   "library_and_hospital", "hospital", 633, 875, 50, 40, to=["up", "hospital", "library_and_hospital"])
	register_place(   "library_and_hospital", "houses_1", 0, 1050, 40, 110, to=["left", "houses_1", "library_and_hospital"])
	register_place(   "library_and_hospital", "houses_1-up", 0, 725, 40, 80, to=["left", "houses_1", "lib_and_hosp-up"])
	register_place(   "library_and_hospital", "library", 1120, 450, 60, 40, to=["up", "library", "library_and_hospital"])
	register_place(   "library_and_hospital", "scene", 510, 0, 70, 40, to=["up", "scene", "library_and_hospital"])
	register_place(   "library_and_hospital", "tennis", 1368, 470, 40, 110, to=["right", "tennis", "library_and_hospital"])
	
	register_location("mus_club", "images/locations/mus_club/", True, 224, 272)
	register_place(   "mus_club", "mus_club_microphone_pos", 60, 220, 2, 2)
	register_place(   "mus_club", "stand_pos", 110, 230, 2, 2)
	register_place(   "mus_club", "clubs", 130, 242, 55, 30, to=["down", "clubs", "mus_club"])
	
	register_location("old_camp", "images/locations/old_camp/", False, 2070, 1740)
	register_place(   "old_camp", "bunker", 820, 645, 40, 40, to=["up", "bunker", "old_camp"])
	register_place(   "old_camp", "forest_path-1", 1150, 1700, 190, 40, to=["down", "forest_path-1", "old_camp", to_forward])
	
	register_location("radio_club", "images/locations/radio_club/", True, 310, 247)
	register_place(   "radio_club", "clubs", 218, 205, 55, 40, to=["down", "clubs", "radio_club"])
	register_place(   "radio_club", "radio_storeroom", 273, 185, 34, 30, to=["right", "radio_storeroom", "radio_club", to_left])
	
	register_location("radio_storeroom", "images/locations/radio_storeroom/", True, 162, 247)
	register_place(   "radio_storeroom", "radio_club", 99, 217, 30, 30, to=["down", "radio_club", "radio_storeroom", to_left])
	
	register_location("scene", "images/locations/scene/", False, 960, 992)
	register_place(   "scene", "closed-1", 237, 115, 40, 20)
	register_place(   "scene", "closed-2", 80, 290, 60, 30)
	register_place(   "scene", "library_and_hospital", 400, 952, 150, 40, to=["down", "library_and_hospital", "scene"])
	
	register_location("square", "images/locations/square/", False, 1824, 1344)
	register_place(   "square", "bench_left_pos-1", 204, 319, 2, 2)
	register_place(   "square", "bench_left_pos-2", 204, 542, 2, 2)
	register_place(   "square", "bench_left_pos-3", 204, 767, 2, 2)
	register_place(   "square", "bench_right_pos-1", 685, 319, 2, 2)
	register_place(   "square", "bench_right_pos-2", 685, 542, 2, 2)
	register_place(   "square", "bench_right_pos-3", 685, 767, 2, 2)
	register_place(   "square", "car_pos", 1223, 846, 2, 2)
	register_place(   "square", "closed", 1580, 680, 120, 30)
	register_place(   "square", "lamp_pos-1", 206, 274, 2, 2)
	register_place(   "square", "lamp_pos-10", 976, 737, 2, 2)
	register_place(   "square", "lamp_pos-11", 1705, 937, 2, 2)
	register_place(   "square", "lamp_pos-2", 206, 497, 2, 2)
	register_place(   "square", "lamp_pos-3", 206, 722, 2, 2)
	register_place(   "square", "lamp_pos-4", 206, 950, 2, 2)
	register_place(   "square", "lamp_pos-5", 680, 274, 2, 2)
	register_place(   "square", "lamp_pos-6", 680, 497, 2, 2)
	register_place(   "square", "lamp_pos-7", 680, 722, 2, 2)
	register_place(   "square", "lamp_pos-8", 680, 950, 2, 2)
	register_place(   "square", "lamp_pos-9", 312, 1292, 2, 2)
	register_place(   "square", "washbasin_left_pos-1", 204, 432, 2, 2)
	register_place(   "square", "washbasin_left_pos-2", 204, 671, 2, 2)
	register_place(   "square", "washbasin_right_pos-1", 687, 432, 2, 2)
	register_place(   "square", "washbasin_right_pos-2", 688, 671, 2, 2)
	register_place(   "square", "admin", 0, 940, 40, 120, to=["left", "admin", "square"])
	register_place(   "square", "boat_station", 310, 1304, 100, 40, to=["down", "boat_station", "square"])
	register_place(   "square", "canteen", 1187, 655, 80, 20, to=["up", "canteen", "square"])
	register_place(   "square", "houses_1", 190, 0, 510, 40, to=["up", "houses_1", "square"])
	register_place(   "square", "houses_2", 20, 1304, 100, 40, to=["down", "houses_2", "square"])
	register_place(   "square", "stadium", 1784, 940, 40, 120, to=["right", "stadium", "square"])
	
	register_location("stadium", "images/locations/stadium/", False, 2080, 1536)
	register_place(   "stadium", "closed-1", 540, 800, 40, 20)
	register_place(   "stadium", "closed-2", 760, 800, 45, 20)
	register_place(   "stadium", "stadium_rails_pos", 671, 831, 2, 2)
	register_place(   "stadium", "toilet", 105, 380, 140, 30)
	register_place(   "stadium", "beach", 530, 1496, 320, 40, to=["down", "beach", "stadium"])
	register_place(   "stadium", "forest_path-5", 2040, 1340, 40, 110, to=["right", "forest_path-5", "stadium", to_left])
	register_place(   "stadium", "square", 0, 1340, 40, 100, to=["left", "square", "stadium"])
	register_place(   "stadium", "tennis", 1000, 0, 100, 40, to=["up", "tennis", "stadium"])
	
	register_location("station", "images/locations/station/", False, 736, 992)
	register_place(   "station", "before_stop", 270, 390, 70, 50)
	register_place(   "station", "liaz_enter", 400, 390, 30, 50)
	register_place(   "station", "liaz_place", 430, 520, 100, 20)
	register_place(   "station", "station_enter", 270, 0, 70, 20)
	
	register_location("tennis", "images/locations/tennis/", False, 992, 670)
	register_place(   "tennis", "separator_pos", 708, 373, 2, 2)
	register_place(   "tennis", "forest_path-6", 430, 0, 100, 40, to=["up", "forest_path-6", "tennis"])
	register_place(   "tennis", "forest_path-8", 952, 490, 40, 120, to=["right", "forest_path-8", "tennis", to_left])
	register_place(   "tennis", "library_and_hospital", 0, 330, 40, 80, to=["left", "library_and_hospital", "tennis"])
	register_place(   "tennis", "stadium", 270, 630, 100, 40, to=["down", "stadium", "tennis"])
	
	register_location("washbasins", "images/locations/washbasins/", False, 735, 595)
	register_place(   "washbasins", "clubs", 57, 555, 100, 40, to=["down", "clubs", "washbasins"])
	register_place(   "washbasins", "crossroad", 695, 290, 40, 60, to=["right", "crossroad", "washbasins"])
	
	
	
	rpg_locations["admin"].x, rpg_locations["admin"].y = 732, 356
	rpg_locations["bath"].x, rpg_locations["bath"].y = 701, 69
	rpg_locations["beach"].x, rpg_locations["beach"].y = 1236, 488
	rpg_locations["boat_station"].x, rpg_locations["boat_station"].y = 868, 488
	rpg_locations["bunker"].x, rpg_locations["bunker"].y = 481, 857
	rpg_locations["bunker_enter"].x, rpg_locations["bunker_enter"].y = 491, 978
	rpg_locations["canteen"].x, rpg_locations["canteen"].y = 984, 344
	rpg_locations["clubs"].x, rpg_locations["clubs"].y = 481, 352
	rpg_locations["crossroad"].x, rpg_locations["crossroad"].y = 676, 213
	rpg_locations["enter"].x, rpg_locations["enter"].y = 350, 454
	rpg_locations["flat"].x, rpg_locations["flat"].y = 21, 698
	rpg_locations["forest_path-1"].x, rpg_locations["forest_path-1"].y = 336, 750
	rpg_locations["forest_path-2"].x, rpg_locations["forest_path-2"].y = 400, 649
	rpg_locations["forest_path-3"].x, rpg_locations["forest_path-3"].y = 532, 628
	rpg_locations["forest_path-4"].x, rpg_locations["forest_path-4"].y = 76, 371
	rpg_locations["forest_path-5"].x, rpg_locations["forest_path-5"].y = 75, 267
	rpg_locations["forest_path-6"].x, rpg_locations["forest_path-6"].y = 1297, 182
	rpg_locations["forest_path-7"].x, rpg_locations["forest_path-7"].y = 1451, 186
	rpg_locations["forest_path-8"].x, rpg_locations["forest_path-8"].y = 1422, 293
	rpg_locations["forest_path-9"].x, rpg_locations["forest_path-9"].y = 75, 473
	rpg_locations["hospital"].x, rpg_locations["hospital"].y = 1140, 276
	rpg_locations["house_dv"].x, rpg_locations["house_dv"].y = 697, 625
	rpg_locations["house_mt"].x, rpg_locations["house_mt"].y = 930, 29
	rpg_locations["house_sl"].x, rpg_locations["house_sl"].y = 869, 128
	rpg_locations["house_un"].x, rpg_locations["house_un"].y = 789, 29
	rpg_locations["houses_1"].x, rpg_locations["houses_1"].y = 817, 249
	rpg_locations["houses_2"].x, rpg_locations["houses_2"].y = 625, 504
	rpg_locations["ikarus"].x, rpg_locations["ikarus"].y = 214, 473
	rpg_locations["liaz"].x, rpg_locations["liaz"].y = 132, 893
	rpg_locations["library"].x, rpg_locations["library"].y = 1156, 136
	rpg_locations["library_and_hospital"].x, rpg_locations["library_and_hospital"].y = 1033, 236
	rpg_locations["mus_club"].x, rpg_locations["mus_club"].y = 574, 292
	rpg_locations["old_camp"].x, rpg_locations["old_camp"].y = 334, 860
	rpg_locations["radio_club"].x, rpg_locations["radio_club"].y = 332, 294
	rpg_locations["radio_storeroom"].x, rpg_locations["radio_storeroom"].y = 244, 300
	rpg_locations["scene"].x, rpg_locations["scene"].y = 1022, 96
	rpg_locations["square"].x, rpg_locations["square"].y = 870, 384
	rpg_locations["stadium"].x, rpg_locations["stadium"].y = 1262, 386
	rpg_locations["station"].x, rpg_locations["station"].y = 27, 851
	rpg_locations["tennis"].x, rpg_locations["tennis"].y = 1286, 292
	rpg_locations["washbasins"].x, rpg_locations["washbasins"].y = 513, 224

