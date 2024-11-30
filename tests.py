# flake8: noqa
# pylint: disable=broad-exception-raised, raise-missing-from, too-many-arguments, redefined-outer-name
# pylance: disable=reportMissingImports, reportMissingModuleSource, reportGeneralTypeIssues
# type: ignore

import unittest
from currency_parser import CurrencyParser

class TestCurrencyParser(CurrencyParser):
    def process_currencies(self, currencies):
        return currencies

class TestCurrencyParsing(unittest.TestCase):
    def setUp(self):
        self.parser = TestCurrencyParser()

    def test_all_cases(self):
        def test(text, expected):
            result = self.parser.find_currencies(text)
            print(f'Test "{text}" -> {result} (expected {expected}), {"Pass" if result == expected else "Fail"}')
            self.assertEqual(result, expected)

        test("100 драм", [(100.0, "AMD", "100 драм")])
        test("200 драма", [(200.0, "AMD", "200 драма")])
        test("300 драмов", [(300.0, "AMD", "300 драмов")])
        
        test("100 шекелей", [(100.0, "ILS", "100 шекелей")])
        test("200 шекель", [(200.0, "ILS", "200 шекель")])
        test("300 шекеля", [(300.0, "ILS", "300 шекеля")])
        test("400 шек", [(400.0, "ILS", "400 шек")])
        test("500 шах", [(500.0, "ILS", "500 шах")])
        test("600 ils", [(600.0, "ILS", "600 ils")])
        test("700₪", [(700.0, "ILS", "700₪")])
        test("700 ₪", [(700.0, "ILS", "700 ₪")])
        
        test("100 фунтов", [(100.0, "GBP", "100 фунтов")])
        test("200 фунт", [(200.0, "GBP", "200 фунт")])
        test("300 фунтов", [(300.0, "GBP", "300 фунтов")])
        test("400 паунд", [(400.0, "GBP", "400 паунд")])
        test("500 pound", [(500.0, "GBP", "500 pound")])
        test("600 gbp", [(600.0, "GBP", "600 gbp")])
        test("700£", [(700.0, "GBP", "700£")])
        test("£800", [(800.0, "GBP", "£800")])
        test("700 £", [(700.0, "GBP", "700 £")])
        test("£ 800", []) 
        test("1.2.3 доллара", [(2.3, 'USD', '2.3 доллара')]) 
        test("2 песо", [])
        test("77 тугриков", [])
        test("7666777 kwd", [])
        test("100500 CAD вышло", [])
        test("два с половиной бакса", [])
        test("пять баксов", [])
        test("three hundred bucks", [])
        
        test("100 рублей", [(100.0, "RUB", "100 рублей")])
        test("200 рубль", [(200.0, "RUB", "200 рубль")])
        test("300 рубля", [(300.0, "RUB", "300 рубля")])
        test("400 rub", [(400.0, "RUB", "400 rub")])
        test("500₽", [(500.0, "RUB", "500₽")])
        test("500 ₽", [(500.0, "RUB", "500 ₽")])
        test("500\₽", [])
        test("\500", [])
        test("500'₽", [])
        test("500,₽", [])
        test("500.₽", [])
        test("500;₽", [])
        test("500:₽", [])
        test("500₽$", [(500.0, "RUB", "500₽")])
        test("500$$", [(500.0, 'USD', '500$')])

        test("200 доллар", [(200.0, "USD", "200 доллар")])
        test("200 Доллар", [(200.0, "USD", "200 Доллар")])
        test("200 ДоллаР", [(200.0, "USD", "200 ДоллаР")])
        test("200 доЛлаРов", [(200.0, "USD", "200 доЛлаРов")])

        test("300 доллара", [(300.0, "USD", "300 доллара")])
        test("400 баксов", [(400.0, "USD", "400 баксов")])
        test("500 бакс", [(500.0, "USD", "500 бакс")])
        test("600 usd", [(600.0, "USD", "600 usd")])
        test("700$", [(700.0, "USD", "700$")])
        test("$800", [(800.0, "USD", "$800")])
        
        test("100 евро", [(100.0, "EUR", "100 евро")])
        test("200 eur", [(200.0, "EUR", "200 eur")])
        test("300€", [(300.0, "EUR", "300€")])
        test("€400", [(400.0, "EUR", "€400")])
        
        test("100 йен", [(100.0, "JPY", "100 йен")])
        test("200 йена", [(200.0, "JPY", "200 йена")])
        test("300 йен", [(300.0, "JPY", "300 йен")])
        test("400 jpy", [(400.0, "JPY", "400 jpy")])
        test("500¥", [(500.0, "JPY", "500¥")])
        
        test("100 юаней", [(100.0, "CNY", "100 юаней")])
        test("200 юань", [(200.0, "CNY", "200 юань")])
        test("300 юаня", [(300.0, "CNY", "300 юаня")])
        test("400 cny", [(400.0, "CNY", "400 cny")])
        
        test("100 лари", [(100.0, "GEL", "100 лари")])
        test("200 gel", [(200.0, "GEL", "200 gel")])
        
        test("100 динаров", [(100.0, "JOD", "100 динаров")])
        test("200 динар", [(200.0, "JOD", "200 динар")])
        test("300 динаров", [(300.0, "JOD", "300 динаров")])
        test("400 jod", [(400.0, "JOD", "400 jod")])
        
        test("100 батов", [(100.0, "THB", "100 батов")])
        test("200 бат", [(200.0, "THB", "200 бат")])
        test("300 бата", [(300.0, "THB", "300 бата")])
        test("400 thb", [(400.0, "THB", "400 thb")])
        
        test("100 тенге", [(100.0, "KZT", "100 тенге")])
        test("200 тг", [(200.0, "KZT", "200 тг")])
        test("300 kzt", [(300.0, "KZT", "300 kzt")])
        
        test("1.5 рублей", [(1.5, "RUB", "1.5 рублей")])
        test("2,5 евро", [(2.5, "EUR", "2,5 евро")])
        test("$3.14", [(3.14, "USD", "$3.14")])
        test("10.50₽", [(10.50, "RUB", "10.50₽")])
        test("100 рублей", [(100.0, "RUB", "100 рублей")])
        test("$200", [(200.0, "USD", "$200")])
        test("300 EUR", [(300.0, "EUR", "300 EUR")])
        test("400₽", [(400.0, "RUB", "400₽")])
        test("500 баксов", [(500.0, "USD", "500 баксов")])
        test("600 долларов", [(600.0, "USD", "600 долларов")])
        test("1к рублей", [(1000.0, "RUB", "1к рублей")])
        test("1к долларов", [(1000.0, "USD", "1к долларов")])
        test("1к евро", [(1000.0, "EUR", "1к евро")])
        test("1к йен", [(1000.0, "JPY", "1к йен")])
        test("1к юаней", [(1000.0, "CNY", "1к юаней")])
        test("1к лари", [(1000.0, "GEL", "1к лари")])
        test("1к динаров", [(1000.0, "JOD", "1к динаров")])
        test("1к батов", [(1000.0, "THB", "1к батов")])
        test("1к тенге", [(1000.0, "KZT", "1к тенге")])
        test("1к тенгег", [])
        test("1к батова", [])


        test("2к баксов", [(2000.0, "USD", "2к баксов")])
        test("1.5к EUR", [(1500.0, "EUR", "1.5к EUR")])
        test("0.5к долларов", [(500.0, "USD", "0.5к долларов")])
        test("1к$", [(1000.0, "USD", "1к$")])
        test("2к₽", [(2000.0, "RUB", "2к₽")])
        test("1.5к€", [(1500.0, "EUR", "1.5к€")])
        test("1к$ и 2к₽", [(1000.0, "USD", "1к$"), (2000.0, "RUB", "2к₽")])
        test("перевел 1к$ получил 2к₽", [(1000.0, "USD", "1к$"), (2000.0, "RUB", "2к₽")])
        test("отдал е��у 1.5к€", [(1500.0, "EUR", "1.5к€")])
        test("Купил за 100 баксов и 200 рублей", [(100.0, "USD", "100 баксов"), (200.0, "RUB", "200 рублей")])
        test("Перевел 1к$ и 2к₽", [(1000.0, "USD", "1к$"), (2000.0, "RUB", "2к₽")])
        test("€100 и 200₽ и $300", [(100.0, "EUR", "€100"), (200.0, "RUB", "200₽"), (300.0, "USD", "$300")])
        test("Привет, как дела?", [])
        test("123", [])
        test("просто текст", [])
        test("k рублей", [])
        test("kрублей", [])
        test("k долларов", [])  
        test("k евро", [])
        test("k йен", [])
        test("k юаней", [])
        test("k лари", [])
        test("k динаров", [])
        test("k батов", [])
        test("k тенге", [])
        test("k$", [])
        test("k€", [])
        test("k₽", [])
        test("$k", [])
        test("€k", [])
        test("из долларов он получил 0. рублей тоже не получил", [])
        test("он получил5 рублей, и долларов тоже", [(5, 'RUB', "5 рублей")])

        test("он получил 0.5 рублей, и долларов тоже", [(0.5, 'RUB', "0.5 рублей")])
        test("он получил .5 рублей, и долларов тоже", [(5, 'RUB', "5 рублей")]) #???!!
        test("3 412 928 ₪", [(3412928.0, 'ILS', "3 412 928 ₪")])
        test("3 412  928 ₪", [(928.0, 'ILS', '928 ₪')])
        test("3 412н 928 ₪", [(928.0, 'ILS', '928 ₪')])
        test("3 412 н928 ₪", [(928.0, 'ILS', '928 ₪')])


        
        test("13675 ₽", [(13675.0, 'RUB', "13675 ₽")])
        test("13675₽", [(13675.0, 'RUB', "13675₽")])

        test("462 ₪", [(462.0, "ILS", "462 ₪")])
        test("462₪", [(462.0, "ILS", "462₪")])

        test("127 $", [(127.0, "USD", "127 $")])
        test("127$", [(127.0, "USD", "127$")])

        test("120 €", [(120.0, "EUR", "120 €")])
        test("120€", [(120.0, "EUR", "120€")])

        test("888 ₽", [(888.0, "RUB", "888 ₽")])
        test("888₽", [(888.0, "RUB", "888₽")])

        test("8.2 $", [(8.2, "USD", "8.2 $")])
        test("8.2$", [(8.2, "USD", "8.2$")])

        test("6.5 £", [(6.5, "GBP", "6.5 £")])
        test("6.5£", [(6.5, "GBP", "6.5£")])

        test("7.8 €", [(7.8, "EUR", "7.8 €")])
        test("7.8€", [(7.8, "EUR", "7.8€")])

        test("38 $", [(38.0, "USD", "38 $")])
        test("38$", [(38.0, "USD", "38$")])

        test("36 €", [(36.0, "EUR", "36 €")])
        test("36€", [(36.0, "EUR", "36€")])

        test("1.4 ₪", [(1.4, "ILS", "1.4 ₪")])
        test("1.4₪", [(1.4, "ILS", "1.4₪")])

        test("0.4 $", [(0.4, "USD", "0.4 $")])
        test("0.4$", [(0.4, "USD", "0.4$")])

        test("0.3 £", [(0.3, "GBP", "0.3 £")])
        test("0.3£", [(0.3, "GBP", "0.3£")])

        test("0.4 €", [(0.4, "EUR", "0.4 €")])
        test("0.4€", [(0.4, "EUR", "0.4€")])

        test("6838 ₽", [(6838.0, "RUB", "6838 ₽")])
        test("6838₽", [(6838.0, "RUB", "6838₽")])

        test("231 ₪", [(231.0, "ILS", "231 ₪")])
        test("231₪", [(231.0, "ILS", "231₪")])

        test("63 $", [(63.0, "USD", "63 $")])
        test("63$", [(63.0, "USD", "63$")])

        test("60 €", [(60.0, "EUR", "60 €")])
        test("60€", [(60.0, "EUR", "60€")])

        test("26 ₽", [(26.0, "RUB", "26 ₽")])
        test("26₽", [(26.0, "RUB", "26₽")])    

        test("0.9 ₪", [(0.9, "ILS", "0.9 ₪")])
        test("0.9₪", [(0.9, "ILS", "0.9₪")])

        test("0.3 $", [(0.3, "USD", "0.3 $")])
        test("0.3$", [(0.3, "USD", "0.3$")])

        test("0.2 £", [(0.2, "GBP", "0.2 £")])
        test("0.2£", [(0.2, "GBP", "0.2£")])

        test("0.2 €", [(0.2, "EUR", "0.2 €")])
        test("0.2€", [(0.2, "EUR", "0.2€")])


        test("-5 рублей", [(5.0, "RUB", "5 рублей")])
        test("10 рублей + 20 фунтов", [(10.0, "RUB", "10 рублей"), (20.0, "GBP", "20 фунтов")])

        test("3^5 фунтов", [(5.0, 'GBP', "5 фунтов")])
        test("0x1999 фунтов", [(1999.0, 'GBP', "1999 фунтов")])
        test("50e10 фунтов", [(10.0, 'GBP', "10 фунтов")])
        test("5+5 долларов", [(5.0, 'USD', "5 долларов")])
        test("${7*7} долларов", [])
        test("1e10 рублей", [(10.0, 'RUB', "10 рублей")])
        test("4+5 рублей", [(5.0, 'RUB', "5 рублей")])
        test("4-5 рублей", [(5.0, 'RUB', "5 рублей")])
        test("4/5 рублей", [(5.0, 'RUB', "5 рублей")])
        test("4*5 рублей", [(5.0, 'RUB', "5 рублей")])
        test("4^5 рублей", [(5.0, 'RUB', "5 рублей")])
        test("4%5 рублей", [(5.0, 'RUB', "5 рублей")])
        test("4!5 рублей", [(5.0, 'RUB', "5 рублей")])
        test("5! рублей", [])

        test("4.5 в рублей", [])
        test("4.5 рублей", [(4.5, 'RUB', "4.5 рублей")])
        test("100-10 рублей", [(10.0, 'RUB', "10 рублей")])
        test("20 динар", [(20.0, 'JOD', "20 динар")])

        test("-100 баксов", [(100.0, "USD", "100 баксов")])
        test("0 рублей", [(0.0, "RUB", "0 рублей")])
        test("0рублей", [(0.0, "RUB", "0рублей")])

        test("-10 рублей", [(10.0, "RUB", "10 рублей")])
        test("-1 рублей", [(1.0, "RUB", "1 рублей")])
        test("-0 рублей", [(0.0, "RUB", "0 рублей")])
        test("-0 сколько рублей", [])
        test("-0 сколько рублей и долларов", [])
        test("Сто фунтов", [])
        test("Двадцать два рубля", [])
        test("Пять тысяч рублей", [])
        test("пицот рублей", [])
        test("Две тысячи двести двадцать два рубля", [])

        test("10:30 рублей", [(30.0, "RUB", "30 рублей")])
        test("10:30 и дальш�� рублей", [])

        test("1$1", [(1.0, 'USD', '1$')])
        test("1$1$", [(1.0, 'USD', '1$'), (1.0, 'USD', '1$')])
        test("1$$1", [(1.0, 'USD', '1$'), (1.0, 'USD', '$1')])
        test("1$$1$", [(1.0, 'USD', '1$'), (1.0, 'USD', '$1')])
        test("1$1$1$1$1$1$1$1$1$", [(1.0, 'USD', '1$'), (1.0, 'USD', '1$'), (1.0, 'USD', '1$'), (1.0, 'USD', '1$'), (1.0, 'USD', '1$'), (1.0, 'USD', '1$'), (1.0, 'USD', '1$'), (1.0, 'USD', '1$'), (1.0, 'USD', '1$')])
        test("1$1$1$1$1$1$1$1$1$1$", [(1.0, 'USD', '1$'), (1.0, 'USD', '1$'), (1.0, 'USD', '1$'), (1.0, 'USD', '1$'), (1.0, 'USD', '1$'), (1.0, 'USD', '1$'), (1.0, 'USD', '1$'), (1.0, 'USD', '1$'), (1.0, 'USD', '1$'), (1.0, 'USD', '1$')])
        test("1. рубль", [])
        test("0. драм", [])
        test("AMD6521", [])
        test("AMD 6521", [])
        test("1 TON", [])
        test("null долларов", [])
        test("Бля рубля", [])
        test("1 шахерезада", [])
        test("20 песо", [])
        test("30 пхп", [])
        test("100500 кгам", [])
        test("1337 чего блядь", [])
        test("5500 AMD", [])
        test("1337 лари", [(1337.0, "GEL", "1337 лари")])
        test("415 amd", [])
        test("300$", [(300.0, "USD", "300$")])
        test("10 юаней", [(10.0, "CNY", "10 юаней")])
        test("1 фунт", [(1.0, "GBP", "1 фунт")])
        test("1488 фунтов", [(1488.0, "GBP", "1488 фунтов")])
        test("5 баксов", [(5.0, "USD", "5 баксов")])
        test("99 фунтов и 100 долларов", [(99.0, "GBP", "99 фунтов"), (100.0, "USD", "100 долларов")])
        test("10 рублей + 1 рубль", [(10.0, "RUB", "10 рублей"), (1.0, "RUB", "1 рубль")])
        test("999999999999999999999999 фунтов", [(999999999999999999999999.0, "GBP", "999999999999999999999999 фунтов")])
        test("500 сигарет", [])
        test("500 хуёв тебе в жопу", [])    
        test("8", [])

        test("Бля ₪", [])
        test("50 нфс", [])
        test("50 агорот", [])
        test("50 огород", [])


        test("1 рубль", [(1.0, "RUB", "1 рубль")])
        test("1 лари 100 рублей 2 доллара", [(1.0, "GEL", "1 лари"), (100.0, "RUB", "100 рублей"), (2.0, "USD", "2 доллара")])
        test("0.0 кг, 0.1 ₽,", [(0.1, 'RUB', '0.1 ₽')])
        test("0.001 фунта", [(0.001, 'GBP', '0.001 фунта')])
        test("1 лари", [(1.0, "GEL", "1 лари")])
        test("0.0015 рублей", [(0.0015, 'RUB', '0.0015 рублей')])

        test("Пять 6 долларов", [(6.0, 'USD', '6 долларов')])
        test("5 6 7 долларов", [(7.0, 'USD', '7 долларов')])
        test("3 шекеля", [(3.0, 'ILS', '3 шекеля')])
        test("10000 рублей", [(10000.0, 'RUB', '10000 рублей')])
        test("двадцать 2 рубля", [(2.0, 'RUB', '2 рубля')])
        test("Один1 рублей", [(1.0, 'RUB', '1 рублей')])

        test("1.0 рублей", [(1.0, 'RUB', '1.0 рублей')])
        test("1. Рублей", [])
        test("2. Долларов", [])
        test("0. драм", [])

        test("-100 фунтов", [(100.0, "GBP", "100 фунтов")])
        test("-100000000000 фунтов", [(100000000000.0, "GBP", "100000000000 фунтов")])
        test("15 фунтов", [(15.0, "GBP", "15 фунтов")])
        test("12345679x9 евро", [(9.0, "EUR", "9 евро")])
        test("1блять1 долларов", [(1.0, "USD", "1 долларов")])
        test("Ox5 долларов", [(5.0, "USD", "5 долларов")])
        test("Блять11 долларов", [(11.0, "USD", "11 долларов")])
        test("Вставить 0,05 ₽", [(0.05, 'RUB', '0,05 ₽')])

        # Тесты для центов
        test("50 центов", [(0.5, "USD", "50 центов")])
        test("1 цент", [(0.01, "USD", "1 цент")])
        test("2 цента", [(0.02, "USD", "2 цента")])
        test("5 cents", [(0.05, "USD", "5 cents")])
        test("1 cent", [(0.01, "USD", "1 cent")])
        
        # Тесты для евроцентов
        test("50 евроцентов", [(0.5, "EUR", "50 евроцентов")])
        test("1 евроцент", [(0.01, "EUR", "1 евроцент")])
        test("2 евроцента", [(0.02, "EUR", "2 евроцента")])
        test("5 eurocents", [(0.05, "EUR", "5 eurocents")])
        test("1 eurocent", [(0.01, "EUR", "1 eurocent")])
        
        # Комбинированные тесты
        test("5 долларов 30 центов", [(5.0, "USD", "5 долларов"), (0.3, "USD", "30 центов")])
        test("2 евро 15 евроцентов", [(2.0, "EUR", "2 евро"), (0.15, "EUR", "15 евроцентов")])
        test("1 доллар 1 цент", [(1.0, "USD", "1 доллар"), (0.01, "USD", "1 цент")])
        test("1 евро 1 евроцент", [(1.0, "EUR", "1 евро"), (0.01, "EUR", "1 евроцент")])

        # Негативные тесты
        test("центов", [])
        test("евроцентов", [])
        test("k центов", [])
        test("k евроцентов", [])
        test("0 центов", [(0.0, "USD", "0 центов")])
        test("0 евроцентов", [(0.0, "EUR", "0 евроцентов")])

        test("1,000 долларов", [(1000.0, "USD", "1,000 долларов")])
        test("1 000 долларов", [(1000.0, "USD", "1 000 долларов")])
        test("1 000,50 долларов", [(1000.50, "USD", "1 000,50 долларов")])
        test("2.500,75 евро", [(2500.75, "EUR", "2.500,75 евро")])
        test("3,000,000 йен", [(3000000.0, "JPY", "3,000,000 йен")])

        # Тесты для отрицательных сумм
        test("-5 долларов", [(5.0, "USD", "5 долларов")])
        test("минус 10 евро", [(10.0, "EUR", "10 евро")])

        test("¥1000", [(1000.0, "JPY", "¥1000")])
        test("1000¥", [(1000.0, "JPY", "1000¥")])

        # Тесты для дополнительных валют
        test("500 юаней", [(500.0, "CNY", "500 юаней")])
        test("200 cny", [(200.0, "CNY", "200 cny")])
        test("100 шекелей", [(100.0, "ILS", "100 шекелей")])
        test("200₪", [(200.0, "ILS", "200₪")])

        # Негативные тесты для некорректных форматов
        test("100..50 долларов", [(50.0, 'USD', '50 долларов')])
        test("100, долларов", [])
        test("долларов 100", [])
        test("две тысячи долларов", [])
        test("минус пять евро", [])
        test("5 долларов США", [(5.0, 'USD', '5 долларов')])

        # Тесты для чисел с разделителями тысяч и десятичными
        test("1 000,50 долларов", [(1000.50, "USD", "1 000,50 долларов")])
        test("1.000,50 евро", [(1000.50, "EUR", "1.000,50 евро")])
        test("1,000.50 фунтов", [(1000.50, "GBP", "1,000.50 фунтов")])
        test("3,000,000 йен", [(3000000.0, "JPY", "3,000,000 йен")])
        test("3 412 928 ₪", [(3412928.0, "ILS", "3 412 928 ₪")])
        
        # Дополнительные тесты для проверки граничных случаев
        #test("1.000.000,50 евро", [(1000000.50, "EUR", "1.000.000,50 евро")])
        #test("1,000,000.50 долларов", [(1000000.50, "USD", "1,000,000.50 долларов")])
        test("1 000 000,50 рублей", [(1000000.50, "RUB", "1 000 000,50 рублей")])
        #test("1.234.567,89 евро", [(1234567.89, "EUR", "1.234.567,89 евро")])
        #test("1,234,567.89 фунтов", [(1234567.89, "GBP", "1,234,567.89 фунтов")])


from currency_formatter import CurrencyFormatter

class StubExchangeRatesManager:
    def get_rate(self, from_currency, to_currency):
        # Возвращаем фиксированный курс для тестирования
        return 1.0  # Курс 1 для упрощения тестов

class TestCurrencyFormatting(unittest.TestCase):
    def setUp(self):
        self.parser = TestCurrencyParser()
        self.formatter = CurrencyFormatter()
        self.rates_manager = StubExchangeRatesManager()
        self.rates = {}
        for curr in self.formatter.target_currencies:
            for target in self.formatter.target_currencies:
                if curr != target:
                    self.rates[f"{curr}_{target}"] = self.rates_manager.get_rate(curr, target)

    def test_formatter(self):
        def test(input_text: str, expected_output: str):
            currency_list = self.parser.find_currencies(input_text)
            result = self.formatter.format_multiple_conversions(currency_list, self.rates, mode='chat')
            self.assertEqual(result, expected_output)

        test("100 долларов", "100 долларов (🇺🇸) это 🇪🇺 €100, 🇬🇧 £100, 🇷🇺 100 ₽, 🇮🇱 100 ₪, 🇯🇵 100 ¥, 🇦🇲 100 ֏")
        test("100 фунтов", "100 фунтов (🇬🇧) это 45.4 кг, а также 🇺🇸 $100, 🇪🇺 €100, 🇷🇺 100 ₽, 🇮🇱 100 ₪, 🇯🇵 100 ¥, 🇦🇲 100 ֏")
        test("0 рублей", "Нахуй пошел")
        test("0 динаров", "Нахуй пошел")
        test("k динаров", None)
        test("k долларов", None)
        test("k евро", None)
        test("k йен", None)
        test("k юаней", None)
        test("k лари", None)
        test("k батов", None)
        test("k тенге", None)
        test(" 5 пять минут пять минут долларов", None)
        test("2000000 долларов", "Откуда у тебя такие деньги, сынок?")
        test("Ноль ноль долларов", None)
        test("Пять минус пять долларов", None)
        test("Восемь восемьсот пять пять пять три пять три пять рублей", None)
        test("Один один доллар", None)
        test("1 bdsm", None)
        test("1 килограмм рублей", None)
        test("1 килограмм рублей", None)
        test("1 TON", None)
        test("дюжина рублей", None)
        test("Сво рублей", None)
        test("Да бля а как работает сто сто рублей", None)
        test("6 пять долларов", None)
        test("13\" рублей", None)
        test("Десятнадцать рублей", None)
        test("миллиард долларов", None)
        test("Додекалион рублей", None)
        test("ёёёёё23322ёёёё драм", None)
        test("Один четыре восемь восемь продавать рублей не бросим", None)
        test("ёдесять рублей", None)
        test("тридцатьё лари", None)
        test("Двeсти рyблей", None)
        test("Двести') exit() рублей", None)
        test("Двести рублей') exit() рублей", None)
        test("Две тысячи двести <script>alert()</script> двадцать два рубля", None)
        test("две тысячи ХУËВ ТЕБЕ В ЖОПУ двадцать восемь фунтов", None)
        test("Пять сто пять восемь рублей", None)
        test("Пять сто пять восемь", None)
        test("Две тысячи ПОШЕЛ НА ХУЙ двести двадцать два рубля", None)
        test("Сто блядских рублей", None)
        test("Пять пять рублей", None)
        test("что рублей где", None)
        test("Две тысячи бля двести двадцать два рубля", None)
        test("Сто сто рублей", None)
        test("Две тысячи двести двадцать два рубля", None)
        test("Арубля", None)
        test("1Арубля", None)
        test("10 Арубля", None)
        test("Влад скинь долларов пабрацки", None)
        test("2 бля", None)
        test("Влад скинь длооаров пабрацки", None)
        test("Пица рублей", None)
        test("пицот рублей", None)
        test("100 песо", None)
        test("``5+5`` долларов", None)
        test("Звоните мне на +79936969420", None)
        test("у меня когда-то в Додо был пин-код 1488, чтобы додорубли списывать", None)
        test("100500 кгам", None)
        test("1488 хуёв", None)
        test("сто тысяч миллионов зимбабвийских долларов", None)
        test("сто фунтов хуев тебе в панамку", None)
        test("два фунта мяса", None)
        test("100 т", None)
        test("я вам расскажу историю про 1488, но писать мне лень, поэтому будет войс мессадж ебать", None)
        test("50 юсд", None)
        test("Пять фунтов долларов", None)
        test("Сука где, фунты есть же", None)
        test("100 камней", None)
        test("Сто фунтов", None)
        test("Я хочу доллар по рублю", None)
        test("Хотя нахер мне доллар)", None)
        test("Могу продать рубль по доллару", None)
        test("Суки скинулись по рублю и разбежались", None)
        test("¾ рублей", None)
        test("Deployed vm nillion-cxs6v0lt in 'dosage' (took 26 min 8 sec, vm 145 out of 301 in batch, left 156 nodes", None)
        test("50 cents", "In Da Club!")
        test("0.5 USD", "In Da Club!")
        test("Привет, как дела?", None)

    def test_inline_formatter(self):
        def test(input_text: str, expected_output: str):
            currency_list = self.parser.find_currencies(input_text)
            result = self.formatter.format_multiple_conversions(currency_list, self.rates, mode='inline')
            self.assertEqual(result, expected_output)

        # Базовые тесты для inline режима
        test("100 долларов", "100 долларов (🇪🇺 €100, 🇬🇧 £100, 🇷🇺 100 ₽, 🇮🇱 100 ₪, 🇯🇵 100 ¥, 🇦🇲 100 ֏)")
        test("100 фунтов", "100 фунтов (45.4 кг) (🇺🇸 $100, 🇪🇺 €100, 🇷🇺 100 ₽, 🇮🇱 100 ₪, 🇯🇵 100 ¥, 🇦🇲 100 ֏)")
        
        # Тесты для специальных случаев
        test("0 долларов", "0 долларов (🇪🇺 €0.0, 🇬🇧 £0.0, 🇷🇺 0.0 ₽, 🇮🇱 0.0 ₪, 🇯🇵 0.0 ¥, 🇦🇲 0.0 ֏)")
        test("0.5 USD", "0.5 USD (🇪🇺 €0.5, 🇬🇧 £0.5, 🇷🇺 0.5 ₽, 🇮🇱 0.5 ₪, 🇯🇵 0.5 ¥, 🇦🇲 0.5 ֏)")
        test("2000000 долларов", "2000000 долларов (🇪🇺 €2 000 000, 🇬🇧 £2 000 000, 🇷🇺 2 000 000 ₽, 🇮🇱 2 000 000 ₪, 🇯🇵 2 000 000 ¥, 🇦🇲 2 000 000 ֏)")
        
        # Тест для множественных валют
        test("100 долларов и 200 евро", 
                "100 долларов (🇪🇺 €100, 🇬🇧 £100, 🇷🇺 100 ₽, 🇮🇱 100 ₪, 🇯🇵 100 ¥, 🇦🇲 100 ֏)\n" + 
                "200 евро (🇺🇸 $200, 🇬🇧 £200, 🇷🇺 200 ₽, 🇮🇱 200 ₪, 🇯🇵 200 ¥, 🇦🇲 200 ֏)")
        
        # Тест для фунтов (с конвертацией в кг)
        test("1 фунт", "1 фунт (0.5 кг) (🇺🇸 $1.0, 🇪🇺 €1.0, 🇷🇺 1.0 ₽, 🇮🇱 1.0 ₪, 🇯🇵 1.0 ¥, 🇦🇲 1.0 ֏)")
        
        # Тест для форматирования больших чисел
        test("10000 долларов", "10000 долларов (🇪🇺 €10000, 🇬🇧 £10000, 🇷🇺 10000 ₽, 🇮🇱 10000 ₪, 🇯🇵 10000 ¥, 🇦🇲 10000 ֏)")
        test("30000 долларов", "30000 долларов (🇪🇺 €30 000, 🇬🇧 £30 000, 🇷🇺 30 000 ₽, 🇮🇱 30 000 ₪, 🇯🇵 30 000 ¥, 🇦🇲 30 000 ֏)")

        # Тест для десятичных чисел
        test("12.34 евро", "12.34 евро (🇺🇸 $12.3, 🇬🇧 £12.3, 🇷🇺 12.3 ₽, 🇮🇱 12.3 ₪, 🇯🇵 12.3 ¥, 🇦🇲 12.3 ֏)")
        
        # Тест для отсутствия курсов конвертации
        def test_no_rates(self):
            currency_list = self.parser.find_currencies("100 долларов")
            result = self.formatter.format_multiple_conversions(currency_list, {}, mode='inline')
            self.assertEqual(result, "100 долларов (нет доступных курсов конвертации)")

if __name__ == '__main__':
    unittest.main() 