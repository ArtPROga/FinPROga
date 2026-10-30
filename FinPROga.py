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
    print("\n" + "="*40)
    print("РЕЗУЛЬТАТ:")
    print(f"Взятая сумма кредита/ипотеки: {data['debt_start']:,} руб")
    print(f"Срок погашения кредита: {data['year']} лет(год/-а) и {data['months']} месяц(-ев)")
    print(f"{data['month']} месяц(-ев)")
    print(f"Всего отдано: {data['totalpaid']:,.0f} руб")
    print(f"Переплата: {data['overpayment']:,.0f} руб")
    print("="*40)
    print(f"Дата расчёта кредита/ипотеки: {date}")
    print(f"Время: {time}")

    print("Показать таблицу погашения по годам? (да/нет)")

    user_input = input("> ")

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

    print("\nСохранить отчёт в файл? (да/нет)")
    user_input = input("> ")
    if user_input.lower().strip() in ["да", "lf"]:

        filename = f"Калькулятор_Кредита_Ипотеки_{now.strftime('%m.%d.%Y_%H-%M-%S')}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            """Результат"""
            f.write(f"Результат:\n")
            f.write("\n")
            f.write(f"Взятая сумма кредита/ипотеки: {data['debt_start']:,} руб\n")
            f.write(f"Срок погашения: {data['year']} лет(год/-a) и {data['months']} месяц(-ев)\n")
            f.write(f"{data['month']} месяц(-ев)\n")
            f.write(f"Всего отдано: {data['totalpaid']:,.0f} руб\n")
            f.write(f"Переплата: {data['overpayment']:,.0f} руб\n")
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
    print("\n === FinPROga - модуль 1 (Калькулятор расчёта кредита/ипотеки) === ")
    while True:
        try:
            while True:
                try:
                    while True:
                        print("Введите сумму вашего кредита/ипотеки")
                        debt = int(input("Ввод: > "))
                        if debt <= -1:
                            print("Ошибка: Число не может быть отрицательным!\n")
                            continue
                        
                        break
                    break
                
                except ValueError:
                    print("Ошибка: Пожалуйста, вводите только цифры!\n")
                    continue

            while True:
                try:
                    while True:
                        print("\nВведите ставку по вашему кредиту/ипотеке (в %.)")
                        annual_rate = input("Ввод: > ")
                        annual_rate = annual_rate.replace(",", ".")
                        annual_rate = float(annual_rate)

                        if annual_rate <= -1:
                            print("Ошибка: Ставка не может быть отрицательной!\n")
                            continue
                        break
                    break

                except ValueError:
                    print("Ошибка: Пожалуйста, водите только числа!\n")
                    continue

            while True:
                try:
                    while True:
                        print("\nВведите ваш ежемесячный платёж")
                        monthly_payment = int(input("Ввод: > "))
                        if monthly_payment < 0:
                            print("Ошибка: Платёж не может быть отрицательным!\n")
                            continue
                        break
                    break

                except ValueError:
                    print("Ошибка: Пожалуйста, вводите только цифры!\n")
                    continue
            break

        except KeyboardInterrupt:
            print()
            break
  
    user = CreditCalculator(debt, annual_rate, monthly_payment)
    user_data = user.calculate()
    result(data=user_data)

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
            print("\nНужно ли вам перевести рубли в зарубежную валюту? (да/нет)")
            user_answer = input("> ")
        
            if user_answer.lower().strip() in ["да", "lf"]:
                for num, (code, name) in CURRENCIES.items():
                    print(f"{num}. {code} ({name})")
                            
                print("\nВыберите валюту (введите цифру):")          
                currency_code = int(input("Ввод: > "))
                                                                    
                if currency_code not in CURRENCIES:
                    print("Такой валюты нет!")
                    continue
                                                                    
                code, name = CURRENCIES[currency_code]
                                                                    
                try:
                    print("Введите сумму в рублях")
                    rub_amount = float(input("Ввод: > ").replace(",", "."))
                except ValueError:
                    print("Ошибка: Пожалуйста, вводите только цифры!")
                    continue

                
                result = converter.convert(rub_amount, code)
                print(f"Результат: {result} {code}")

                    
                print("Нужно рассчитать ещё? (да/нет)")
                answer = input("Ввод: > ")
                if answer.lower().strip in ["да", "lf"]:
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

        response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")

        try:
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
                print("="*30)

                return rates

            else:
                print("Ошибка: Не удается загрузить страницу, проверьте ваше подключение к интернету и попробуйте снова")

        except ConnectionError:
            print(f"Ошибка: Не удается загрузить страницу, проверьте ваше подключение к интернету и попробуйте снова")


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

        print(f" === Курсы валют: === ")
        print("Примерное значение: ")
        for code, rate in rates.items():
            print(f"1 {code} = {rate:.2f} RUB")
            print("=" * 30)

        return rates

    while True:
        try:
            print("\n === FinPROga - модуль 2 (Курс и перевод валют) === ")
            print("Выберите режим работы:")
            print("1. Онлайн режим, точный курс валют")
            print("2. Оффлайн режим, примерный курс валют")
            print("3. Выйти из модуля")

            user_answer = input("Введите цифру: > ")
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
                print("Ошибка: Пожалуйста, вводите только цифры/числа из списка!")
                continue

        except ValueError:
            print("Ошибка: Пожалуйста, вводите только цифры/числа из списка!")
            continue
            
        except KeyboardInterrupt:
            print()
            break

# =============================================================================

"""Использование программы"""
def user_input():
    print("\n"*10 + "=== FinPROga - финансовая программа ===")
    print("Version: 1.2.0 (BETA)")
    print("Author: ArtPROga (ArtPRO)")
    print(f"© {years} All rigths reserved.")

    while True:
        try:
            print("\n === FinPROga - главное меню ===")
            print("Выберите нужный инструмент: ")
            print("1. Калькулятор расчёта кредита/ипотеки")
            print("2. Курс и перевод валют")
            print("3. Выход из программы")
            
            user_input = input("\nВведите цифру: > ")
            if user_input.strip() == "1":
                credit_user_data()

            elif user_input.strip() == "2":
                currency_statistics()

            elif user_input.strip() == "3":
                print("До свидания! Спасибо за ваш визит")
                break

            else:
                print("\n"*10 + "Пожалуйста, вводите только цифры из списка!")
                continue

        except KeyboardInterrupt:
            print("\nДо свидания! Спасибо за ваш визит")
            break

user_input()