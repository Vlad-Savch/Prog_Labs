import os
import unittest
from src.lab5.orders_checker import process_orders


class TestOrdersProcessing(unittest.TestCase):
    def setUp(self):
        self.tests_dir = os.path.dirname(__file__)

        self.input_file = os.path.join(self.tests_dir, 'orders.txt')
        self.valid_file = os.path.join(self.tests_dir, 'order_country.txt')
        self.invalid_file = os.path.join(self.tests_dir, 'non_valid_orders.txt')

        with open(self.input_file, 'w', encoding='utf-8') as f:
            f.write("31987;Сыр, Колбаса, Сыр, Макароны, Колбаса;Петрова Анна;Россия. Ленинградская область. Санкт-Петербург. набережная реки Фонтанки;+7-921-456-78-90;MIDDLE\n")
            f.write("87459;Молоко, Яблоки, Хлеб, Яблоки, Молоко;Иванов Иван Иванович;Россия. Московская область. Москва. улица Пушкина;+7-912-345-67-89;MAX\n")
            f.write("31987;Сыр, Колбаса, Макароны, Сыр, Колбаса;Петрова Анна Сергеевна;Франция. Иль-де-Франс. Париж. Шанз-Элизе;+3-214-020-50-50;MIDDLE\n")
            f.write("56342;Хлеб, Молоко, Хлеб, Молоко;Смирнова Мария Леонидовна;Германия. Бавария. Мюнхен. Мариенплац;+4-989-234-56;LOW\n")
            f.write("48276;Яблоки, Макароны, Яблоки;Алексеев Алексей Алексеевич;Италия. Лацио. Рим. Колизей;+3-061-234-56-78;MAX\n")
            f.write("65829;Сок, Вода, Сок, Вода;Белова Екатерина Михайловна;Испания. Каталония. Барселона. Рамбла;+34-93-1234-567;LOW\n")
            f.write("72901;Чай, Кофе, Чай, Кофе;Михайлов Сергей Петрович;Великобритания. Англия. Лондон. Бейкер-стрит;+4-207-946-09-58;LOW\n")
            f.write("84756;Печенье, Сыр, Печенье, Сыр;Васильева Анна Владимировна;Япония. Шибуя. Шибуя-кроссинг;+8-131-234-5678;MAX\n")
            f.write("90385;Макароны, Сыр, Макароны, Сыр;Николаев Николай;;+1-416-123-45-67;LOW\n")

    def test_process_orders(self):
        process_orders(self.input_file, self.valid_file, self.invalid_file)

        expected_valid = (
            "87459;Молоко x2, Яблоки x2, Хлеб;Иванов Иван Иванович;Московская область. Москва. улица Пушкина;+7-912-345-67-89;MAX\n"
            "31987;Сыр x2, Колбаса x2, Макароны;Петрова Анна;Ленинградская область. Санкт-Петербург. набережная реки Фонтанки;+7-921-456-78-90;MIDDLE\n"
            "72901;Чай x2, Кофе x2;Михайлов Сергей Петрович;Англия. Лондон. Бейкер-стрит;+4-207-946-09-58;LOW\n"
            "48276;Яблоки x2, Макароны;Алексеев Алексей Алексеевич;Лацио. Рим. Колизей;+3-061-234-56-78;MAX\n"
            "31987;Сыр x2, Колбаса x2, Макароны;Петрова Анна Сергеевна;Иль-де-Франс. Париж. Шанз-Элизе;+3-214-020-50-50;MIDDLE\n"
        )
        with open(self.valid_file, 'r', encoding='utf-8') as f:
            valid_data = f.read()
        self.assertEqual(valid_data.strip(), expected_valid.strip())

        expected_invalid = (
            "56342;2;+4-989-234-56\n"
            "65829;2;+34-93-1234-567\n"
            "84756;1;Япония. Шибуя. Шибуя-кроссинг\n"
            "84756;2;+8-131-234-5678\n"
            "90385;1;no data\n"
        )
        with open(self.invalid_file, 'r', encoding='utf-8') as f:
            invalid_data = f.read()
        self.assertEqual(invalid_data.strip(), expected_invalid.strip())

    def tearDown(self):
        for file in [self.input_file, self.valid_file, self.invalid_file]:
            if os.path.exists(file):
                os.remove(file)


if __name__ == '__main__':
    unittest.main()
