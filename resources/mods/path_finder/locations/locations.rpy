init python:
	
	register_location("admin", "images/locations/admin/", False, 1376, 1344)
	register_place(   "admin", "bench_left_pos", 870, 455, 2, 2)
	register_place(   "admin", "lamp_pos-1", 977, 372, 2, 2)
	register_place(   "admin", "lamp_pos-2", 977, 540, 2, 2)
	register_place(   "admin", "lamp_pos-3", 978, 987, 2, 2)
	register_place(   "admin", "lamp_pos-4", 611, 987, 2, 2)
	register_place(   "admin", "lamp_pos-5", 348, 987, 2, 2)
	register_place(   "admin", "clubs"         , 20, 990, 20, 120)
	register_exit(    "admin", "clubs", "admin", 0, 990, 20, 120)
	register_place(   "admin", "square"         , 1336, 990, 20, 120)
	register_exit(    "admin", "square", "admin", 1356, 990, 20, 120)
	
	register_location("bath", "images/locations/bath/", False, 647, 1000)
	register_place(   "bath", "bath_rails_left_pos", 304, 587, 2, 2)
	register_place(   "bath", "bath_rails_right_pos", 432, 587, 2, 2)
	register_place(   "bath", "crossroad"        , 180, 960, 190, 20)
	register_exit(    "bath", "crossroad", "bath", 180, 980, 190, 20)
	
	register_location("beach", "images/locations/beach/", False, 1792, 1408)
	register_place(   "beach", "board_station"         , 20, 328, 20, 150)
	register_exit(    "beach", "board_station", "beach", 0, 328, 20, 150)
	register_place(   "beach", "stadium"         , 800, 20, 350, 20)
	register_exit(    "beach", "stadium", "beach", 800, 0, 350, 20)
	
	register_location("board_station", "images/locations/board_station/", False, 1536, 1664)
	register_place(   "board_station", "beach"                 , 1496, 350, 20, 255)
	register_exit(    "board_station", "beach", "board_station", 1516, 350, 20, 255)
	register_place(   "board_station", "houses_2"                 , 20, 540, 20, 320)
	register_exit(    "board_station", "houses_2", "board_station", 0, 540, 20, 320)
	register_place(   "board_station", "square"                 , 370, 20, 90, 20)
	register_exit(    "board_station", "square", "board_station", 370, 0, 90, 20)
	
	register_location("bunker", "images/locations/bunker/", True, 276, 253)
	register_place(   "bunker", "bunker_enter"          , 60, 223, 70, 15)
	register_exit(    "bunker", "bunker_enter", "bunker", 60, 238, 70, 15)
	register_place(   "bunker", "old_camp"          , 160, 223, 40, 15)
	register_exit(    "bunker", "old_camp", "bunker", 160, 238, 40, 15)
	
	register_location("bunker_enter", "images/locations/bunker_enter/", True, 130, 258)
	register_place(   "bunker_enter", "bunker"                , 30, 111, 70, 15)
	register_exit(    "bunker_enter", "bunker", "bunker_enter", 30, 96, 70, 15)
	
	register_location("canteen", "images/locations/canteen/", True, 1152, 832)
	register_place(   "canteen", "canteen_column_back_pos-1", 143, 319, 2, 2)
	register_place(   "canteen", "canteen_column_back_pos-2", 431, 319, 2, 2)
	register_place(   "canteen", "canteen_column_back_pos-3", 655, 319, 2, 2)
	register_place(   "canteen", "canteen_column_pos-1", 143, 607, 2, 2)
	register_place(   "canteen", "canteen_column_pos-2", 431, 607, 2, 2)
	register_place(   "canteen", "canteen_column_pos-3", 655, 607, 2, 2)
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
	register_place(   "canteen", "square"           , 640, 802, 55, 15)
	register_exit(    "canteen", "square", "canteen", 640, 817, 55, 15)
	
	register_location("clubs", "images/locations/clubs/", False, 1152, 1664)
	register_place(   "clubs", "mus_club_column_pos-1", 773, 400, 2, 2)
	register_place(   "clubs", "mus_club_column_pos-2", 836, 400, 2, 2)
	register_place(   "clubs", "mus_club_column_pos-3", 899, 400, 2, 2)
	register_place(   "clubs", "mus_club_column_pos-4", 962, 400, 2, 2)
	register_place(   "clubs", "mus_club_column_pos-5", 1025, 400, 2, 2)
	register_place(   "clubs", "mus_club_rails_pos-1", 804, 400, 2, 2)
	register_place(   "clubs", "mus_club_rails_pos-2", 867, 400, 2, 2)
	register_place(   "clubs", "mus_club_rails_pos-3", 930, 400, 2, 2)
	register_place(   "clubs", "mus_club_rails_pos-4", 1056, 400, 2, 2)
	register_place(   "clubs", "admin"         , 1112, 1190, 20, 130)
	register_exit(    "clubs", "admin", "clubs", 1132, 1190, 20, 130)
	register_place(   "clubs", "enter"         , 20, 1190, 20, 130, to_right)
	register_exit(    "clubs", "enter", "clubs", 0, 1190, 20, 130)
	register_place(   "clubs", "houses_2"         , 780, 1624, 100, 20)
	register_exit(    "clubs", "houses_2", "clubs", 780, 1644, 100, 20)
	register_place(   "clubs", "mus_club"         , 970, 355, 50, 15)
	register_exit(    "clubs", "mus_club", "clubs", 970, 340, 50, 15)
	register_place(   "clubs", "radio_club"         , 390, 1135, 120, 15)
	register_exit(    "clubs", "radio_club", "clubs", 390, 1120, 120, 15)
	register_place(   "clubs", "washbasins"         , 620, 20, 145, 20, to_back)
	register_exit(    "clubs", "washbasins", "clubs", 620, 0, 145, 20)
	
	register_location("crossroad", "images/locations/crossroad/", False, 700, 700)
	register_place(   "crossroad", "bath"             , 305, 20, 80, 20)
	register_exit(    "crossroad", "bath", "crossroad", 305, 0, 80, 20)
	register_place(   "crossroad", "houses_1"             , 660, 335, 20, 70)
	register_exit(    "crossroad", "houses_1", "crossroad", 680, 335, 20, 70)
	register_place(   "crossroad", "washbasins"             , 20, 335, 20, 70)
	register_exit(    "crossroad", "washbasins", "crossroad", 0, 335, 20, 70)
	
	register_location("enter", "images/locations/enter/", False, 960, 992)
	register_place(   "enter", "before_gates", 415, 290, 130, 50)
	register_place(   "enter", "behind_gates", 415, 250, 130, 10)
	register_place(   "enter", "gate_left_pos", 449, 279, 2, 2)
	register_place(   "enter", "gate_right_pos", 509, 279, 2, 2)
	register_place(   "enter", "ikarus_pos", 293, 590, 2, 2)
	register_place(   "enter", "clubs"         , 410, 20, 140, 20, to_back)
	register_exit(    "enter", "clubs", "enter", 410, 0, 140, 20)
	register_place(   "enter", "forest_path-5"         , 920, 565, 20, 160, to_left)
	register_exit(    "enter", "forest_path-5", "enter", 940, 565, 20, 160)
	register_place(   "enter", "forest_path-9"         , 20, 555, 20, 160, to_right)
	register_exit(    "enter", "forest_path-9", "enter", 0, 555, 20, 160)
	register_place(   "enter", "ikarus"         , 400, 600, 40, 15)
	register_exit(    "enter", "ikarus", "enter", 400, 585, 40, 15)
	
	register_location("flat", "images/locations/flat/", True, 192, 272)
	register_place(   "flat", "armchair_pos", 80, 143, 2, 2)
	register_place(   "flat", "bed", 120, 155, 30, 70)
	register_place(   "flat", "center", 70, 170, 40, 40)
	register_place(   "flat", "computer", 60, 140, 80, 20)
	register_place(   "flat", "exit", 23, 252, 30, 20)
	register_place(   "flat", "flat_keys_pos", 20, 205, 2, 2)
	register_place(   "flat", "lighter_pos", 121, 112, 2, 2)
	register_place(   "flat", "notepad_pos", 20, 190, 2, 2)
	register_place(   "flat", "phone_pos", 155, 160, 2, 2)
	
	register_location("forest_path-1", "images/locations/forest_path-1/", False, 1088, 832)
	register_place(   "forest_path-1", "left_exit", 20, 690, 20, 90)
	register_place(   "forest_path-1", "right_exit", 1048, 120, 20, 60)
	register_place(   "forest_path-1", "forest_path-2"                 , 720, 20, 120, 20)
	register_exit(    "forest_path-1", "forest_path-2", "forest_path-1", 720, 0, 120, 20)
	register_place(   "forest_path-1", "old_camp"                 , 605, 792, 110, 20, to_forward)
	register_exit(    "forest_path-1", "old_camp", "forest_path-1", 605, 812, 110, 20)
	register_exit("forest_path-1", "forest_path-1", "left_exit", 1068, 120, 20, 60)
	register_exit("forest_path-1", "forest_path-1", "right_exit", 0, 690, 20, 90)
	
	register_location("forest_path-2", "images/locations/forest_path-2/", False, 768, 576)
	register_place(   "forest_path-2", "forest_path-1"                 , 120, 536, 80, 20)
	register_exit(    "forest_path-2", "forest_path-1", "forest_path-2", 120, 556, 80, 20)
	register_place(   "forest_path-2", "forest_path-3"                 , 728, 270, 20, 90)
	register_exit(    "forest_path-2", "forest_path-3", "forest_path-2", 748, 270, 20, 90)
	
	register_location("forest_path-3", "images/locations/forest_path-3/", False, 640, 416)
	register_place(   "forest_path-3", "forest_path-2"                 , 20, 310, 20, 60)
	register_exit(    "forest_path-3", "forest_path-2", "forest_path-3", 0, 310, 20, 60)
	register_place(   "forest_path-3", "houses_2"                 , 500, 20, 90, 20)
	register_exit(    "forest_path-3", "houses_2", "forest_path-3", 500, 0, 90, 20)
	
	register_location("forest_path-4", "images/locations/forest_path-4/", False, 544, 416)
	register_place(   "forest_path-4", "forest_path-5"                 , 120, 20, 180, 20)
	register_exit(    "forest_path-4", "forest_path-5", "forest_path-4", 120, 0, 180, 20)
	register_place(   "forest_path-4", "forest_path-9"                 , 120, 376, 180, 20)
	register_exit(    "forest_path-4", "forest_path-9", "forest_path-4", 120, 396, 180, 20)
	
	register_location("forest_path-5", "images/locations/forest_path-5/", False, 544, 416)
	register_place(   "forest_path-5", "enter"                 , 120, 20, 180, 20, to_back)
	register_exit(    "forest_path-5", "enter", "forest_path-5", 120, 0, 180, 20)
	register_place(   "forest_path-5", "forest_path-4"                 , 120, 376, 180, 20)
	register_exit(    "forest_path-5", "forest_path-4", "forest_path-5", 120, 396, 180, 20)
	register_place(   "forest_path-5", "stadium"                 , 504, 215, 20, 145, to_left)
	register_exit(    "forest_path-5", "stadium", "forest_path-5", 524, 215, 20, 145)
	
	register_location("forest_path-6", "images/locations/forest_path-6/", False, 544, 416)
	register_place(   "forest_path-6", "left", 20, 120, 20, 80, to_right)
	register_place(   "forest_path-6", "up", 310, 20, 90, 20, to_back)
	register_place(   "forest_path-6", "forest_path-7"                 , 504, 210, 20, 90)
	register_exit(    "forest_path-6", "forest_path-7", "forest_path-6", 524, 210, 20, 90)
	register_place(   "forest_path-6", "tennis"                 , 150, 376, 90, 20)
	register_exit(    "forest_path-6", "tennis", "forest_path-6", 150, 396, 90, 20)
	register_exit("forest_path-6", "forest_path-6", "up", 0, 120, 20, 80)
	register_exit("forest_path-6", "forest_path-6", "left", 310, 0, 90, 20)
	
	register_location("forest_path-7", "images/locations/forest_path-7/", False, 544, 416)
	register_place(   "forest_path-7", "right", 504, 80, 20, 90, to_left)
	register_place(   "forest_path-7", "up", 210, 20, 90, 20, to_back)
	register_place(   "forest_path-7", "forest_path-6"                 , 20, 180, 20, 90)
	register_exit(    "forest_path-7", "forest_path-6", "forest_path-7", 0, 180, 20, 90)
	register_place(   "forest_path-7", "forest_path-8"                 , 220, 376, 80, 20)
	register_exit(    "forest_path-7", "forest_path-8", "forest_path-7", 220, 396, 80, 20)
	register_exit("forest_path-7", "forest_path-7", "right", 210, 0, 90, 20)
	register_exit("forest_path-7", "forest_path-7", "up", 524, 80, 20, 90)
	
	register_location("forest_path-8", "images/locations/forest_path-8/", False, 544, 416)
	register_place(   "forest_path-8", "down", 210, 376, 90, 20, to_forward)
	register_place(   "forest_path-8", "right", 504, 120, 20, 90, to_left)
	register_place(   "forest_path-8", "forest_path-7"                 , 400, 20, 100, 20)
	register_exit(    "forest_path-8", "forest_path-7", "forest_path-8", 400, 0, 100, 20)
	register_place(   "forest_path-8", "tennis"                 , 20, 210, 20, 90)
	register_exit(    "forest_path-8", "tennis", "forest_path-8", 0, 210, 20, 90)
	register_exit("forest_path-8", "forest_path-8", "right", 210, 396, 90, 20)
	register_exit("forest_path-8", "forest_path-8", "down", 524, 120, 20, 90)
	
	register_location("forest_path-9", "images/locations/forest_path-9/", False, 544, 416)
	register_place(   "forest_path-9", "enter"                 , 120, 376, 180, 20, to_forward)
	register_exit(    "forest_path-9", "enter", "forest_path-9", 120, 396, 180, 20)
	register_place(   "forest_path-9", "forest_path-4"                 , 120, 20, 180, 20)
	register_exit(    "forest_path-9", "forest_path-4", "forest_path-9", 120, 0, 180, 20)
	
	register_location("hospital", "images/locations/hospital/", True, 224, 256)
	register_place(   "hospital", "library_and_hospital"            , 120, 226, 34, 15)
	register_exit(    "hospital", "library_and_hospital", "hospital", 120, 241, 34, 15)
	
	register_location("house_dv", "images/locations/house_dv/", True, 512, 512)
	register_place(   "house_dv", "houses_2"            , 250, 386, 55, 15)
	register_exit(    "house_dv", "houses_2", "house_dv", 250, 401, 55, 15)
	
	register_location("house_mt", "images/locations/house_mt/", True, 512, 512)
	register_place(   "house_mt", "houses_1"            , 209, 400, 54, 15)
	register_exit(    "house_mt", "houses_1", "house_mt", 209, 415, 54, 15)
	
	register_location("house_sl", "images/locations/house_sl/", True, 512, 512)
	register_place(   "house_sl", "houses_1"            , 229, 378, 54, 15)
	register_exit(    "house_sl", "houses_1", "house_sl", 229, 393, 54, 15)
	
	register_location("house_un", "images/locations/house_un/", True, 512, 512)
	register_place(   "house_un", "houses_1"            , 229, 378, 54, 15)
	register_exit(    "house_un", "houses_1", "house_un", 229, 393, 54, 15)
	
	register_location("houses_1", "images/locations/houses_1/", False, 1632, 1152)
	register_place(   "houses_1", "lib_and_hosp-up", 1592, 700, 20, 70)
	register_place(   "houses_1", "crossroad"            , 20, 700, 20, 70)
	register_exit(    "houses_1", "crossroad", "houses_1", 0, 700, 20, 70)
	register_place(   "houses_1", "house_mt"            , 1085, 365, 70, 15)
	register_exit(    "houses_1", "house_mt", "houses_1", 1085, 350, 70, 15)
	register_place(   "houses_1", "house_sl"            , 1405, 675, 70, 15)
	register_exit(    "houses_1", "house_sl", "houses_1", 1405, 660, 70, 15)
	register_place(   "houses_1", "house_un"            , 190, 355, 70, 15)
	register_exit(    "houses_1", "house_un", "houses_1", 190, 340, 70, 15)
	register_place(   "houses_1", "library_and_hospital"            , 1592, 1020, 20, 110)
	register_exit(    "houses_1", "library_and_hospital", "houses_1", 1612, 1020, 20, 110)
	register_place(   "houses_1", "square"            , 827, 1112, 520, 20)
	register_exit(    "houses_1", "square", "houses_1", 827, 1132, 520, 20)
	register_exit("houses_1", "library_and_hospital", "houses_1-up", 1612, 700, 20, 70)
	
	register_location("houses_2", "images/locations/houses_2/", False, 2112, 1920)
	register_place(   "houses_2", "board_station"            , 2072, 1080, 20, 170)
	register_exit(    "houses_2", "board_station", "houses_2", 2092, 1080, 20, 170)
	register_place(   "houses_2", "clubs"            , 540, 20, 130, 20)
	register_exit(    "houses_2", "clubs", "houses_2", 540, 0, 130, 20)
	register_place(   "houses_2", "forest_path-3"            , 160, 1880, 100, 20)
	register_exit(    "houses_2", "forest_path-3", "houses_2", 160, 1900, 100, 20)
	register_place(   "houses_2", "house_dv"            , 1180, 355, 70, 15)
	register_exit(    "houses_2", "house_dv", "houses_2", 1180, 340, 70, 15)
	register_place(   "houses_2", "square"            , 1921, 20, 130, 20)
	register_exit(    "houses_2", "square", "houses_2", 1921, 0, 130, 20)
	
	register_location("ikarus", "images/locations/ikarus/", True, 478, 154)
	register_place(   "ikarus", "before_sit_place", 409, 76, 2, 2)
	register_place(   "ikarus", "before_sit_place-2", 410, 100, 10, 10)
	register_place(   "ikarus", "sit_place", 397, 71, 2, 2)
	register_place(   "ikarus", "enter"          , 407, 124, 30, 15)
	register_exit(    "ikarus", "enter", "ikarus", 407, 139, 30, 15)
	
	register_location("liaz", "images/locations/liaz/", True, 432, 216)
	register_place(   "liaz", "liaz_enter", 320, 196, 70, 20, to_forward)
	register_place(   "liaz", "sit_place", 325, 85, 2, 2)
	
	register_location("library", "images/locations/library/", True, 384, 512)
	register_place(   "library", "cupboard_1_pos", 214, 389, 2, 2)
	register_place(   "library", "cupboard_2_pos", 214, 317, 2, 2)
	register_place(   "library", "cupboard_3_pos", 215, 248, 2, 2)
	register_place(   "library", "library_and_hospital"           , 240, 470, 55, 20)
	register_exit(    "library", "library_and_hospital", "library", 240, 490, 55, 20)
	
	register_location("library_and_hospital", "images/locations/library_and_hospital/", False, 1408, 1312)
	register_place(   "library_and_hospital", "houses_1-up", 20, 725, 20, 80)
	register_place(   "library_and_hospital", "hospital"                        , 633, 910, 50, 20)
	register_exit(    "library_and_hospital", "hospital", "library_and_hospital", 633, 890, 50, 20)
	register_place(   "library_and_hospital", "houses_1"                        , 20, 1050, 20, 110)
	register_exit(    "library_and_hospital", "houses_1", "library_and_hospital", 0, 1050, 20, 110)
	register_place(   "library_and_hospital", "library"                        , 1120, 470, 60, 20)
	register_exit(    "library_and_hospital", "library", "library_and_hospital", 1120, 450, 60, 20)
	register_place(   "library_and_hospital", "scene"                        , 510, 20, 70, 20)
	register_exit(    "library_and_hospital", "scene", "library_and_hospital", 510, 0, 70, 20)
	register_place(   "library_and_hospital", "tennis"                        , 1368, 470, 20, 110)
	register_exit(    "library_and_hospital", "tennis", "library_and_hospital", 1388, 470, 20, 110)
	register_exit("library_and_hospital", "houses_1", "lib_and_hosp-up", 0, 725, 20, 80)
	
	register_location("mus_club", "images/locations/mus_club/", True, 224, 272)
	register_place(   "mus_club", "mus_club_microphone_pos", 60, 220, 2, 2)
	register_place(   "mus_club", "stand_pos", 110, 230, 2, 2)
	register_place(   "mus_club", "clubs"            , 130, 242, 55, 15)
	register_exit(    "mus_club", "clubs", "mus_club", 130, 257, 55, 15)
	
	register_location("old_camp", "images/locations/old_camp/", False, 2070, 1740)
	register_place(   "old_camp", "bunker"            , 820, 665, 40, 20)
	register_exit(    "old_camp", "bunker", "old_camp", 820, 645, 40, 20)
	register_place(   "old_camp", "forest_path-1"            , 1160, 1700, 150, 20, to_forward)
	register_exit(    "old_camp", "forest_path-1", "old_camp", 1160, 1720, 150, 20)
	
	register_location("radio_club", "images/locations/radio_club/", True, 310, 247)
	register_place(   "radio_club", "clubs"              , 218, 217, 55, 15)
	register_exit(    "radio_club", "clubs", "radio_club", 218, 232, 55, 15)
	register_place(   "radio_club", "radio_storeroom"              , 270, 185, 20, 30)
	register_exit(    "radio_club", "radio_storeroom", "radio_club", 290, 185, 20, 30)
	
	register_location("radio_storeroom", "images/locations/radio_storeroom/", True, 162, 247)
	register_place(   "radio_storeroom", "radio_club"                   , 99, 217, 30, 15, to_forward)
	register_exit(    "radio_storeroom", "radio_club", "radio_storeroom", 99, 232, 30, 15)
	
	register_location("scene", "images/locations/scene/", False, 960, 992)
	register_place(   "scene", "library_and_hospital"         , 400, 952, 150, 20)
	register_exit(    "scene", "library_and_hospital", "scene", 400, 972, 150, 20)
	
	register_location("square", "images/locations/square/", False, 1824, 1344)
	register_place(   "square", "bench_left_pos-1", 204, 319, 2, 2)
	register_place(   "square", "bench_left_pos-2", 204, 542, 2, 2)
	register_place(   "square", "bench_left_pos-3", 204, 767, 2, 2)
	register_place(   "square", "bench_right_pos-1", 685, 319, 2, 2)
	register_place(   "square", "bench_right_pos-2", 685, 542, 2, 2)
	register_place(   "square", "bench_right_pos-3", 685, 767, 2, 2)
	register_place(   "square", "car_pos", 1223, 846, 2, 2)
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
	register_place(   "square", "admin"          , 20, 940, 20, 120)
	register_exit(    "square", "admin", "square", 0, 940, 20, 120)
	register_place(   "square", "board_station"          , 310, 1304, 100, 20)
	register_exit(    "square", "board_station", "square", 310, 1324, 100, 20)
	register_place(   "square", "canteen"          , 1187, 665, 80, 10)
	register_exit(    "square", "canteen", "square", 1187, 655, 80, 10)
	register_place(   "square", "houses_1"          , 190, 20, 510, 20)
	register_exit(    "square", "houses_1", "square", 190, 0, 510, 20)
	register_place(   "square", "houses_2"          , 20, 1304, 100, 20)
	register_exit(    "square", "houses_2", "square", 20, 1324, 100, 20)
	register_place(   "square", "stadium"          , 1784, 940, 20, 120)
	register_exit(    "square", "stadium", "square", 1804, 940, 20, 120)
	
	register_location("stadium", "images/locations/stadium/", False, 2080, 1536)
	register_place(   "stadium", "stadium_rails_pos", 671, 831, 2, 2)
	register_place(   "stadium", "beach"           , 530, 1496, 320, 20)
	register_exit(    "stadium", "beach", "stadium", 530, 1516, 320, 20)
	register_place(   "stadium", "forest_path-5"           , 2040, 1340, 20, 110, to_left)
	register_exit(    "stadium", "forest_path-5", "stadium", 2060, 1340, 20, 110)
	register_place(   "stadium", "square"           , 20, 1340, 20, 100)
	register_exit(    "stadium", "square", "stadium", 0, 1340, 20, 100)
	register_place(   "stadium", "tennis"           , 1000, 20, 100, 20)
	register_exit(    "stadium", "tennis", "stadium", 1000, 0, 100, 20)
	
	register_location("station", "images/locations/station/", False, 736, 992)
	register_place(   "station", "before_stop", 270, 390, 70, 50)
	register_place(   "station", "liaz_enter", 400, 390, 30, 50)
	register_place(   "station", "liaz_place", 430, 520, 100, 20)
	register_place(   "station", "station_enter", 270, 0, 70, 20)
	
	register_location("tennis", "images/locations/tennis/", False, 992, 670)
	register_place(   "tennis", "separator_pos", 708, 373, 2, 2)
	register_place(   "tennis", "forest_path-6"          , 430, 20, 100, 20, to_back)
	register_exit(    "tennis", "forest_path-6", "tennis", 430, 0, 100, 20)
	register_place(   "tennis", "forest_path-8"          , 952, 490, 20, 120, to_left)
	register_exit(    "tennis", "forest_path-8", "tennis", 972, 490, 20, 120)
	register_place(   "tennis", "library_and_hospital"          , 20, 330, 20, 80)
	register_exit(    "tennis", "library_and_hospital", "tennis", 0, 330, 20, 80)
	register_place(   "tennis", "stadium"          , 270, 630, 100, 20)
	register_exit(    "tennis", "stadium", "tennis", 270, 650, 100, 20)
	
	register_location("washbasins", "images/locations/washbasins/", False, 735, 595)
	register_place(   "washbasins", "clubs"              , 57, 555, 100, 20)
	register_exit(    "washbasins", "clubs", "washbasins", 57, 575, 100, 20)
	register_place(   "washbasins", "crossroad"              , 695, 290, 20, 60)
	register_exit(    "washbasins", "crossroad", "washbasins", 715, 290, 20, 60)
	
	
	
	locations["admin"].x, locations["admin"].y = 732, 356
	locations["bath"].x, locations["bath"].y = 701, 69
	locations["beach"].x, locations["beach"].y = 1237, 489
	locations["board_station"].x, locations["board_station"].y = 868, 489
	locations["bunker"].x, locations["bunker"].y = 481, 857
	locations["bunker_enter"].x, locations["bunker_enter"].y = 491, 978
	locations["canteen"].x, locations["canteen"].y = 984, 344
	locations["clubs"].x, locations["clubs"].y = 481, 352
	locations["crossroad"].x, locations["crossroad"].y = 677, 214
	locations["enter"].x, locations["enter"].y = 350, 454
	locations["flat"].x, locations["flat"].y = 72, 720
	locations["forest_path-1"].x, locations["forest_path-1"].y = 336, 750
	locations["forest_path-2"].x, locations["forest_path-2"].y = 400, 650
	locations["forest_path-3"].x, locations["forest_path-3"].y = 532, 628
	locations["forest_path-4"].x, locations["forest_path-4"].y = 76, 371
	locations["forest_path-5"].x, locations["forest_path-5"].y = 75, 267
	locations["forest_path-6"].x, locations["forest_path-6"].y = 1297, 182
	locations["forest_path-7"].x, locations["forest_path-7"].y = 1451, 186
	locations["forest_path-8"].x, locations["forest_path-8"].y = 1422, 293
	locations["forest_path-9"].x, locations["forest_path-9"].y = 75, 473
	locations["hospital"].x, locations["hospital"].y = 1140, 276
	locations["house_dv"].x, locations["house_dv"].y = 697, 625
	locations["house_mt"].x, locations["house_mt"].y = 930, 29
	locations["house_sl"].x, locations["house_sl"].y = 869, 128
	locations["house_un"].x, locations["house_un"].y = 789, 29
	locations["houses_1"].x, locations["houses_1"].y = 818, 250
	locations["houses_2"].x, locations["houses_2"].y = 625, 504
	locations["ikarus"].x, locations["ikarus"].y = 214, 473
	locations["liaz"].x, locations["liaz"].y = 60, 987
	locations["library"].x, locations["library"].y = 1156, 136
	locations["library_and_hospital"].x, locations["library_and_hospital"].y = 1034, 236
	locations["mus_club"].x, locations["mus_club"].y = 574, 292
	locations["old_camp"].x, locations["old_camp"].y = 334, 860
	locations["radio_club"].x, locations["radio_club"].y = 332, 294
	locations["radio_storeroom"].x, locations["radio_storeroom"].y = 244, 300
	locations["scene"].x, locations["scene"].y = 1022, 96
	locations["square"].x, locations["square"].y = 870, 384
	locations["stadium"].x, locations["stadium"].y = 1262, 386
	locations["station"].x, locations["station"].y = 71, 855
	locations["tennis"].x, locations["tennis"].y = 1286, 292
	locations["washbasins"].x, locations["washbasins"].y = 514, 224

