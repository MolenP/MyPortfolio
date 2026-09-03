#----------------------Добро пожаловать----------------------#

"""

Приветствую вас, я сделал этот код для создания портфолио себе,
но вы также можете настроить это портфолио под себя в разделе "Создание портфолио", изменив данные.
Я надеюсь вам понравится мой довольно универсальный настраиваемый код, я старался:),

Тут есть все подсказки что-где-зачем нужно, удачи:)

И не изменяйте там где этого не надо, а то программа может сломаться:(


"""

#----------------------Начало кода----------------------#

import keyboard
import os
import colorama

"""

Если у вас библиотека keyboard подчеркивается желтой линией,
то вам нужно установить ее, открыв терминал и введя данную команду: pip install keyboard

То же самое с Colorama: pip install colorama 

"""

colorama.init()

class Portfolio:
    def __init__(self, 
                name, 
                age, 
                What_am_i_doing, 
                facts, 
                purpose, 
                How_did_i_came_to_IT, 
                teachers_info,
                progress,
                hobby,
                best_works,
                GitHub_link):
        self.name = name
        self.age = age
        self.What_am_i_doing = What_am_i_doing
        self.facts = facts
        self.purpose = purpose
        self.How_did_i_came_to_IT = How_did_i_came_to_IT
        self.teachers_info = teachers_info
        self.progress = progress
        self.hobby = hobby
        self.best_works = best_works
        self.GitHub_link = GitHub_link

#-------------Функции-------------#

def O_sebe():
    os.system("cls")
    print(f"---------------О себе---------------\n"
            f"Мое имя: {my_portfolio.name}\n"
            f"Мой возраст: {my_portfolio.age}\n"
            f"Чем я занимаюсь: {my_portfolio.What_am_i_doing}\n"
            f"Факты обо мне: {my_portfolio.facts}"
            f"\n\n{colorama.Fore.GREEN}Чтобы выйти нажмите Escape{colorama.Style.RESET_ALL}"
        )
    while True:
        if keyboard.is_pressed("Escape"):
            break
    os.system("cls")

def my_purpose():
    os.system("cls")
    print(f"---------------Моя цель---------------\n"
            f"{my_portfolio.purpose}"
            f"\n\n{colorama.Fore.GREEN}Чтобы выйти нажмите Escape{colorama.Style.RESET_ALL}"
        )
    while True:
        if keyboard.is_pressed("Escape"):
            break
    os.system("cls")

def how_i_came_to_IT():
    os.system("cls")
    print(f"---------------Как я пришел в IT---------------\n"
            f"{my_portfolio.How_did_i_came_to_IT}"
            f"\n\n{colorama.Fore.GREEN}Чтобы выйти нажмите Escape{colorama.Style.RESET_ALL}"
        )
    while True:
        if keyboard.is_pressed("Escape"):
            break
    os.system("cls")

def moy_mentor():
    os.system("cls")
    print(f"---------------Мой ментор---------------\n"
            f"{my_portfolio.teachers_info}"
            f"\n\n{colorama.Fore.GREEN}Чтобы выйти нажмите Escape{colorama.Style.RESET_ALL}"
        )
    while True:
        if keyboard.is_pressed("Escape"):
            break
    os.system("cls")

def my_progress():
    os.system("cls")
    print(f"---------------Мой прогресс---------------\n"
            f"{my_portfolio.progress}"
            f"\n\n{colorama.Fore.GREEN}Чтобы выйти нажмите Escape{colorama.Style.RESET_ALL}"
        )
    while True:
        if keyboard.is_pressed("Escape"):
            break
    os.system("cls")

def my_hobby():
    os.system("cls")
    print(f"---------------Хобби и интересы---------------\n"
            f"{my_portfolio.hobby}"
            f"\n\n{colorama.Fore.GREEN}Чтобы выйти нажмите Escape{colorama.Style.RESET_ALL}"
        )
    while True:
        if keyboard.is_pressed("Escape"):
            break
    os.system("cls")

def my_best_works():
    os.system("cls")
    print(f"---------------Мои лучшие работы---------------\n"
            f"{my_portfolio.best_works}"
            f"\n\n{colorama.Fore.GREEN}Чтобы выйти нажмите Escape{colorama.Style.RESET_ALL}"
        )
    while True:
        if keyboard.is_pressed("Escape"):
            break
    os.system("cls")

def my_github_link():
    os.system("cls")
    print(f"---------------Ссылка на GitHub---------------\n"
            f"Ссылка на GitHub: {colorama.Fore.CYAN}{my_portfolio.GitHub_link}{colorama.Style.RESET_ALL}"
            f"\n\n{colorama.Fore.GREEN}Чтобы выйти нажмите Escape{colorama.Style.RESET_ALL}"
        )
    while True:
        if keyboard.is_pressed("Escape"):
            break
    os.system("cls")
    


#-------------Обучение по партфолио(ОБЯЗАТЕЛЬНО ПРОЧИТАТЬ!)-------------#

"""

Обучение как сделать свою IT Портфолио:
    Впиши свою информацию в соответствующую линию ниже внутри ковычек.

    Все данные кроме возраста(в возрасте просто впишите число) должны быть в текстовом формате(String),
    их можно сделать просто добавив ковычки, а далее уже в них мы пишем свой текст

    Если у тебя очень длинный текст в поле, 
    то ты должен открыть скобку в начале и перейти на следующую строку,
    (если у тебя две скобки, то ты должен навести курсор на середину между скобок и нажать ENTER)
    далее ты должен открыть ковычки и вписать свои данные,
    потом закрываешь ковычки и опять переходишь на следующую строку
    и так раз за разом, чтобы строка не была такой длинной для эстетики.
        ПРИМЕР:
            facts = (
                "Очень длинный текст"
                "Очень длинный текст"
                "Очень длинный текст"
            )

    кстати, некоторую информацию вы должны написать полностью, 
        ПРИМЕР:"я занимаюсь ..." или "мое любимое хобби это ..." и почему это твое любимое хобби
    я обозначу там где это надо плюсиком "+" в комментариях, которые отображены серым цветом

"""

#------------Создание Портфолио(Вы можете изменить данные под себя)-----------#

#Ваше имя
name = "Ерлан"

#Ваш возраст, вместо number введи число и удали ковычки
age = 16 

#Чем вы занимаетесь, +
What_am_i_doing = "Я пишу этот код" 

#Факты о вас, +
facts = "Я скромный, люблю играть в ПК" 

#Зачем ты пришел в программирование/дизайн и к чему идешь +
purpose = "Я пришел в программирование с целью получить знания в этой сфере для моего будущего" 

#Как вы пришли к IT, +
How_did_i_came_to_IT = (
    "Я полюбил программирование из-за хакеров, которые взламывают системы, камеры и тому подобное, в Watch Dogs 2 играл, "
    "но я конечно если и буду взламывать, то только по заданию а не в своих целях:),"
    "еще я просто хочу игры создавать"
) 

#Ваш учитель/ментор в программировании и информация о нем/ней, +
teachers_info = (
    "Мой учитель - это Молдыр Капал, хороший и добрый учитель, не ругает, "
    "плохого о ней я сказать ничего не могу, потому что нечего, "
    "коротко говоря, хороший и добрый ментор:)"
) 

#Ваш прогресс(от точки А до точки Б), +
progress = (
    "Я, если честно, пришел в курс уже с довольно неплохим опытом в роблокс студио, где я тоже программировал, "
    "и в пайтоне тоже до этого имел дело, но не такие как с роблоксом, что-то типо просто написать input(...) в пайтоне, "
    "но больше ничего особенного не было в нем, но сейчас я перехожу в Middle разработчика Python(ну наверно), уже создаю легкого телеграм бота. "
    "Если честно, то у меня очень хороший прогресс, я многое узнал и мне это точно пригодится как трамплин к следующим языкам программирования, "
    "я вполне доволен"
)
            

#Ваше хобби или занятие, +
hobby = "я люблю играть в видеоигры, могу еще попрограммировать в роблоксе, либо делать карту в Osu!." 

#Ваши лучшие работы, желательно вписать название, описание, ссылка, +
best_works = (
    "Моя лучшая работа - это 2-ая проектная работа под названием\n"
    "'Проектная работа: Образовательное приложение с карточками, викториной и заметками'\n\n"
    "в данной работе, я должен был сделать очень сложную для меня систему, а именно викторину(Вопрос, а на него ответ). "
    "Из-за этой работы я не мог нормально думать и играть, так как всегда в голове держалась мысль, "
    "что я не успею сделать её если буду только играть, но к счастью справился за две недели. "
    "Я сталкивался с багами, нужно было обходить некоторые проблемы, придумывать систему, короче беда."
    "но, переборов себя, закинув очень много вопросов чату гпт(кстати очень сильно помог с реализацией, "
    "но я его не абьюзил и не копировал код, использовал только в безвыходных для меня ситуаций, и я все его коды разбирал) "
    "я все таки это сделал, как камень с плеч был. Эта работа проверяла мою выносливость и выдержку, "
    "но я прошел. Эта работа показала, насколько может быть проблемен проект. Но я благодарен этой работе. "
    "Я много чего взял с неё.\n"
    "Ссылка на данную работу: https://capeducation.getcourse.ru/pl/teach/control/lesson/view?id=341874479&editMode=0"
)

#Ссылка на ваш проект/портфолио
GitHub_link = "https://github.com/MolenP/Portfolio.git" 

#--------------------------------------------------------------

my_portfolio = Portfolio(name,
                        age, 
                        What_am_i_doing, 
                        facts, 
                        purpose, 
                        How_did_i_came_to_IT, 
                        teachers_info,
                        progress,
                        hobby,
                        best_works,
                        GitHub_link)
        
while True:
    os.system("cls")
    print("---------------Меню---------------\n" \
        "Приветствую, Это мое портфолио, чего хотели бы?(Выбери цифру на клавиатуре)\n" \
        "1) О себе\n" \
        "2) Моя цель\n" \
        "3) Как я пришел в IT\n" \
        "4) Мой ментор\n" \
        "5) Мой прогресс(Точка А ---> Точка Б)\n" \
        "6) Хобби и интересы\n" \
        "7) Мои лучшие работы\n" \
        "8) Ссылка на GitHub\n"
        )
    while True:
        if keyboard.is_pressed("1"):
            os.system("cls")
            O_sebe()
            break

        if keyboard.is_pressed("2"):
            os.system("cls")
            my_purpose()
            break

        if keyboard.is_pressed("3"):
            os.system("cls")
            how_i_came_to_IT()
            break

        if keyboard.is_pressed("4"):
            os.system("cls")
            moy_mentor()
            break

        if keyboard.is_pressed("5"):
            os.system("cls")
            my_progress()
            break

        if keyboard.is_pressed("6"):
            os.system("cls")
            my_hobby()
            break

        if keyboard.is_pressed("7"):
            os.system("cls")
            my_best_works()
            break

        if keyboard.is_pressed("8"):
            os.system("cls")
            my_github_link()
            break
