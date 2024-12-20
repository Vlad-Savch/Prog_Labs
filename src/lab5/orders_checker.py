import re
from collections import Counter

phone_pattern = re.compile(r'^\+(\d)-(\d{3})-(\d{3})-(\d{2})-(\d{2})$')


def process_orders(input_file, valid_file, invalid_file):
    orders = []
    invalid_orders = []

    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            order = line.strip().split(';')
            if len(order) != 6:
                continue

            order_id, products, full_name, address, phone, priority = order

            errors = []

            # 1. Проверка номера заказа
            if len(order_id) != 5 or not order_id.isdigit():
                errors.append("Номер заказа должен быть пятизначным числом.")

            # 2. Проверка набора продуктов
            if not products:
                errors.append("Набор продуктов не может быть пустым.")

            # 3. Проверка ФИО заказчика
            name_parts = full_name.split()
            if len(name_parts) < 2:
                errors.append("ФИО заказчика должно содержать хотя бы фамилию и имя.")

            # 4. Проверка адреса доставки
            if not address or len(address.split('.')) < 4:
                errors.append("Ошибка заполнения адреса доставки.")
            else:
                address_parts = address.split('.')
                if len(address_parts) < 4 or any(not part.strip() for part in address_parts):
                    errors.append("Ошибка заполнения адреса доставки.")

            # 5. Проверка номера телефона
            if not phone or not phone_pattern.match(phone):
                errors.append("Ошибка заполнения номера телефона.")

            # 6. Проверка приоритета доставки
            if priority not in ['MAX', 'MIDDLE', 'LOW']:
                errors.append("Приоритет доставки должен быть MAX, MIDDLE или LOW.")

            if errors:
                for error in errors:
                    if 'адрес' in error:
                        invalid_orders.append(f"{order_id};1;{address if address else 'no data'}")
                    elif 'телефон' in error:
                        invalid_orders.append(f"{order_id};2;{phone if phone else 'no data'}")
                    elif 'Набор продуктов' in error or 'ФИО' in error or 'Приоритет' in error:
                        invalid_orders.append(f"{order_id};1;no data")

            else:
                country = address.split('.')[0].strip()
                region_city_street = '.'.join(address.split('.')[1:]).strip()

                product_list = products.split(', ')
                product_count = Counter(product_list)

                formatted_products = ', '.join(
                    [f"{product} x{count}" if count > 1 else product for product, count in product_count.items()])

                orders.append((order_id, formatted_products, full_name, region_city_street, phone, priority, country))


