# Дата 09.11.2026. ФИО: КУзьмин Виталий Иванович. Время: 14:50.
# Установка библиотеки. 


# uv self update
# uv add playwright
# playwright install

# Я скопировал пример из раздела «Написание тестов» и запустил его локально
# playwright.dev проверяет, содержит ли заголовок страницы слово «Playwright».
# Описание: Этот код запускает браузер Chromium, открывает страницу
# Время: 15:06

# from playwright.sync_api import sync_playwright # берем из sync_playwright штучку playwright.sync_api

# with sync_playwright() as p:   # с функции sync_playwright() берем и сохраняем результат в p
    # browser = p.chromium.launch() # запускаем браузер
    # page = browser.new_page() # открываем страницу браузера
    # page.goto("https://playwright.dev") # открываем сайт
    # print(page.title()) # выводим Титул со странички
    # browser.close() # Закрываем браузер

# Результат запуска: "Fast and reliable end-to-end testing for modern web apps | Playwright"
# Код выполнен без ошибок.

# Ассинхронный вариант

# import asyncio
# from playwright.async_api import async_playwright

# async def main():
    # async with async_playwright() as p:
        # browser = await p.chromium.launch()
        # page = await browser.new_page()
        # await page.goto("https://playwright.dev")
        # print(await page.title())
        # await browser.close()

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



# я поработал в интерактивном REPl Python
# фотографии работы: rabota1.png and rabota2.png


# работа с PyInstaller

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

