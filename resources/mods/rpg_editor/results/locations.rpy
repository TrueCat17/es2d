init python:
	
	register_location("admin", "images/locations/admin/", False, 1376, 1344)
	register_place(   "admin", "clubs"         , 20, 990, 20, 120)
	register_exit(    "admin", "clubs", "admin", 0, 990, 20, 120)
	register_place(   "admin", "square"         , 1336, 990, 20, 120)
	register_exit(    "admin", "square", "admin", 1356, 990, 20, 120)
	
	register_location("bath", "images/locations/bath/", False, 647, 1000)
	
	register_location("board_station", "images/locations/board_station/", False, 1536, 1664)
	register_place(   "board_station", "houses_2"                 , 20, 540, 20, 320)
	register_exit(    "board_station", "houses_2", "board_station", 0, 540, 20, 320)
	register_place(   "board_station", "square"                 , 370, 20, 90, 20)
	register_exit(    "board_station", "square", "board_station", 370, 0, 90, 20)
	
	register_location("clubs", "images/locations/clubs/", False, 1152, 1664)
	register_place(   "clubs", "musclub_column_pos-1", 836, 400, 2, 2)
	register_place(   "clubs", "musclub_column_pos-2", 899, 400, 2, 2)
	register_place(   "clubs", "musclub_column_pos-3", 962, 400, 2, 2)
	register_place(   "clubs", "musclub_column_pos-4", 1025, 400, 2, 2)
	register_place(   "clubs", "musclub_rails_pos-1", 804, 400, 2, 2)
	register_place(   "clubs", "musclub_rails_pos-2", 867, 400, 2, 2)
	register_place(   "clubs", "musclub_rails_pos-3", 930, 400, 2, 2)
	register_place(   "clubs", "musclub_rails_pos-4", 1056, 400, 2, 2)
	register_place(   "clubs", "admin"         , 1112, 1190, 20, 130)
	register_exit(    "clubs", "admin", "clubs", 1132, 1190, 20, 130)
	register_place(   "clubs", "enter"         , 20, 1190, 20, 130)
	register_exit(    "clubs", "enter", "clubs", 0, 1190, 20, 130)
	register_place(   "clubs", "houses_2"         , 780, 1624, 100, 20)
	register_exit(    "clubs", "houses_2", "clubs", 780, 1644, 100, 20)
	register_place(   "clubs", "radio_club"         , 390, 1135, 120, 15)
	register_exit(    "clubs", "radio_club", "clubs", 390, 1120, 120, 15)
	
	register_location("enter", "images/locations/enter/", False, 960, 992)
	register_place(   "enter", "behind_gates", 415, 180, 130, 10)
	register_place(   "enter", "gates", 415, 200, 130, 50)
	register_place(   "enter", "ikarus_pos", 293, 590, 2, 2)
	register_place(   "enter", "left_exit", 20, 540, 20, 140)
	register_place(   "enter", "left_gate_pos", 449, 279, 2, 2)
	register_place(   "enter", "right_exit", 920, 540, 20, 150)
	register_place(   "enter", "right_gate_pos", 509, 314, 2, 2)
	register_place(   "enter", "clubs"         , 410, 20, 140, 20)
	register_exit(    "enter", "clubs", "enter", 410, 0, 140, 20)
	register_place(   "enter", "ikarus"         , 400, 610, 40, 20)
	register_exit(    "enter", "ikarus", "enter", 400, 590, 40, 20)
	register_exit("enter", "enter", "right_exit", 0, 540, 20, 140)
	register_exit("enter", "enter", "left_exit", 940, 540, 20, 150)
	
	register_location("flat", "images/locations/flat/", True, 192, 272)
	register_place(   "flat", "flat_out", 20, 252, 40, 20)
	
	register_location("hospital", "images/locations/hospital/", True, 224, 256)
	register_place(   "hospital", "library_and_hospital"            , 90, 216, 100, 20)
	register_exit(    "hospital", "library_and_hospital", "hospital", 90, 236, 100, 20)
	
	register_location("house_od", "images/locations/house_od/", True, 544, 416)
	register_place(   "house_od", "houses_1"            , 230, 322, 54, 15)
	register_exit(    "house_od", "houses_1", "house_od", 230, 337, 54, 15)
	
	register_location("houses_1", "images/locations/houses_1/", False, 1632, 1152)
	register_place(   "houses_1", "lib_and_hosp-up", 1592, 700, 20, 70)
	register_place(   "houses_1", "house_od"            , 1090, 370, 60, 20)
	register_exit(    "houses_1", "house_od", "houses_1", 1090, 350, 60, 20)
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
	register_place(   "houses_2", "square"            , 1921, 20, 130, 20)
	register_exit(    "houses_2", "square", "houses_2", 1921, 0, 130, 20)
	
	register_location("ikarus", "images/locations/ikarus/", True, 478, 154)
	register_place(   "ikarus", "before_sit_place", 409, 76, 2, 2)
	register_place(   "ikarus", "sit_place", 397, 71, 2, 2)
	register_place(   "ikarus", "enter"          , 407, 124, 30, 15)
	register_exit(    "ikarus", "enter", "ikarus", 407, 139, 30, 15)
	
	register_location("liaz", "images/locations/liaz/", True, 432, 216)
	register_place(   "liaz", "lias_enter", 320, 196, 70, 20)
	register_place(   "liaz", "sit_place", 325, 85, 2, 2)
	
	register_location("library", "images/locations/library/", True, 382, 510)
	register_place(   "library", "library_and_hospital"           , 215, 470, 100, 20)
	register_exit(    "library", "library_and_hospital", "library", 215, 490, 100, 20)
	
	register_location("library_and_hospital", "images/locations/library_and_hospital/", False, 1408, 1312)
	register_place(   "library_and_hospital", "houses_1-up", 20, 725, 20, 80)
	register_place(   "library_and_hospital", "hospital"                        , 633, 910, 50, 20)
	register_exit(    "library_and_hospital", "hospital", "library_and_hospital", 633, 890, 50, 20)
	register_place(   "library_and_hospital", "houses_1"                        , 20, 1050, 20, 110)
	register_exit(    "library_and_hospital", "houses_1", "library_and_hospital", 0, 1050, 20, 110)
	register_place(   "library_and_hospital", "library"                        , 1120, 470, 60, 20)
	register_exit(    "library_and_hospital", "library", "library_and_hospital", 1120, 450, 60, 20)
	register_exit("library_and_hospital", "houses_1", "lib_and_hosp-up", 0, 725, 20, 80)
	
	register_location("old_camp", "images/locations/old_camp/", False, 2070, 1740)
	
	register_location("radio_club", "images/locations/radio_club/", True, 310, 247)
	register_place(   "radio_club", "clubs"              , 215, 207, 60, 20)
	register_exit(    "radio_club", "clubs", "radio_club", 215, 227, 60, 20)
	
	register_location("square", "images/locations/square/", False, 1824, 1344)
	register_place(   "square", "admin"          , 20, 940, 20, 120)
	register_exit(    "square", "admin", "square", 0, 940, 20, 120)
	register_place(   "square", "board_station"          , 310, 1304, 100, 20)
	register_exit(    "square", "board_station", "square", 310, 1324, 100, 20)
	register_place(   "square", "houses_1"          , 190, 20, 510, 20)
	register_exit(    "square", "houses_1", "square", 190, 0, 510, 20)
	register_place(   "square", "houses_2"          , 20, 1304, 100, 20)
	register_exit(    "square", "houses_2", "square", 20, 1324, 100, 20)
	register_place(   "square", "stadium"          , 1784, 940, 20, 120)
	register_exit(    "square", "stadium", "square", 1804, 940, 20, 120)
	
	register_location("stadium", "images/locations/stadium/", False, 2080, 1536)
	register_place(   "stadium", "square"           , 20, 1340, 20, 100)
	register_exit(    "stadium", "square", "stadium", 0, 1340, 20, 100)
	register_place(   "stadium", "tennis"           , 1000, 20, 100, 20)
	register_exit(    "stadium", "tennis", "stadium", 1000, 0, 100, 20)
	
	register_location("station", "images/locations/station/", False, 736, 992)
	register_place(   "station", "station_enter", 270, 0, 70, 20)
	
	register_location("tennis", "images/locations/tennis/", False, 992, 670)
	register_place(   "tennis", "stadium"          , 270, 630, 100, 20)
	register_exit(    "tennis", "stadium", "tennis", 270, 650, 100, 20)
	
	
	
	locations["flat"].x, locations["flat"].y = 20, 732
	locations["square"].x, locations["square"].y = 425, 289
	locations["board_station"].x, locations["board_station"].y = 433, 413
	locations["stadium"].x, locations["stadium"].y = 617, 295
	locations["admin"].x, locations["admin"].y = 273, 265
	locations["tennis"].x, locations["tennis"].y = 641, 204
	locations["hospital"].x, locations["hospital"].y = 557, 12
	locations["houses_1"].x, locations["houses_1"].y = 372, 169
	locations["liaz"].x, locations["liaz"].y = 233, 824
	locations["radio_club"].x, locations["radio_club"].y = 81, 148
	locations["library"].x, locations["library"].y = 449, 10
	locations["bath"].x, locations["bath"].y = None, None
	locations["library_and_hospital"].x, locations["library_and_hospital"].y = 505, 156
	locations["clubs"].x, locations["clubs"].y = 169, 263
	locations["station"].x, locations["station"].y = 128, 745
	locations["houses_2"].x, locations["houses_2"].y = 244, 414
	locations["old_camp"].x, locations["old_camp"].y = None, None
	locations["house_od"].x, locations["house_od"].y = 308, 51
	locations["enter"].x, locations["enter"].y = 24, 333
	locations["ikarus"].x, locations["ikarus"].y = 16, 268

