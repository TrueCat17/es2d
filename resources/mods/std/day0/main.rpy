init python:
	day0_phrases_forgot_things = [
		"Кажется, я что-то забыл.",
		"Карманы ощущаются слишком лёгкими, нужно проверить, вдруг забыл что-то.",
		"Не помешает проверить карманы… Чёрт, чего-то не хватает.",
		"Я точно всё взял?",
	]
	
	day0_before_exit = False
	
	def day0_can_exit_to(to_location_name, to_place_name):
		return False

label day0_start:
	python:
		day_num = 0
		night_time()
		control = False
		
		set_location("enter", "before_gates_far")
		me.set_direction(to_forward)
	
		gate_right = get_location_objects(cur_location_name, me, "gate_right", 1)[0]
		gate_right.start_animation("open")
	
		add_location_object("enter", "behind_gates", "uv_night_prologue")
	
	"Мне опять снился сон."
	"Этот сон…"
	"Расплывчатые очертания ворот который раз кружат перед глазами, словно мираж."
	"Только здесь, во время этого странного сна, ощущаешь себя живым."
	"Проснёшься - и сон забудется; пока ещё спишь - осознаёшь своё глупое положение от того, что не сможешь удержать все эти образы в голове после пробуждения."
	"Воистину странное чувство."
	"И вот рассеивается дымка, обнажая ворота."
	"И, несмотря на время - а здесь и сейчас лето, - чувствуешь лёгкий озноб."
	"Такое огромное желание подбежать к воротам, распахнуть их и вбежать внутрь, ведь там тепло!"
	"Наверняка тепло, на все сто процентов!"
	"Приятные мысли расслабляют, погружают в забытье."
	"Даже боюсь, что засну во сне."
	"Но это не мой дом, и меня туда никто не приглашал."
	"Небо. Такое красивое и такое притягательное - в наших краях такого точно не встретить."
	"Сотни и тысячи. Нет. Миллионы и миллиарды звёзд с чьей-то лёгкой руки просто-напросто рассыпаны по чёрному одеялу - хватай горсть и беги."
	"Но до них ещё придётся как-то дотянуться."
	"А что это над воротами?"
	
	$ cam_to('behind_gates')
	
	"“Совёнок”?"
	"Как сова, но маленькая…"
	"Или как сов?"
	"Даже не знаю, и знать не хочу."
	"В любом случае, я лишь наблюдаю. При всём желании ни звезду, ни кусок ржавого металла и даже странного птенца не менее странной птицы с собой не заберу."
	"Что ни говори, а ночь здесь прекрасна."
	"Окружающая действительность всё больше и больше напоминала часть сказки. Той сказки, в которую, без преувеличения, хотел попасть каждый."
	"Ну не может всё так идеально быть, в самом деле?"
	"Конечно не может, ведь это - сон."
	"Всего лишь сон."
	"Сколько бы я ни был здесь, сколько ни бродил по округе, но ни разу не замечал всего лишь одной детали, настолько мелкой и настолько важной."
	"Куда же эти ворота ведут?"

	"А кто это там?"
	"Из-за приоткрытых створок ворот выглядывала пара любопытных глаз."
	"Хозяйка их (а я уверен, что это была именно “она”), более похожая на комок чего-то чёрного и бесформенного, но не отвратительного, пришла в это место лишь для одного - забрать меня."

	dreamgirl "Ты пойдёшь со мной?"
	me "Пойду? Но куда? И зачем?"
	"Ответа нет."
	"А был ли это вопрос?"
	"Что же. Скоро просыпаться, так почему бы не осмотреться здесь получше?.."
	
	$ cam_to(me)
	
	"[Управление: WASD/стрелки, шаг/бег: Shift]"
	window hide
	
	$ control = True
	# Свободное время, сон заканчивается, если подойти к воротам


label day0__enter__before_gates_close:
	scene bg black with dissolve
	python:
		control = False
		remove_location_object("enter", "behind_gates", "uv_night_prologue")
		gate_right.remove_animation()
		hide_location()
		day_time()
	
	play sound_loop sfx_keyboard_mouse_computer_noise fadein 3
	scene anim 1 _prologue with fade3
	pause 9.4
	scene anim 2 _prologue with fade3
	pause 9.4
	scene anim 3 _prologue with fade3
	pause 6.2
	
	python:
		set_location("flat", "armchair_pos")
		me.y -= 1
		me.set_pose("stance")
		me.set_direction(to_forward)
		me.set_dress("home")
	hide anim with dissolve

	"Недельный запас еды, тёмная комната и компьютер с доступом в интернет - всё то, что у меня есть и то, что приносило хоть какое-то удовольствие до недавнего времени."
	"Так давно полюбившиеся мною имиджборды начали надоедать."
	"В последнее время начал понимать, что загоняю себя в информационный вакуум, созданный мной же."
	"И знаете, мне это даже нравится! Не вакуум, конечно же, а его осмысление."
	"Неумелые шуточки, придуманные истории якобы из реальной жизни и просто депрессивная атмосфера - ни с чем из этого я больше не хотел связывать свою жизнь."
	"До меня дошла простая истина: хочешь что-то изменить - не сиди на пятой точке ровно."
	"…"
	"И сегодня именно тот самый “понедельник первого числа”, с которого у лентяев принято начинать что-то делать."
	"Как чувствуя, позвонил старый знакомый и позвал на встречу выпускников ВУЗа."
	"Довольно приятно, что обо мне кто-то всё ещё помнит."
	"До часа “Хэ” было ещё много времени, но всё равно стоило бы подготовиться к выходу из кельи."
	"Хотя… Про подготовку я перегнул. Если сейчас 8 утра, а встреча в 8 вечера… То у меня есть около 12 часов свободного времени, можно заняться чем-нибудь своим."
	window hide
	
	stop sound_loop fadeout 1
	
	$ me.set_pose("stance")
	$ me.move_to_place("computer")
	$ me.move_to_place("center")
	
	$ control = True
	$ day0_before_exit = False
	
	# Свободный режим
	# Варианты действий: подойти к кровати, подойти к компьютеру, подойти к двери.

label day0__flat__bed:
	if day0_before_exit:
		return
	$ control = False
	$ me.set_pose("stance")
	$ me.set_direction(to_right)
	"Просыпаться так рано совсем не свойственно для меня. Лучше будет ещё немножечко вздремнуть, не забыв поставить будильник."
	$ sunset_time()
	$ me.set_direction(to_left)
	call prologue_before_exit

label day0__flat__computer:
	if day0_before_exit:
		return
	$ control = False
	$ me.set_pose("stance")
	$ me.set_direction(to_forward)
	"К счастью, у меня есть, чем занять свободное время: нужно подыскать мастера по ремонту гитар, посмотреть подходящие вакансии для трудоустройства, ну и глянуть видео с котиками, само собой."
	$ sunset_time()
	$ me.set_direction(to_back)
	call prologue_before_exit

label day0__flat__exit:
	if day0_before_exit:
		call day0_exit
		return
	$ control = False
	$ me.set_pose("stance")
	$ me.set_direction(to_back)
	"День принято начинать с приёма пищи. Хороший завтрак не помешает будущим свершениям."
	"И мусор бы ещё вынести."
	$ sunset_time()
	$ me.set_direction(to_forward)
	call prologue_before_exit


label prologue_before_exit:
	"Пора собираться на встречу выпускников."
	"Хотя выпускником я не был (бросил учёбу после второго курса), но приятные воспоминания о времяпрепровождений с некоторыми одногруппниками до сих пор грели мне душу, так почему бы и не сходить?"
	$ control = True
	$ day0_before_exit = True
	
	$ quest_start("taking_objects")
	window hide
	# Свободный режим в комнате Семёна
	# Игроку нужно подобрать основные предметы: телефон, деньги, ключи, зажигалка...


label day0_exit:
	python:
		all_objs = True
		for obj in 'phone notepad flat_keys lighter'.split(' '):
			if not has_in_inventory(obj, 1):
				all_objs = False
				break
	if not all_objs:
		# Фразы Семёна, если он попытается уйти, не собрав все вещи
		me random.choice(day0_phrases_forgot_things)
		window hide
		return
	
	$ quest_end("taking_objects")
	
	$ me.set_dress("winter")
	$ set_location("station", "station_enter")
	$ me.set_direction(to_back)

label day0__station__before_stop:
	$ control = False
	$ me.set_pose("stance")
	$ me.set_direction(to_right)
	"И вот надо было мне собраться куда-то в такой мороз. Впрочем, уже поздно о чём-то жалеть."
	"…"
	
	window hide
	show blink
	pause 1.5
	scene bg black
	$ add_location_object("station", "liaz_place", "liaz")
	show unblink
	hide bg
	pause 1.5
	hide unblink
	
	$ me.move_to_place("liaz_enter")
	$ set_location("liaz", "liaz_enter")
	$ me.move_to_place("sit_place")
	$ me.set_direction(to_right)
	$ me.set_pose("sit")
	
	scene bg intro_xx with fade
	$ hide_location()
	
	"Разглядывая снежинки за окном, невольно подмечаешь оживлённость городских улиц."
	"А ведь сейчас зима!"
	"Время холодное, праздничные дни, а кто-то всё равно топчет только что выпавший снег."
	"Дела, заботы. Почти все чем-то заняты."
	"Кто-то не успевает купить подарки, кто-то просто торопится домой. Третий догоняет компанию друзей."
	
	window hide
	show blinking
	pause 3.5
	"Уличный неон скрывает от глаз что-то важное, значимое, но что - неизвестно."
	hide blinking
	
	"Сколько раз не пытаешься ухватиться за светящийся плакат, столько же раз и понимаешь, что всё, что там написано и нарисовано забудется через пару минут."
	"Кроме одного, пожалуй."
	"Люди. Я всегда обращал на них внимание. Не все, конечно, но очень многие выглядят совершенно по-разному."
	"За ними очень интересно наблюдать и представлять о чём они думают, что собираются делать."
	"Представляю себя детективом-профи, хоть и нет возможности проверить реальные намерения объекта наблюдений."
	
	window hide
	show blinking with dissolve
	pause 3.5
	"Интересно, кто сидел на этом месте до меня?"
	hide blinking
	
	"Даже не знаю, ну и ладно."
	"Бессмысленные рассуждения надолго отвлекли меня от поездки."
	"Я, ни разу не пользовавшийся этим маршрутом, будто попал в другой город."
	
	window hide
	show blinking with dissolve
	pause 3.5
	"И хотя близлежащие от дома окрестности мне известны хорошо, но усталость даёт о себе знать - голова не работает совершенно."
	scene bg black with dissolve
	"…"
	
	window hide
	call day1_start

