# Сайт винного магазина

Этот проект представляет собой генератор статического сайта для винного магазина, написанный на Python. Скрипт создает HTML-страницу с каталогом вин, сгруппированных по категориям, и запускает локальный веб-сервер для отображения результата.

## Описание
- Расчет количества лет с момента основания магазина
- Загрузка данных о винах из Excel-файла
- Группировка вин по категориям
- Генерация HTML-страницы с использованием шаблона Jinja2
- Запуск локального веб-сервера для отображения сгенерированной страницы

## Основные компоненты
`calculate_years_since_founding()`: Вычисляет количество лет с момента основания магазина.

`get_year_suffix()`: Возвращает правильное склонение слова "год" на русском языке.

`load_and_group_wines()`: Загружает данные о винах из Excel-файла и группирует их по категориям.

`main()`: Генерирует HTML-страницу и запускает локальный веб-сервер.

## Установка и запуск
1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/your-username/wine-shop-generator.git
    cd wine-shop-generator
    ```
2. Создайте виртуальное окружение и активируйте его:
    ```bash
    python -m venv venv
    source venv/bin/activate # Для Unix
    venv\Scripts\activate # Для Windows
    ```
3. Убедитесь, что у вас установлены все необходимые зависимости.
    ```bash
    pip install -r requirements.txt
    ```
    
4.  Подготовьте файл `wine.xlsx` с данными о винах. Файл должен содержать колонку "Категория" и другие необходимые данные о винах (см. пример ниже).
    ```text
    | Категория   | Название         | Цена   |
    |-------------|------------------|--------|
    | Красные вина| Каберне Совиньон | 1200   |
    | Белые вина  | Шардоне          | 900    |

    Убедитесь, что колонка "Категория" присутствует, так как она используется для группировки вин.
    ```
5. Создайте HTML-шаблон template.html в той же директории.
6. Запустите скрипт:
    
    Без указанию пути (по умолчанию на файл wine.xlsx):
    ```bash
    python main.py
    ```
    С указанием пути:
    ```bash
    python main.py --wine-data /Ваш/путь/до/файла/ваш_файл.xlsx
    ```
7. Откройте браузер и перейдите по адресу http://localhost:8000 для просмотра сгенерированной страницы.
8. Для остановки сервера нажмите Ctrl+C в терминале.


## Настройка
- Год основания магазина можно изменить, отредактировав переменную founding_year в функции main().
- Путь к файлу с данными о винах можно изменить в вызове функции load_and_group_wines().
- Имя HTML-шаблона можно изменить в вызове env.get_template().
- Путь к файлу с данными о винах можно указать через переменную окружения WINE_DATA_PATH. Если переменная не задана используется значение по умолчанию 'wine.xlsx'. 

    Пример использования:
    ```bash
    WINE_DATA_PATH=/path/to/your/wine_data.xlsx python main.py
    ```
## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
