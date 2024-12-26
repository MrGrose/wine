import os
from collections import defaultdict
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape


def calculate_years_since_founding(founding_year: int) -> int:
    current_year = datetime.now().year
    return current_year - founding_year


def get_year_suffix(years: int) -> str:
    last_digit_of_years = years % 10
    last_two_digits_of_years = years % 100

    if last_two_digits_of_years in range(11, 15):
        return 'лет'
    elif last_digit_of_years == 1:
        return 'год'
    elif last_digit_of_years in [2, 3, 4]:
        return 'года'
    else:
        return 'лет'


def load_and_group_wines(file_path: str) -> dict[str, list[dict[str, int]]]:
    wine_data = pandas.read_excel(file_path, keep_default_na=False)
    grouped_wines = wine_data.groupby('Категория')
    return defaultdict(
        list,
        {category: group.to_dict(orient='records')
         for category, group in grouped_wines},
    )


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')

    founding_year = 1920
    years_since_founding = calculate_years_since_founding(founding_year)
    year_suffix = get_year_suffix(years_since_founding)

    WINE_DATA_PATH = os.environ.get('WINE_DATA_PATH', 'wine.xlsx')
    categorized_wines = load_and_group_wines(WINE_DATA_PATH)

    rendered_page = template.render(
        difference_years=years_since_founding,
        year_text=year_suffix,
        wines=categorized_wines,
    )
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
