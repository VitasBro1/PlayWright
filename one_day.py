# Дата 09.11.2026. ФИО: КУзьмин Виталий Иванович. Время: 14:50.
# Установка библиотеки. 


# uv self update
# uv add playwright
# playwright install

# Я скопировал пример из раздела «Написание тестов» и запустил его локально
# playwright.dev проверяет, содержит ли заголовок страницы слово «Playwright».
# Описание: Этот код запускает браузер Chromium, открывает страницу
# Время: 15:06

from playwright.sync_api import sync_playwright # берем из sync_playwright штучку playwright.sync_api

with sync_playwright() as p:   # с функции sync_playwright() берем и сохраняем результат в p
    browser = p.chromium.launch() # запускаем браузер
    page = browser.new_page() # открываем страницу браузера
    page.goto("https://playwright.dev") # открываем сайт
    print(page.title()) # выводим Титул со странички
    browser.close() # Закрываем браузер

# Результат запуска: "Fast and reliable end-to-end testing for modern web apps | Playwright"
# Код выполнен без ошибок.

# Ассинхронный вариант

import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://playwright.dev")
        print(await page.title())
        await browser.close()

asyncio.run(main()) # завершает цикл событий




