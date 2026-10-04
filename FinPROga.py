# 1 инструмент
import requests
import sys

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
    def convert_currency(rates):
        # Универсальная конвертация валют
        while True:
            for num, (code, name) in CURRENCIES.items():
                print(f"{num}. {code} ({name})")
            
            print("\nВыберите валюту (введите цифру):")
            
            try:
                money = int(input("Ввод: "))
            except ValueError:
                print("Введите число!")
                continue
            
            if money not in CURRENCIES:
                print("Такой валюты нет!")
                continue
            
            code, name = CURRENCIES[money]
            
            try:
                rub = float(input("Введите сумму в рублях: ").replace(",", "."))
            except ValueError:
                print("Введите число!")
                continue
            
            result = rub / rates[code]
            print(f"{rub} РУБЛЕЙ = {result:.2f} {code}")
            
            answer = input("Нужно рассчитать еще? (да/нет): ")
            if answer.lower() not in ["да", "lf"]:
                print("До свидания!")
                sys.exit()

    def online():
        # ОНЛАЙН РЕЖИМ: (С ИНТЕРНЕТОМ, точное значение) --------------------------------------
        response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")

        if response.status_code == 200:
            data = response.json()

            rates = {
                "USD": data['Valute']['USD']['Value'],  # Доллар
                "EUR": data['Valute']['EUR']['Value'],  # Евро
                "CNY": data['Valute']['CNY']['Value'],  # Юань
                "GBP": data['Valute']['GBP']['Value'],  # Фунт стерлингов
                "JPY": data['Valute']['JPY']['Value'],  # Японская иена
                "CHF": data['Valute']['CHF']['Value'],  # Швейцарский франк
                "TRY": data['Valute']['TRY']['Value'],  # Турецкая лира
                "KZT": data['Valute']['KZT']['Value'],  # Казахстанский тенге
                "BYN": data['Valute']['BYN']['Value'],  # Белорусский рубль
            } 

            print("\n === Курсы валют: === ")
            for code, rate in rates.items():
                print(f"1. {code} = {rate:.2f} RUB")
            print("=" * 30)

        try:
            while True:
                otvet = input("Нужно ли вам перевести рубли в иностранную валюту? (да/нет): ")
                if otvet.lower() in ["да", "lf"]:
                    convert_currency(rates)

                else:
                    print("До свидания!")
                    sys.exit()

        except KeyboardInterrupt:
            print("\nДо свидания!")
            sys.exit()

        except ConnectionError:
            print("Ошибка не удается загрузить страницу, проверьте ваше подключение к интернету.")
    # -------------------------------------------------------------

    # Для перехода в оффлайн режим:
    # ОФФЛАЙН РЕЖИМ: (БЕЗ ИНТЕРНЕТА, примерное значение) ----------------------------
    def offline():
        # примерные курсы
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

        try:
            while True:
                otvet = input("Нужно ли вам перевести рубли в иностранную валюту? (да/нет): ")
                if otvet.lower() in ["да", "lf"]:
                    convert_currency(rates)
                                
                else:
                    print("До свидания!")
                    sys.exit()
                    
        except KeyboardInterrupt:
            print("До свидания!")
            sys.exit()
    # --------------------------------------------------------

    print("\n=== Здравствуйте, переводчик валюты открыт! Выберите режим работы === ")
    print("1. Онлайн, (online) точное значение (С ИНТЕРЕНТОМ)")
    print("2. Оффлайн, (offline) примерое значение (БЕЗ ИНТЕРНЕТА)")
    print("="*50)
    print("Выберите режим (напишите цифру)")
    try:
        while True:
            otvet = int(input("Ввод: "))
            if otvet == 1:
                online()
                sys.exit()
                
            elif otvet == 2:
                offline()
                sys.exit()
                
            else:
                print("Ошибка. Вводите только цифры из списка!")
                continue
    except ValueError:
        print("Пожалуйста, вводите только цифры из списка!")

    except KeyboardInterrupt:
        print("\nУспешный выход, до свидания!")
        sys.exit()

# 2 инструмент
def credit_calculator():
    def admin_panel():

        print("Здравствуйте, вход в админ панель")
        attempt = 0

        while True:
            password = input("Введите пароль: ")

            if password == "**AdM001aQQzs":
                print("Вы вошли в админ панель! Для выхода напишите: 'Exit' ")
                print("\nДоступные опции: ")
                print("1. Статистика использований")
                print("2. Скрытые опции")

                while True:
                    user_input = input("Выберите опцию (вводите цифру): ")

                    if user_input == "1":
                        print("\nСтатистика использований:")
                        print("Всего раз использовано: NA раз")

                    elif user_input == "2":
                        print("Скрытые функции:")

                    elif user_input.lower().strip() in ["exit"]:
                        print("Успешный выход")
                        sys.exit()

                    else:
                        print("Такой опции нет, введите опцию из списка.")

            else:
                attempt += 1
                print(f"Неверный пароль. Осталось попыток: {3 - attempt}")

            if attempt >= 3:
                print("Попытки для входа закончились.")
                sys.exit()

    # ========= ЦВЕТА ========
    RED = '\033[91m' # - Красный
    GREEN = '\033[92m' # - Зеленый
    YELLOW = '\033[93m' # - Желтый
    BLUE = '\033[94m' # - Синий
    PURPLE = '\033[95m' # - Фиолетовый
    CYAN = '\033[96m' # - Голубой
    RESET = '\033[0m' # - Обычный (сброс)
    # ========================

    def get_number(question, min_val, max_val, is_percent=False):
        """Универсальная функция ввода числа с защитой"""
        while True:
            user_input = input(question)

            # Проверка на пустой ввод
            if user_input.strip() == "":
                print(f"Пожалуйста, вводите только цифры!")
                continue

            #Замена запятой на точку
            user_input = user_input.replace(",", ".")

            # Проверка на буквы и символы
            try:
                value = float(user_input)

                # Проверка на отрицательные числа
                if value < 0:
                    print(f"Значение не может быть отрицательным!")
                    continue

                # Проверка на допустимый диапазон
                if value < min_val:
                    print(f"Ваше число слишком маленькое! Минимальное значение: {min_val}.")
                    continue

                if value > max_val:
                    print(f"Ваше число слишком большое! Максимальное значение: {max_val}.")
                    continue
                
                # Для процентов оставляем как есть (может быть дробным)
                if is_percent:
                    return value
                else:
                    return int(value) # рубли - целые числа

            except ValueError:
                print(f"Пожалуйста, вводите только цифры!")

    # ========== ОСНОВНАЯ ПРОГРАММА ==========

    print("\n" + "="*56)
    print(f"Калькулятор кредита открыт.")
    print("="*56)
    print(f"Введите сумму кредита (до 100 млрд рублей).")
    debt = get_number("> ", 1, 1_000_000_000)

    debt_start = debt # ЗАПОМИНАЕМ начальную сумму для расчета переплаты

    # Ввод ставки с защитой от запятой, скрытая админ панель (ШАБЛОН)
    print("Введите годовую ставку по кредиту.")
    user_input = input("> ")

    if user_input.strip().lower() == "admin":
        admin_panel()

    else:
            try:
                annual_rate = float(user_input.replace(",", "."))
                if annual_rate < 1 or annual_rate > 100:
                    print("Ставка должна быть от 1% до 100%!")
                    sys.exit()

                monthly_rate = annual_rate / 100 / 12
            except ValueError:
                print("Вводите только цифры!")
                sys.exit()

    monthly_payment = get_number(f"Введите сумму ежемесячного платежа: ", 1, 100_000_000_000)

    # Минимальный платеж для покрытия процентов
    min_monthly_pay = int(debt * (annual_rate / 100 / 12)) + 1

    if monthly_payment < min_monthly_pay:
        print(f"\nВаш платеж {monthly_payment} руб. Слишком мал! ")
        print(f"Проценты за месяц: {min_monthly_pay - 1} руб.")
        print(f"Вы никога не закроете кредит, если не увеличите платёж.")

    while monthly_payment < min_monthly_pay:
        print(f"Минимальный платёж для погашения кредита: {min_monthly_pay} руб.")
        monthly_payment = get_number(f"Введите новую сумму платежа: ", 1, 100_000_000_000)
        
    month = 0
    max_month = 1200
    debt_temp = debt

    print("\nИдет расчет...\n")

    while debt_temp > 0:
        month += 1

        if month > max_month:
            print("РАСЧЕТ ОТСАНОВЛЕН!")
            print("Слишком маленький платеж! Ипотека будет длится более 100 лет.")
            exit()

        percent = debt_temp * monthly_rate
        debt_temp = debt_temp + percent - monthly_payment
    
        if debt_temp < 0:
            debt_temp = 0
        
        if month % 6 == 0 or debt_temp == 0:
            print(f"Месяц {month}: остаток {round(debt_temp, 2)} руб.")

    # ============ НОВЫЕ ВЫВОДЫ (переплата и итоги) ===========
    year = month // 12
    months = month % 12
    total_paid = monthly_payment * month
    overpayment = total_paid - debt_start

    print("\n" + "="*40)
    print(f"Результат:")
    print(f"Срок погашения: {month} месяцев.")
    print(f"Это {year} лет и {months} месяцев")
    print(f"Всего отдано банку: {total_paid:,.0f} руб.")
    print(f"Переплата банку: {overpayment:,.0f} руб.")
    print("="*40)

    answer = input("\nПоказать таблицу погашения по годам? (да/нет): ")
    if answer.lower().startswith(('Да', 'ДА', 'дА', 'да', 'lf', 'lF', 'LF', 'Lf', 'l', 'L', 'д', 'Д')):
        print("\n| Год  | Остаток долга | Проценты за год |")
        print("|------|---------------|-----------------|")
        
        debt_tab = debt_start
        monthly_rate = annual_rate / 100 / 12

        for year in range(1, 100):
            percent_year = 0
            for months in range(12):
                percent = debt_tab * monthly_rate
                percent_year += percent
                debt_tab = debt_tab + percent - monthly_payment
                if debt_tab < 0:
                    debt_tab = 0
            print(f"| {year:<4} | {round(debt_tab, 2):>13} | {round(percent_year, 2):>14}  |")
            if debt_tab <= 0:
                break


    save = input("\nСохранить результат в файл? (напиши: да/нет): ")
    if save.lower().strip() in ["да", "дА", "ДА", "Да", "lf", "LF", "Lf", "lF", "L", "l", "Д", "д"]:
        from datetime import datetime
        now = datetime.now()
        filename = f"Расчёт_кредита_{now.strftime('%Y%m%d_%H%M%S')}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Дата: {now.strftime('%Y-%m-%d %H:%M')}\n")
            f.write(f"Сумма долга: {debt_start:,.0f} руб.\n")
            f.write(f"Годовая ставка: {annual_rate:.1f} %\n")
            f.write(f"Ежемесячный платёж: {monthly_payment:,.0f} руб.\n")
            f.write(f"Срок погашения: {month} месяцев\n")
            f.write(f"Срок погашения: {year} Лет и {months} Месяцев\n")
            f.write(f"Переплата: {overpayment:,.0f} руб.\n")

            # НОВОВВЕДЕНИЕ ТАБЛИЦА ПО ГОДАМ:
            f.write("\n" + "="*42 + "\n")
            f.write("ТАБЛИЦА ПОГАШЕНИЯ ПО ГОДАМ:")
            f.write("\n" + "="*42 + "\n")
            f.write("| Год  | Остаток долга | Проценты за год |\n")
            f.write("|------|---------------|-----------------|\n")

            # РАСЧЕТ ТАБЛИЦЫ:
            debt_tab = debt_start
            monthly_rate = annual_rate / 100 / 12

            for year in range(1, 100):
                percent_year = 0
                for months in range(12):
                    percent = debt_tab * monthly_rate
                    percent_year += percent
                    debt_tab = debt_tab + percent - monthly_payment
                    if debt_tab < 0:
                        debt_tab = 0
                f.write(f"| {year:<4} | {round(debt_tab, 2):>13} | {round(percent_year, 2):>14}  |\n")
                if debt_tab <= 0:
                    break

        print("\n")    
        print(f"{YELLOW}Отчёт сохранен в файл: {filename}")
        
    else:
            print("\n")
            print(f"До свидания!")

print("\n === FinPROga_V1.1.0 === ")
print("Здравствуйте! Выберите инструмент из списка.")
print("\n=== МЕНЮ ===")
print("1. Конвертор валюты")
print("2. Калькулятор кредитов")
print("="*40)
try:
    while True:
        user_input = int(input("Ввод: "))
        if user_input == 1:
            currency_statistics()
            sys.exit()
        elif user_input == 2:
            credit_calculator()
            sys.exit()
        else:
            print("Вводите число из списка!")
except ValueError:
    print("Вводите только числа!")
except KeyboardInterrupt:
    print("\nУспешный выход, до свидания!")
    sys.exit()