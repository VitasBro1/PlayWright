# Дата 09.11.2026. ФИО: КУзьмин Виталий Иванович. Время: 14:50.
""" Установка библиотеки. """ 


# uv self update
# uv add playwright
# playwright install

# Я скопировал пример из раздела «Написание тестов» и запустил его локально
# playwright.dev проверяет, содержит ли заголовок страницы слово «Playwright».
# Описание: Этот код запускает браузер Chromium, открывает страницу
# Время: 15:06

#from playwright.sync_api import sync_playwright # берем из sync_playwright штучку playwright.sync_api

#with sync_playwright() as p:   # запускаем sync_playwright() берем и сохраняем результат в p
 #   browser = p.chromium.launch() # запускаем браузер
  #  page = browser.new_page() # открываем страницу браузера
   # page.goto("https://store.steampowered.com/") # открываем сайт
    #print(page.title()) # выводим Титул со странички
    # browser.close() # Закрываем браузер
# Результат запуска: "Fast and reliable end-to-end testing for modern web apps | Playwright"
# Код выполнен без ошибок.

""" Модифицированный код 
from playwright.sync_api import sync_playwright  # импортируем sync_playwright

with sync_playwright() as p:  # запускаем sync_playwright(), сохраняем в p
    browser = p.chromium.launch(channel="chromium")  # запускаем браузер chromium (собранный playwright)
    page = browser.new_page()  # открываем страницу браузера
    page.goto("https://store.steampowered.com/") # открываем сайт
    print("Title:", page.title())  # выводим заголовок страницы
    browser.close()  # закрываем браузер

Время 23:50. ФИО: Кузьмин Виталий Иванович. Дата: 11.11.2026 """



""" Ассинхронный вариант """



# asyncio.run(main()) # завершает цикл событий

# Результат запуска: "Fast and reliable end-to-end testing for modern web apps | Playwright"
# Код выполнен без ошибок.

# выполнение скриншота
# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
    # browser = p.webkit.launch(headless=False, slow_mo=500) # запускает браузер firefox
    # page = browser.new_page()
    # page.goto("https://playwright.dev/")
    # page.screenshot(path="example.png", full_page=True)
    # browser.close()

# изменен код для того, чтобы увидеть пользовательский интерфейс

""" Модифицированный код №2"""
"""Время 14:41. Дата 12.11.2026. ФИО: Кузьмин Виталий Иванович"""
#from playwright.sync_api import sync_playwright

#with sync_playwright() as p:
    #browser = p.webkit.launch(headless=False, slow_mo=500)  # запускает браузер WebKit (Safari)
    #page = browser.new_page()
    #page.goto("https://github.com/VitasBro1", wait_until="networkidle") # ждет пока сайт перестанет что то грузить по сети и только потом идет дальше
    #page.screenshot(path="example.png", full_page=True)
    #browser.close()


""" REPL Python """
# я поработал в интерактивном REPl Python
# фотографии работы: rabota1.png and rabota2.png


""" работа с PyInstaller """

# Дата 10.11.2026. Время: 13:25. ФИО: Кузьмин Виталий Иванович
# ДЕНЬ 2

# Использование Playwright c Pyinstaller для создания автономных исполняемых файлов
# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
    # browser = p.chromium.launch()
    # page = browser.new_page()
    # page.goto("https://playwright.dev/")
    # page.screenshot(path="example2.png")
    # browser.close()

# Код выполнен. Скриншот был сделан.

# Для того чтобы обьединить браузеры с исполняемыми файлами:

# PLAYWRIGHT_BROWSERS_PATH=0 playwright install chromium
# pyinstaller -F main.py

""" Известные проблемы """

# в Playwright есть автоматическое ожидание.
# Вместо time.sleep(5) используйте page.wait_for_timeout(5000)
# Иногда лучше использовать wait_for_timeout вместо модуля time. Ведь Асинхронные операции могут старым способом может обрабатываться некорректно

# НЕСОВМЕСТИМОСТЬ SelectorEventLoop с asyncio.
# selectorEventLoop не поддерживает асинхронные подпроцессы

# Threading
#    API Playwright не безопасный. При многопоточности надо создавать отдельный поток.

# Отмена asyncio задач
#    Если задача долго обрабатывается запустите в отдельной задаче и защитите с помощью asyncio.shield()
"""----------------------------------------------------------------------------------------------------------"""
"""                                              Действия                                                    """
"""----------------------------------------------------------------------------------------------------------"""

""" Введение """
# Playwright умеет работать с:
# полями ввода, чекбоксами, радиокнопками, выпадающими списками, кликами, вводом текста, клавишами и сочетаниями, загрузкой файлов и фокусом на элементах
""" Ввод текста """
# locator.fill() это самый простой способ заполнит поля формы. Элемент фукусируется и запускает input
""" Флажки и переключатели """
# установить или снять флажок или переключатель -  locator.set_checked(). Метод используется с input[type=checkbox], input[type=radio] и [role=checkbox].
""" Параметры """
# Выбирается один или несколько параметров через <select> с помощью locator.select_option()
# Параметр можно указать value or label. Можно выбрать несколько
""" Mouse click """
# может выполнить обычный щелчок как человек

# Принудительный щелчок
"""! page.get_by_role("button").click(force=True) !"""
# Программный клик
# Можно вызвать поведение HTMLElement.click() простым нажатием на элемент с помощью locator.dispatch_event()
""" ! page.get_by_role("button").dispatch_event('click') ! """
# Все ассинхронные варианты добавляются в начале с командой await

""" Ввод символов """
# ВАЖНО!!!! В большинстве случаев текст следует вводить с помощью locator.fill(). Вводить надо только в случае спец клавиатуры на сайте.
# Вводить текст надо посимвольно, через locator.press_sequentially()
""" page.locator('#area').press_sequentially('Hello World!') """
# Все ассинхронные варианты добавляются в начале с командой await
# Этот метод генерирует все необходимые события клавиатуры, включая события keydown, keyup, keypress
# Можно указать delay в промежутке, для имитации действий реального пользователя

""" Клавиши и сочетания клавиш """
# locator.press() фокусирует выбранный элемент и выполняет одно нажатие клавиши
# Через  keyboardEvent.key передаются логические значения клавиш
"""page.locator('#name').press('Shift+A')
page.locator('#name').press('Shift+ArrowLeft') """
# Все ассинхронные варианты добавляются в начале с командой await

""" Загрузка файлов """
# Входные файлы для загрузки выбираются методом  locator.set_input_files(). 
# В массиве можно указать несколько файлов
# Можно обработать событие page.on("filechooser") если нет элемента ввода или использовать метод ожидания
""" with page.expect_file_chooser() as fc_info:
    page.get_by_label("Upload file").click()
file_chooser = fc_info.value
file_chooser.set_files("myfile.pdf") """
# Все ассинхронные варианты добавляются в начале с командой await

""" Элемент фокуса """
# На динамический сайтах с обработкой фокуса можно использовать метод locator.focus()
""" page.get_by_label('password').focus() """
# Все ассинхронные варианты добавляются в начале с командой await

""" Перетаскивание """
# Выполняет операцию перетаскивания с помощью locator.drag_to(). 
# Порядок действий:
# 1. Навести курсор на элемент, который будет перетаскиваться.
# 2. Нажмите левую кнопку мыши.
# 3. Наведите курсор мыши на элемент, который будет удален.
# 4. Отпустите левую кнопку мыши.
""" page.locator("#item-to-be-dragged").drag_to(page.locator("#item-to-drop-at")) """
# Все ассинхронные варианты добавляются в начале с командой await
""" Перетаскивание вручную """
# Для контроля перетаскивания вручную использовать locator.hover(), mouse.down(), mouse.move() и mouse.up().abs
""" page.locator("#item-to-be-dragged").hover()
page.mouse.down()
page.locator("#item-to-drop-at").hover()
page.mouse.up() """
# Все ассинхронные варианты добавляются в начале с командой await

""" Прокрутка """
# Почти всегда Playwright автоматически выполняет прокрутку перед выполнением каких-либо действий, вручную ничего крутить не надо
""" page.get_by_role("button").click() """
# Все ассинхронные варианты добавляются в начале с командой await
# Иногда требуется ручная прокрутка. Следует найти элемент нужный и прокрутить страницу чтобы он был в поле зрения.abs
""" page.get_by_text("Footer text").scroll_into_view_if_needed() """
# Все ассинхронные варианты добавляются в начале с командой await
# Если требуется более точно управлять, использовать  mouse.wheel() или locator.evaluate()
""" page.get_by_test_id("scrolling-container").hover()
page.mouse.wheel(0, 10)

page.get_by_test_id("scrolling-container").evaluate("e => e.scrollTop += 100") """
# Все ассинхронные варианты добавляются в начале с командой await

"""----------------------------------------------------------------------------------------------------------"""
"""                                         Автоматическое ожидание                                          """
"""----------------------------------------------------------------------------------------------------------"""

""" Ввод текста """
#
