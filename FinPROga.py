"""Цвета и эффекты текста"""  

# Цвета:
BLACK = "\033[30m" # Чёрный
RED = "\033[31m" # Красный
GREEN = "\033[32m" # Зелёный
YELLOW = "\033[33m" # Жёлтый
BLUE = "\033[34m" # Синий
PURPLE = "\033[35m" # Фиолетовый
CYAN = "\033[36m" # Голубой
WHITE = "\033[37m" # Белый
GREY = "\033[90m" # Серый

# Эффекты:
RESET = "\033[0m" # СБРОС (на обычный деф текст)
BOLD = "\033[1m" # ЖИРНЫЙ ТЕКСТ
DIM = "\033[2m" # ТУСКЛЫЙ
ITALIC = "\033[3m" # КУРСИВ
UNDERLINE = "\033[4m" # ПОДЧЁРКНУТЫЙ
BLINK = "\033[5m" # МИГАЮЩИЙ
INVERSION = "\033[7m" # ИНВЕРСИЯ (Меняет цвет текста и фона местами)

import requests
from datetime import datetime

class CreditCalculator: 
    """Калькулятор расчёта кредита/ипотеки"""

    def __init__(self, debt, annual_rate, monthly_payment): # Метод для получения (инициализации) данных
        self.debt = debt # долг
        self.annual_rate = annual_rate # ставка
        self.monthly_payment = monthly_payment # ежемесячный платёж

        self.debt_start = debt # Начальный долг по кредиту
        self.monthly_rate = self.annual_rate / 100 / 12

        self.month = 0
        self.max_month = 1200
        self.debt_temp = debt

        self.min_monthly_pay = float(self.debt_start * (self.annual_rate / 100 / 12)) + 1

    def calculate(self): # Метод для расчёта
        while self.debt_temp > 0:
            self.month += 1

            if self.month > self.max_month:
                raise ValueError(f"При платеже {self.monthly_payment} руб. Кредит будет длится более 100 лет.")

            if self.monthly_payment < self.min_monthly_pay:
                raise ValueError(f"При платеже {self.monthly_payment} руб. Вы никогда не закроете кредит/ипотеку! Минимальный платёж: {round(self.min_monthly_pay, 2)}")

            self.percent = self.debt_temp * self.monthly_rate
            self.debt_temp = self.debt_temp + self.percent - self.monthly_payment

            if self.debt_temp < 0:
                self.debt_temp = 0

        self.year = self.month // 12
        self.months = self.month % 12
        self.total_paid = self.monthly_payment * self.month
        self.overpayment = self.total_paid - self.debt_start

        return { # Возвращаем данные для вывода итогов
            "month": self.month,
            "year": self.year,
            "months": self.months,
            "totalpaid": self.total_paid,
            "overpayment": self.overpayment,
            "debt_start": self.debt_start,
            "monthly_rate": self.monthly_rate,
            "annual_rate": self.annual_rate,
            "monthly_payment": self.monthly_payment
        }

now = datetime.now()
date = now.strftime("%m-%d-%Y")
time = now.strftime("%H:%M:%S\n")
years = now.strftime("%Y")

def result(data): # Результаты:
    print(f"\n" + "="*40)
    print(f"{GREEN}{BOLD}РЕЗУЛЬТАТ{WHITE}:")
    print(f"Взятая сумма кредита/ипотеки: {data['debt_start']:,} руб")
    print(f"Срок погашения кредита: {data['year']} лет(год/-а) и {data['months']} месяц(-ев)")
    print(f"{data['month']} месяц(-ев)")
    print(f"Переплата: {data['overpayment']:,.0f} руб")
    print(f"Всего отдано: {data['totalpaid']:,.0f} руб{RESET}")
    print("="*40)
    print(f"Дата расчёта кредита/ипотеки: {date}")
    print(f"Время: {time}")

    print(f"{BOLD}{PURPLE}Показать таблицу погашения по годам? (да/нет){WHITE}")

    user_input = input("Ввод: > ")
    print(f"{RESET}")

    if user_input.lower().strip() in ["да", "lf"]:

        print("\n| Год  | Остаток долга | Проценты за год |")
        print("|------|---------------|-----------------|")

        debt_tab = data['debt_start']
        monthly_rate = data['annual_rate'] / 100 / 12
        year = data['year']
        monthly_payment = data['monthly_payment']

        for year in range(1, 100):
            percent_year = 0
            for months in range(12):
                percent = debt_tab * monthly_rate
                percent_year += percent
                debt_tab = debt_tab + percent - monthly_payment
                if debt_tab < 0:
                    debt_tab = 0

            print(f"| {year:4} | {round(debt_tab, 2):>13} | {round(percent_year, 2):>14}  |")
            if debt_tab <= 0:
                print()
                break

    print(f"{BOLD}{PURPLE}\nСохранить отчёт в файл? (да/нет){WHITE}")
    user_input = input("> ")
    print(f"{RESET}")

    if user_input.lower().strip() in ["да", "lf"]:

        filename = f"Калькулятор_Кредита_Ипотеки_{now.strftime('%m.%d.%Y_%H-%M-%S')}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            """Результат"""
            f.write(f"Результат:\n")
            f.write("\n")
            f.write(f"Взятая сумма кредита/ипотеки: {data['debt_start']:,} руб\n")
            f.write(f"Срок погашения: {data['year']} лет(год/-a) и {data['months']} месяц(-ев)\n")
            f.write(f"{data['month']} месяц(-ев)\n")
            f.write(f"Переплата: {data['overpayment']:,.0f} руб\n")
            f.write(f"Всего отдано: {data['totalpaid']:,.0f} руб\n")
            f.write("="*40 + "\n")
            f.write(f"Дата расчёта кредита/ипотеки: {date}\n")
            f.write(f"Время: {time}\n")

            """Таблица погашения по годам"""
            f.write("\nТаблица погашения по годам:\n")
            f.write("\n")
            f.write("| Год  | Остаток долга | Проценты за год |\n")
            f.write("|------|---------------|-----------------|\n")

            debt_tab = data['debt_start']
            monthly_rate = data['annual_rate'] / 100 / 12
            year = data['year']
            monthly_payment = data['monthly_payment']
            
            for year in range(1, 100):
                percent_year = 0
                for months in range(12):
                    percent = debt_tab * monthly_rate
                    percent_year += percent
                    debt_tab = debt_tab + percent - monthly_payment
                    if debt_tab < 0:
                        debt_tab = 0
            
                f.write(f"| {year:4} | {round(debt_tab, 2):>13} | {round(percent_year, 2):>14}  |\n")
                if debt_tab <= 0:
                    print()
                    break

            f.write("\n\n" + "="*50 + "\n")
            f.write("Software: FinPROga\n")
            f.write("Author: ArtPROga (Artem)\n")
            f.write(f"© {years} All rigths reserved.")

        print(f"Отчёт сохранён в файл: {filename}\n")

def credit_user_data():
    print(f"\n"*2 + f"{BOLD}=== {PURPLE}FinPROga{WHITE} - модуль 1 (Калькулятор расчёта кредита/ипотеки) === ")
    while True:
        try:
            while True:
                try:
                    while True:
                        print("Введите сумму вашего кредита/ипотеки")
                        debt = int(input(f"Ввод: > "))
                       
                        if debt <= -1:
                            print(f"{RED}Ошибка: Число не может быть отрицательным!{WHITE}\n")
                            continue
                        
                        break
                    break
                
                except ValueError:
                    print(f"{RED}Ошибка: Пожалуйста, вводите только цифры!{WHITE}\n")
                    continue

            while True:
                try:
                    while True:
                        print("\nВведите ставку по вашему кредиту/ипотеке (в %.)")
                        annual_rate = input("Ввод: > ")
                    
                        annual_rate = annual_rate.replace(",", ".")
                        annual_rate = float(annual_rate)

                        if annual_rate <= -1:
                            print(f"{RED}Ошибка: Ставка не может быть отрицательной!{WHITE}")
                            continue
                        break
                    break

                except ValueError:
                    print(f"{RED}Ошибка: Пожалуйста, водите только числа!{WHITE}")
                    continue

            while True:
                try:
                    while True:
                        print("\nВведите ваш ежемесячный платёж")
                        monthly_payment = int(input("Ввод: > "))
                        print(f"{RESET}", end="")
                        if monthly_payment < 0:
                            print(f"{BOLD}{RED}Ошибка: Платёж не может быть отрицательным!{WHITE}\n")
                            continue
                        break
                    break

                except ValueError:
                    print(f"{RED}Ошибка: Пожалуйста, вводите только цифры!{WHITE}\n")
                    continue
            break

        except KeyboardInterrupt:
            print()
            return
  
    user = CreditCalculator(debt, annual_rate, monthly_payment)
    
    try:
        user_data = user.calculate()
        result(data=user_data)
    except ValueError as ve:
        print(f"\n{BOLD}{RED}Ошибка: {ve}{WHITE}")

# =============================================================================

class CurrencyConverter:
    """Конвертация валют"""
    def __init__(self, rates):
        self.rates = rates

    def convert(self, rub_amount, currency_code):

        if currency_code not in self.rates:
            raise ValueError("Валюта не найдена")

        result = rub_amount / self.rates[currency_code]
        return round(result, 2)

CURRENCIES = {
    1: ("USD", "Доллар США"),
    2: ("EUR", "ЕВРО"),
    3: ("CNY", "Юань"),
    4: ("GBP", "Фунт стерлингов"),
    5: ("JPY", "Японская иена"),
    6: ("CHF", "Швейцарский франк"),
    7: ("TRY", "Турецкая лира"),
    8: ("KZT", "Казахстанский тенге"),
    9: ("BYN", "Белорусский рубль"),
}

def currency_statistics():
    def target_currency(rates):

        converter = CurrencyConverter(rates)

        while True:
            if not rates:
                print("Данные отсутствуют")
                break

            print("\nНужно ли вам перевести рубли в зарубежную валюту? (да/нет)")
            user_answer = input("Ввод: > ")
        
            if user_answer.lower().strip() in ["да", "lf"]:
                while True:
                    print()
                    for num, (code, name) in CURRENCIES.items():
                        print(f"{num}. {code} ({name})")
                                
                    print("\nВыберите валюту (введите цифру):")          
                    currency_code = int(input("Ввод: > "))
                                                                        
                    if currency_code not in CURRENCIES:
                        print(f"\n{RED}Такой валюты нет!{WHITE}")
                        continue
                                                                        
                    code, name = CURRENCIES[currency_code]
                                                                        
                    try:
                        print("\nВведите сумму в рублях")
                        rub_amount = float(input("Ввод: > ").replace(",", "."))
                    except ValueError:
                        print(f"{RED}Ошибка: Пожалуйста, вводите только цифры/числа!{WHITE}")
                        continue

                    result = converter.convert(rub_amount, code)
                    print(f"{GREEN}РЕЗУЛЬТАТ{WHITE}: {result} {code}")
                        
                    print("Нужно рассчитать ещё? (да/нет)")
                    answer = input("Ввод: > ")
                    if answer.lower().strip() in ["да", "lf"]:
                        continue

                    else:
                        print("Выход...")
                        break

            elif user_answer.lower().strip() in ["нет", "ytn"]:
                print("Выход...")
                break
            break

    def online():
        """Онлайн режим работы."""

        try:
            response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")

            if response.status_code == 200:
                data = response.json()

                rates = {
                    "USD": data['Valute']['USD']['Value'], # Доллар
                    "EUR": data['Valute']['EUR']['Value'], # Евро
                    "CNY": data['Valute']['CNY']['Value'], # Юань
                    "GBP": data['Valute']['GBP']['Value'], # Фунт стерлингов
                    "JPY": data['Valute']['JPY']['Value'], # Японская иена
                    "CHF": data['Valute']['CHF']['Value'], # Швейцарский франк
                    "TRY": data['Valute']['TRY']['Value'], # Турецкая лира
                    "KZT": data['Valute']['KZT']['Value'], # Казахстанский тенге
                    "BYN": data['Valute']['BYN']['Value'], # Белорусский рубль
                }

                print("\n === Курсы валют: === ")
                for currency, rate in rates.items():
                    print(f"1. {currency} = {rate:.2f} RUB")
                print("="*21)
                return rates

            else:
                print("Ошибка: Не удается загрузить страницу, проверьте ваше подключение к интернету и попробуйте снова")

        except requests.exceptions.RequestException:
            print(f"{RED}Ошибка: Не удается загрузить страницу, проверьте ваше подключение к интернету и попробуйте снова{WHITE}")
            return
        
    def offline():
        """Оффлайн режим работы"""
        rates = {
            "USD": 85,
            "EUR": 95,
            "CNY": 12,
            "GBP": 100,
            "JPY": 48,
            "CHF": 95,
            "TRY": 15,
            "KZT": 15,
            "BYN": 26,
        }

        print("\n === Курсы валют: === ")
        print("Примерное значение: ")
        for code, rate in rates.items():
            print(f"1 {code} = {rate:.2f} RUB")
        print("="*21)

        return rates
 
    while True:
        try:
            print(f"\n"*2 + f"{BOLD} === {PURPLE}FinPROga{WHITE} - модуль 2 (Курс и перевод валют) === ")
            print("Выберите режим работы:")
            print("1. Онлайн режим, точный курс валют")
            print("2. Оффлайн режим, примерный курс валют")
            print("3. Выйти из модуля")

            user_answer = input("\nВведите цифру: > ")

            if user_answer == "1":
                data = online()
                target_currency(data)

            elif user_answer == "2":
                data = offline()
                target_currency(data)

            elif user_answer == "3":
                print("Выход...")
                break

            else:
                print(f"{RED}Ошибка: Пожалуйста, вводите только цифры/числа из списка!{WHITE}")
                continue

        except ValueError:
            print(f"{RED}Ошибка: Пожалуйста, вводите только цифры/числа из списка!{WHITE}")
            continue
            
        except KeyboardInterrupt:
            print()
            break

# =============================================================================

"""Использование программы"""
def user_input():
    print("\n"*10 + f"{BOLD}=== {ITALIC}{PURPLE}FinPROga{RESET}{BOLD} - {YELLOW}финансовая программа {WHITE}===")
    print("Version: 1.3.0 (STABLE)")
    print("Author: ArtPROga (ArtPRO)")
    print(f"© {years} All rigths reserved.{RESET}")

    while True:
        try:
            print(f"\n{BOLD} === {ITALIC}{PURPLE}FinPROga{RESET}{BOLD} - {YELLOW}главное меню {WHITE}===")
            print("Выберите нужный инструмент: ")
            print("1. Калькулятор расчёта кредита/ипотеки")
            print("2. Курс и перевод валют")
            print(f"3. Выход из программы{RESET}")
            
            user_input = input(f"\n{BOLD}Введите цифру: >{YELLOW} ")
            print(f"{RESET}", end="")
            if user_input.strip() == "1":
                credit_user_data()

            elif user_input.strip() == "2":
                currency_statistics()

            elif user_input.strip() == "3":
                print(f"{PURPLE}{BOLD}До свидания! Спасибо за ваш визит{RESET}")
                break

            else:
                print("\n"*10 + f"{BOLD}{YELLOW}Пожалуйста, вводите {UNDERLINE}ТОЛЬКО ЦИФРЫ{RESET}{YELLOW}{BOLD} из списка!{RESET}")
                continue

        except KeyboardInterrupt:
            print(f"\n{PURPLE}{BOLD}До свидания! Спасибо за ваш визит{RESET}")
            break

if __name__ == "__main__":
    user_input()