# taking_objects

init:
	$ taking_objects__name = "Сбор вещей"


label taking_objects__start:
	"Начат квест <Сбор вещей>."
	
	"Перед выходом из дома нужно захватить с собой необходимые вещи (4 штуки)."
	"[Для этого нужно подойти к предмету и взять его в инвентарь, нажав E (англ.)]"
	"[Нажав I, можно открыть/закрыть инвентарь]"
	window hide

label taking_objects__end:
	"Квест <Сбор вещей> завершён."
	window hide


label taking_objects__on__taking__notepad:
	"[Блокнот]"
	extend "\nМой блокнот. Старый, поношенный. Не из-за частого использования, правда, а просто постарел со временем. Только взяв в руки и раскрыв, я почуял приятный аромат старых книг."
	"Когда же я его покупал, интересно?"
	"На первых страницах ещё остались первые потуги в описании своей жизни. Правда, из-за отсутствия оного и попросту желания что-то делать, я на него забил."
	"Было бы неплохо возобновить традицию. И ручку не забыть взять."
	window hide

label taking_objects__on__taking__phone:
	"[Телефон]"
	extend "\nТелефон всегда нужно носить с собой. Хоть по нему практически никто не звонит, он всё равно служит отличной медиатекой."
	window hide

label taking_objects__on__taking__moneys:
	"[Деньги]"
	extend "\nНа обратном пути необходимо зайти за продуктами. К тому же, билет тоже стоит денег. Всего здесь около 1050 российских рублей, должно на всё хватить."
	window hide

label taking_objects__on__taking__flat_keys:
	"[Ключи]"
	extend "\nБез ключей не попасть домой. Да и не выйти тоже."
	window hide

label taking_objects__on__taking__lighter:
	"[Зажигалка]"
	extend "\nКурение - ещё один из моих пороков. К слову, стал замечать, что потребление сигарет сильно уменьшилось, как и желание курить."
	window hide

