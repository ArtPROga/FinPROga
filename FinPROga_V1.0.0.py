#1 инструмент
import sys
def MoneyStats(): 
    def online():
        # ОНЛАЙН РЕЖИМ: (С ИНТЕРНЕТОМ, точное значение) --------------------------------------
        import requests
        import sys
        response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")

        if response.status_code == 200:
            data = response.json()

            usd_rate = data['Valute']['USD']['Value']  # Доллар
            eur_rate = data['Valute']['EUR']['Value']  # Евро
            cny_rate = data['Valute']['CNY']['Value']  # Юань
            gbp_rate = data['Valute']['GBP']['Value']  # Фунт стерлингов
            jpy_rate = data['Valute']['JPY']['Value']  # Японская иена
            chf_rate = data['Valute']['CHF']['Value']  # Швейцарский франк
            try_rate = data['Valute']['TRY']['Value']  # Турецкая лира
            kzt_rate = data['Valute']['KZT']['Value']  # Казахстанский тенге
            byn_rate = data['Valute']['BYN']['Value']  # Белорусский рубль

            print("\n === Курсы валют: === ")
            print(f"\nДоллар к Рублю на сегодня: 1 USD = {usd_rate:.2f} RUB")
            print(f"Евро к Рублю на сегодня: 1 EUR = {eur_rate:.2f} RUB")
            print(f"Юань к Рублю на сегодня: 1 CNY = {cny_rate:.2f} RUB")
            print(f"Фунт стерлингов к Рублю на сегодня: 1 GBP = {gbp_rate:.2f} RUB")
            print(f"Японская иена к Рублю на сегодня: 1 JPY = {jpy_rate:.2f} RUB")
            print(f"Швейцарский фрак к Рублю на сегодня: 1 CHF = {chf_rate:.2f} RUB")
            print(f"Турецкая лира к Рублю на сегодня: 1 TRY = {try_rate:.2f} RUB")
            print(f"Казахстанский тенге к Рублю на сегодня: 1 KZT = {kzt_rate:.2f} RUB")
            print(f"Белорусский рубль к Рублю на сегодня: 1 BYN = {byn_rate:.2f} RUB")
            print(f"\n==============================")

        try:
            while True:
                otvet = input("Нужно ли вам перевести рубли в иностранную валюту? (да/нет): ")
                if otvet.lower() in ["да", "lf"]:
                    while True:
                        print("\n === Выберите в какую валюту перевести рубль: === ")
                        print("1. USD (Доллар США)" + "\n2. EUR (ЕВРО)" + "\n3. CNY (Юань)" + "\n4. GBP (Фунт стерлингов)" + "\n5. JPY (Японская иена)" + "\n6. CHF (Швейцарский фрак)" + "\n7. TRY (Турецкая лира)" + "\n8. KZT (Казахстанский тенге)" + "\n9. BYN (Белорусский рубль)")
                        print(" ================ ")

                        print("\nВыберите валюту. (введите цифру)")
                        money = int(input("Ввод: "))
                        if money == 1:
                            rub = float(input("Введите сумму в рублях: "))
                            usd = rub / usd_rate
                            print(f"{rub} РУБЛЕЙ = {usd:.2f} USD")
                            otv = input("Нужно рассчитать еще? (да/нет): ")
                            if otv.lower() in ["да"]:
                                continue
                            else:
                                print("До свидания!")
                                sys.exit()
                                exit()
                        elif money == 2:
                            rub = float(input("Введите сумму в рублях: "))
                            eur = rub / eur_rate
                            print(f"{rub} РУБЛЕЙ = {eur:.2f} EUR")
                            otv = input("Нужно рассчитать еще? (да/нет): ")
                            if otv.lower() in ["да"]:
                                continue
                            else:
                                print("До свидания!")
                                sys.exit()
                                exit()
                        elif money == 3:
                            rub = float(input("Введите сумму в рублях: "))
                            cny = rub / cny_rate
                            print(f"{rub} РУБЛЕЙ = {cny:.2f} CNY")
                            otv = input("Нужно рассчитать еще? (да/нет): ")
                            if otv.lower() in ["да"]:
                                continue
                            else:
                                print("До свидания!")
                                sys.exit()
                                exit()
                        elif money == 4:
                            rub = float(input("Введите сумму в рублях: "))
                            gbp = rub / gbp_rate
                            print(f"{rub} РУБЛЕЙ = {gbp:.2f} GBP")
                            otv = input("Нужно рассчитать еще? (да/нет): ")
                            if otv.lower() in ["да"]:
                                continue
                            else:
                                print("До свидания!")
                                sys.exit()
                                exit()
                        elif money == 5:
                            rub = float(input("Введите сумму в рублях: "))
                            jpy = rub / jpy_rate
                            print(f"{rub} РУБЛЕЙ = {jpy:.2f} JPY")
                            otv = input("Нужно рассчитать еще? (да/нет): ")
                            if otv.lower() in ["да"]:
                                continue
                            else:
                                print("До свидания!")
                                sys.exit()
                                exit()
                        elif money == 6:
                            rub = float(input("Введите сумму в рублях: "))
                            chf = rub / chf_rate
                            print(f"{rub} РУБЛЕЙ = {chf:.2f} CHF")
                            otv = input("Нужно рассчитать еще? (да/нет): ")
                            if otv.lower() in ["да"]:
                                continue
                            else:
                                print("До свидания!")
                                sys.exit()
                                exit()
                        elif money == 7:
                            rub = float(input("Введите сумму в рублях: "))
                            tryy = rub / try_rate
                            print(f"{rub} РУБЛЕЙ = {tryy:.2f} TRY")
                            otv = input("Нужно рассчитать еще? (да/нет): ")
                            if otv.lower() in ["да"]:
                                continue
                            else:
                                print("До свидания!")
                                sys.exit()
                                exit()
                        elif money == 8:
                            rub = float(input("Введите сумму в рублях: "))
                            kzt = rub / gbp_rate
                            print(f"{rub} РУБЛЕЙ = {kzt:.2f} KZT")
                            otv = input("Нужно рассчитать еще? (да/нет): ")
                            if otv.lower() in ["да"]:
                                continue
                            else:
                                print("До свидания!")
                                sys.exit()
                                exit()
                        elif money == 9:
                            rub = float(input("Введите сумму в рублях: "))
                            byn = rub / byn_rate
                            print(f"{rub} РУБЛЕЙ = {byn:.2f} BYN")
                            otv = input("Нужно рассчитать еще? (да/нет): ")
                            if otv.lower() in ["да"]:
                                continue
                            else:
                                print("До свидания!")
                                sys.exit()
                                exit()
                    else:
                        print("До свидания!")
                        sys.exit()
                        exit()
                else:
                    print("До свидания!")
                    sys.exit()
                    exit()
        except KeyboardInterrupt:
            print("До свидания!")
            sys.exit()
            exit()

        except ValueError:
            print("Пожалуйста, вводите только числа!")

        except ConnectionError:
            print("Ошибка не удается загрузить страницу, проверьте ваше подключение к интернету.")
    # -------------------------------------------------------------

    # Для перехода в оффлайн режим:
    # ОФФЛАЙН РЕЖИМ: (БЕЗ ИНТЕРНЕТА, примерное значение) ----------------------------
    def offline():
        # (примерные курсы на лето 2026)
        usd_rate = 77
        eur_rate = 90
        cny_rate = 11
        gbp_rate = 100
        jpy_rate = 48
        chf_rate = 95
        try_rate = 15
        kzt_rate = 15
        byn_rate = 26

        print(f" === Курсы валют: === ")
        print(f"Доллар к Рублю (примерный курс): 1 USD = {usd_rate} RUB")
        print(f"Евро к Рублю (примерный курс): 1 EUR = {eur_rate} RUB")
        print(f"Юань к Рублю (примерный курс): 1 CNY = {cny_rate} RUB")
        print(f"Фунт стерлингов к Рублю (примерный курс): 1 GBP = {gbp_rate} RUB")
        print(f"Японская иена к Рублю (примерный курс): 1 JPY = {jpy_rate} RUB")
        print(f"Швейцарский фрак к Рублю (примерный курс): 1 CHF = {chf_rate} RUB")
        print(f"Турецкая лира к Рублю (примерный курс): 1 TRY = {try_rate} RUB")
        print(f"Казахстанский тенге к Рублю (примерный курс): 1 KZT = {kzt_rate} RUB")
        print(f"Белорусский рубль к Рублю (примерный курс): 1 BYN = {byn_rate} RUB")
        print(f"========================\n")
        try:
            while True:
                otvet = input("Нужно ли вам перевести рубли в иностранную валюту? (да/нет): ")
                if otvet.lower() in ["да", "lf"]:
                    while True:
                        print("\n === Выберите в какую валюту перевести рубль: === ")
                        print("1. USD (Доллар США)" + "\n2. EUR (ЕВРО)" + "\n3. CNY (Юань)" + "\n4. GBP (Фунт стерлингов)" + "\n5. JPY (Японская иена)" + "\n6. CHF (Швейцарский фрак)" + "\n7. TRY (Турецкая лира)" + "\n8. KZT (Казахстанский тенге)" + "\n9. BYN (Белорусский рубль)")
                        print(" ================ ")

                        print("\nВыберите валюту. (введите цифру)")
                        money = int(input("Ввод: "))
                        if money == 1:
                            rub = float(input("Введите сумму в рублях: "))
                            usd = rub / usd_rate
                            print(f"{rub} РУБЛЕЙ = {usd:.2f} USD")
                            otv = input("Нужно рассчитать еще? (да/нет): ")
                            if otv.lower() in ["да"]:
                                continue
                            else:
                                print("До свидания!")
                                sys.exit()
                                exit()
                        elif money == 2:
                            rub = float(input("Введите сумму в рублях: "))
                            eur = rub / eur_rate
                            print(f"{rub} РУБЛЕЙ = {eur:.2f} EUR")
                            otv = input("Нужно рассчитать еще? (да/нет): ")
                            if otv.lower() in ["да"]:
                                continue
                            else:
                                print("До свидания!")
                                sys.exit()
                                exit()
                        elif money == 3:
                            rub = float(input("Введите сумму в рублях: "))
                            cny = rub / cny_rate
                            print(f"{rub} РУБЛЕЙ = {cny:.2f} CNY")
                            otv = input("Нужно рассчитать еще? (да/нет): ")
                            if otv.lower() in ["да"]:
                                continue
                            else:
                                print("До свидания!")
                                sys.exit()
                                exit()
                        elif money == 4:
                            rub = float(input("Введите сумму в рублях: "))
                            gbp = rub / gbp_rate
                            print(f"{rub} РУБЛЕЙ = {gbp:.2f} GBP")
                            otv = input("Нужно рассчитать еще? (да/нет): ")
                            if otv.lower() in ["да"]:
                                continue
                            else:
                                print("До свидания!")
                                sys.exit()
                                exit()
                        elif money == 5:
                            rub = float(input("Введите сумму в рублях: "))
                            jpy = rub / jpy_rate
                            print(f"{rub} РУБЛЕЙ = {jpy:.2f} JPY")
                            otv = input("Нужно рассчитать еще? (да/нет): ")
                            if otv.lower() in ["да"]:
                                continue
                            else:
                                print("До свидания!")
                                sys.exit()
                                exit()
                        elif money == 6:
                            rub = float(input("Введите сумму в рублях: "))
                            chf = rub / chf_rate
                            print(f"{rub} РУБЛЕЙ = {chf:.2f} CHF")
                            otv = input("Нужно рассчитать еще? (да/нет): ")
                            if otv.lower() in ["да"]:
                                continue
                            else:
                                print("До свидания!")
                                sys.exit()
                                exit()
                        elif money == 7:
                            rub = float(input("Введите сумму в рублях: "))
                            tryy = rub / try_rate
                            print(f"{rub} РУБЛЕЙ = {tryy:.2f} TRY")
                            otv = input("Нужно рассчитать еще? (да/нет): ")
                            if otv.lower() in ["да"]:
                                continue
                            else:
                                print("До свидания!")
                                sys.exit()
                                exit()
                        elif money == 8:
                            rub = float(input("Введите сумму в рублях: "))
                            kzt = rub / gbp_rate
                            print(f"{rub} РУБЛЕЙ = {kzt:.2f} KZT")
                            otv = input("Нужно рассчитать еще? (да/нет): ")
                            if otv.lower() in ["да"]:
                                continue
                            else:
                                print("До свидания!")
                                sys.exit()
                                exit()
                        elif money == 9:
                            rub = float(input("Введите сумму в рублях: "))
                            byn = rub / byn_rate
                            print(f"{rub} РУБЛЕЙ = {byn:.2f} BYN")
                            otv = input("Нужно рассчитать еще? (да/нет): ")
                            if otv.lower() in ["да"]:
                                continue
                            else:
                                print("До свидания!")
                                sys.exit()
                                exit()
                    else:
                        print("До свидания!")
                        sys.exit()
                        exit()
                else:
                    print("До свидания!")
                    sys.exit()
                    exit()
        except KeyboardInterrupt:
            print("До свидания!")
            sys.exit()
            exit()

        except ValueError:
            print("Пожалуйста, вводите только числа!")
    # --------------------------------------------------------

    import sys

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
                exit()
            elif otvet == 2:
                offline()
                sys.exit()
                exit()
            else:
                print("Ошибка. Вводите только цифры из списка!")
                continue
    except ValueError:
        print("Пожалуйста, вводите только цифры из списка!")

    except KeyboardInterrupt:
        print("Успешный выход, до свидания!")
        sys.exit()
        exit()


# 2 инструмент0
import sys
def Bankomatik():
    import sys
    def admin_panel():
        print("Здравствуйте, вход в админ панель")
        att = 0
        while True:
            password = input("Введите пароль: ")
            if password == "**AdM001aQQzs":
                print("Вы вошли в админ панель! Для выхода напишите EXIT")
                print("\nДоступные опции: ")
                print("1. Статистика банкоматика")
                print("2. Скрытые опции")
                while True:
                    otv = input("Выберите опцию (вводите цифру): ")
                    if otv == "1":
                        print("\nСтатистика банкоматика:")
                        print("Всего раз использовано: NA раз")
                    elif otv == "2":
                        print("Скрытые функции:")
                        print("HACK")
                    elif otv.lower().strip() in ["exit"]:
                        print("Успешный выход")
                        sys.exit()
                    else:
                        print("Неизвестная команда, попробуйте снова.")
            else:
                att += 1
                print(f"Неверный пароль. Осталось попыток: {3 - att}")

            if att >= 3:
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

    # БАНКОМАТИК v1.4 (с полной защитой)

    def get_number(question, min_val, max_val, is_percent=False):
        """Универсальная функция ввода числа с защитой"""
        while True:
            vvod = input(question)

            # Проверка на пустой ввод
            if vvod.strip() == "":
                print(f" ({RED}!!!{RESET}) {YELLOW}Пожалуйста{RESET}, введите {RED}ЧИСЛО{RESET}, а не буквы, символы, пробел и т.д.")
                continue

            #Замена запятой на точку
            vvod = vvod.replace(",", ".")

            # Проверка на буквы и символы
            try:
                chislo = float(vvod)

                # Проверка на отрицательные числа
                if chislo < 0:
                    print(f"{RED}Значение не может быть отрицательным{RESET}!")
                    continue

                # Проверка на допустимый диапазон
                if chislo < min_val:
                    print(f"{RED}Слишком мало{RESET}! {RED}Минимум{RESET}: {min_val}.")
                    continue

                if chislo > max_val:
                    print(f"{RED}Слишком много{RESET}! Максимум{RESET}: {max_val}.")
                    continue
                
                # Для процентов оставляем как есть (может быть дробным)
                if is_percent:
                    return chislo
                else:
                    return int(chislo) # рубли - целые числа

            except ValueError:
                print(f" ({RED}!!!{RESET}) {YELLOW}Пожалуйста{RESET}, введите {RED}ЧИСЛО{RESET}, а не буквы, символы, пробел и т.д.")

    # ========== ОСНОВНАЯ ПРОГРАММА ==========
    import sys
    print("\n"*3 + "="*56)
    print(f"*{CYAN}Вас приветствует калькулятор кредита{RESET}!* {GREEN}БАНКОМАТИК{RESET} v1.4")
    print("by: Artem Protasov")
    print("="*56)
    print(f"{PURPLE}Пожалуйста{RESET},{PURPLE} введите сумму вашего кредита{RESET}! ")
    
    dolg = get_number(f"({YELLOW}до 1 млрд рублей{RESET}): ", 1, 1_000_000_000)

    dolg_start = dolg # ЗАПОМИНАЕМ начальную сумму для расчета переплаты

    # Ввод ставки с защитой от запятой
    user_input = input(f"{BLUE}Какая годовая ставка{RESET}? (в %): ")

    if user_input.strip().lower() == "adm":
        admin_panel()
    else:
            try:
                stavka = float(user_input.replace(",", "."))
                if stavka < 1 or stavka > 100:
                    print("Ставка должна быть от 1% до 100%!")
                    exit()
                stavka_mesyac = stavka / 100 / 12
            except ValueError:
                print("Ошибка: Введите число.")
                exit()


    print(f"{GREEN}Спасибо{RESET}!")

    platezh = get_number(f"{YELLOW}А сколько денег вы платите в месяц{RESET}? (Руб): ", 1, 100_000_000)

    # ===== НОВАЯ ПРОВЕРКА =====
    # Минимальный платеж для покрытия процентов
    min_platezh = int(dolg * (stavka / 100 / 12)) + 1

    if platezh < min_platezh:
        print(f"\n({RED}!!!{RESET}){YELLOW} ВНИМАНИЕ {RESET}({RED}!!!{RESET}) Ваш платеж {platezh} руб {RED}СЛИШКОМ МАЛ{RESET}! ")
        print(f"{YELLOW}Проценты за месяц уже составляют{RESET}: {min_platezh - 1} руб.")
        print(f"Долг {RED}НИКОГДА НЕ ЗАКРОЕТСЯ{RESET} а будет только расти.")
    while platezh < min_platezh:
        print(f"{YELLOW}Чтобы погасить кредит{RESET},{YELLOW} платеж должен быть {RED}МИНИМУМ{RESET}: {min_platezh} руб.")
        platezh = get_number(f"{GREEN}Введите новую сумму платежа{RESET}: ", 1, 1_000_000_000)
    # ====================================================
        
    mesyac = 0
    max_mesyacev = 1200
    dolg_temp = dolg

    print("\nИдет расчет...\n")

    while dolg_temp > 0:
        mesyac += 1

        if mesyac > max_mesyacev:
            print("РАСЧЕТ ОТСАНОВЛЕН!")
            print("Слишком маленький платеж! Ипотека будет длится более 100 лет.")
            exit()

        procenty = dolg_temp * stavka_mesyac
        dolg_temp = dolg_temp + procenty - platezh
    
        if dolg_temp < 0:
            dolg_temp = 0
        
        if mesyac % 6 == 0 or dolg_temp == 0:
            print(f"Месяц {mesyac}: остаток {round(dolg_temp, 2)} руб.")

    # ============ НОВЫЕ ВЫВОДЫ (переплата и итоги) ===========
    let = mesyac // 12
    mes = mesyac % 12
    vsego_otdano = platezh * mesyac
    pereplata = vsego_otdano - dolg_start

    print("\n" + "="*40)
    print(f"{GREEN}РЕЗУЛЬТАТЫ{RESET}:")
    print(f"Срок погашения: {RED}{mesyac} {RESET}месяцев.")
    print(f"Это {RED}{let}{RESET} лет и {RED}{mes} {RESET}месяцев")
    print(f"Всего отдано банку{RESET}: {RED}{vsego_otdano:,.0f}{RESET} руб{RESET}.")
    print(f"{RED}(!){RESET} Переплата банку{RESET}: {RED}{pereplata:,.0f} {RESET}руб.")
    print("="*40)

    otvet = input("\nПоказать таблицу погашения по годам? (да/нет): ")
    if otvet.lower().startswith(('Да', 'ДА', 'дА', 'да', 'lf', 'lF', 'LF', 'Lf', 'l', 'L', 'д', 'Д')):
        print("\n| Год  | Остаток долга | Проценты за год |")
        print("|------|---------------|-----------------|")
        
        dolg_tab = dolg_start
        stavka_mesyac = stavka / 100 / 12

        for god in range(1, 100):
            procenty_god = 0
            for mes in range(12):
                procenty = dolg_tab * stavka_mesyac
                procenty_god += procenty
                dolg_tab = dolg_tab + procenty - platezh
                if dolg_tab < 0:
                    dolg_tab = 0
            print(f"| {god:<4} | {round(dolg_tab, 2):>13} | {round(procenty_god, 2):>14}  |")
            if dolg_tab <= 0:
                break


    sohranit = input("\nСохранить результат в файл? (напиши: да/нет): ")
    if sohranit.lower().strip() in ["да", "дА", "ДА", "Да", "lf", "LF", "Lf", "lF", "L", "l", "Д", "д"]:
        from datetime import datetime
        now = datetime.now()
        filename = f"BANKOMATIK_{now.strftime('%Y%m%d_%H%M%S')}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Дата: {now.strftime('%Y-%m-%d %H:%M')}\n")
            f.write(f"Сумма долга: {dolg_start:,.0f} руб.\n")
            f.write(f"Годовая ставка: {stavka:.1f} %\n")
            f.write(f"Ежемесячный платёж: {platezh:,.0f} руб.\n")
            f.write(f"Срок погашения: {mesyac} месяцев\n")
            f.write(f"Срок погашения: {let} Лет и {mes} Месяцев\n")
            f.write(f"Переплата: {pereplata:,.0f} руб.\n")

            # НОВОВВЕДЕНИЕ ТАБЛИЦА ПО ГОДАМ:
            f.write("\n" + "="*42 + "\n")
            f.write("ТАБЛИЦА ПОГАШЕНИЯ ПО ГОДАМ:")
            f.write("\n" + "="*42 + "\n")
            f.write("| Год  | Остаток долга | Проценты за год |\n")
            f.write("|------|---------------|-----------------|\n")

            # РАСЧЕТ ТАБЛИЦЫ:
            dolg_tab = dolg_start
            stavka_mesyac = stavka / 100 / 12

            for god in range(1, 100):
                procenty_god = 0
                for mes in range(12):
                    procenty = dolg_tab * stavka_mesyac
                    procenty_god += procenty
                    dolg_tab = dolg_tab + procenty - platezh
                    if dolg_tab < 0:
                        dolg_tab = 0
                f.write(f"| {god:<4} | {round(dolg_tab, 2):>13} | {round(procenty_god, 2):>14}  |\n")
                if dolg_tab <= 0:
                    break

        print("\n")    
        print("="*53)
        print(f"{YELLOW}Отчёт сохранен в файл{RESET}: {filename}")
        print(f"{GREEN}До свидания{RESET}!{GREEN} С вами был ваш{BLUE} БАНКОМАТИК{RESET}! :) ")
        print("="*53)
        print("\n")
        

    else:
            print("\n")
            print("="*50)
            print(f"{GREEN}Хорошо{RESET}, {GREEN}До свидания{RESET}!{GREEN} С вами был ваш{BLUE} БАНКОМАТИК{RESET}! :) ")
            print("="*50)
            print("\n")



print("\n === FinPROga_V1.0.0 === ")
print("Здравствуйте, Финансовая программа запущена! Выберите инструмент из списка.")
print("\n=== МЕНЮ ===")
print("1. Переводчик валюты")
print("2. Калькулятор ипотеки/кредита")
print("="*40)
try:
    while True:
        print("Введите цифру нужного инструмента.")
        otvet = int(input("Ввод: "))
        if otvet == 1:
            MoneyStats()
            sys.exit()
            exit()
        elif otvet == 2:
            Bankomatik()
            sys.exit()
            exit()
        else:
            print("Ошибка. Выберите число из списка!")
except ValueError:
    print("Ошибка. Вводите только числа!")
except KeyboardInterrupt:
    print("Успешный выход. До свидания!")
    sys.exit()
    exit()