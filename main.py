import csv
import matplotlib.pyplot as plt
from datetime import datetime as dt

# Сбор данных и приведение их к виду [{инф. по 1 товару}, {инф. по 2 товару}... {инф. по n-ому товару}]
def read_sales_data(file_path):
    products = [] # Список для дальнейшего наполнения информацией на возврат ф-ии
    # Считываем строки из csv файла и сохраняем их в переменную products
    with open(file_path, encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=",")
        # Проходимся по каждому товару и добавляем их в список products в качестве словарей с предварительно обработанными данными (.strip(), .lower())
        for product in reader:
            products.append({'product_name': product[0].strip().lower(), 'quantity': product[1].strip().lower(), 'price': product[2].strip().lower(), 'date': product[3].strip().lower()})
    return products

# Агрегация по наименованию товара. Сумма для каждого товара
def total_sales_per_product(sales_data):
    total_product_sum = [] # Список, который в дальнейшем будет преобразован в словарь для вывода
    # Добавляем в список total_product_sum все возможные значения product_name
    for i in sales_data:
        total_product_sum.append(i['product_name'])
    # Оставляем только уникальные значения product_name и используем их в качестве ключей в словаре total_product_sum
    total_product_sum = dict.fromkeys(set(total_product_sum), 0)
    # Проходимся по основному списку sales_data и увеличиваем сумму продаж определенного продукта в словаре на вывод
    for i in total_product_sum.keys():
        for j in range(len(sales_data)):
            if i == sales_data[j]['product_name']:
                total_product_sum[i] += int(sales_data[j]['price']) * int(sales_data[j]['quantity'])
    return total_product_sum

# Агрегация по дате покупке товара. Общая сумма за дату
def sales_over_time(sales_data):
    total_date_sum = [] # Список, который в дальнейшем будет преобразован в словарь для вывода
    # Добавляем в список total_product_sum все возможные значения date
    for i in sales_data:
        total_date_sum.append(i['date'])
    # Оставляем только уникальные значения date и используем их в качестве ключей в словаре total_date_sum
    total_date_sum = dict.fromkeys(set(total_date_sum), 0)
    # Проходимся по основному списку sales_data и увеличиваем сумму продаж определенной даты в словаре на вывод
    for i in total_date_sum.keys():
        for j in range(len(sales_data)):
            if i == sales_data[j]['date']:
                total_date_sum[i] += int(sales_data[j]['price']) * int(sales_data[j]['quantity'])
    return total_date_sum


sales_data = read_sales_data('input.csv')
product_name_sum = total_sales_per_product(sales_data)
date_sum = sales_over_time(sales_data)
print(product_name_sum)
print(date_sum)

# Построение графиков
# Преобразуем данные и сформируем оси X и Y

# График по дате
plt.figure(figsize=(20, 6))
plt.title('Сумма продаж по датам')
plt.xlabel('Дата')   # Название оси X
plt.ylabel('Сумма продаж (руб.)')
sorted_data_1 = dict(sorted(date_sum.items()))
x_1 = [dt.strptime(i, '%Y-%m-%d').date() for i in sorted_data_1]
y_1 = list(sorted_data_1.values())
plt.plot(x_1, y_1, marker='o')

plt.figure(figsize=(20, 6))
plt.title('Выручка по продуктам')
plt.xlabel('Название продукта')   # Название оси X
plt.ylabel('Выручка за продукт (руб.)')
x_2 = product_name_sum.keys()
y_2 = product_name_sum.values()
plt.bar(x_2, y_2)

plt.show()
