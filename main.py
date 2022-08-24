""" 
CRUD

Create 
Read - Retrieve
Update
Delete
"""


import shelve
from datetime import datetime

from settings import FILENAME



def create_data():
    """
    Requests information from a user and creates an item in the database
    """
    id_ = datetime.now().strftime('%H%M%S')
    title = input('Введите название товара: ')
    price = int(input('Введите цену товара: '))
    description = input('Введите описание: ')
    created_at = datetime.now().strftime('%d.%m.%y %H:%M')
    with shelve.open(FILENAME) as db:
        db[id_] = {
            'title': title,
            'price': price,
            'description': description,
            'created_at': created_at
        }



def get_all_data():
    """
    Shows a list of items in the database
    """
    with shelve.open(FILENAME) as db:
        for key, value in db.items():
            print('-------------------------------------------------------')
            print('id:', key, '|', 'title:', value['title'], '|', 'price:', value['price'])
            print('-------------------------------------------------------')



def get_data_by_id():
    """
    Retreives an item that is requested
    """
    with shelve.open(FILENAME) as db:
        print(f'Список доступных id: {list(db.keys())}')
        id_ = input('Введите id товара: ')
        try:
            prod = db[id_]
            print(
                f"""
                Название: {prod['title']}
                Цена: {prod['price']}
                Описание: {prod['description']}
                Время создания: {prod['created_at']}
                """
            )
        except KeyError:
            print(f'{id_} не существует')



def update_data():
    """
    Changes information about an item
    """
    with shelve.open(FILENAME, writeback=True) as db:
        print(f'Список доступных id: {list(db.keys())}')
        id_ = input('Введите id товара: ')
        try:
            prod = db[id_]
            prod['title'] = input('Введите новое название: ') or prod['title']
            prod['price'] = int(input('Введите новую цену: ')) or prod['price']
            prod['description'] = input('Введите новое описание: ') or prod['description']
        except KeyError:
            print(f'{id_} не существует')



def delete_data():
    """
    Deletes an item by its id
    """
    with shelve.open(FILENAME) as db:
        print(f'Список доступных id: {list(db.keys())}')
        id_ = input('Введите id товара: ')
        try:
            db.pop(id_)
        except KeyError:
            print(f'{id_} не существует')


# with shelve.open(FILENAME) as db:
#     prod = list(db.keys())

while True:
    
    operation = str(input("""
    Введите операцию, которую хотите совершить: 
    1. create - создать новый продукт
    2. delete - удалить продукт по id
    3. list - получить список всех продуктов
    4. retrieve - получить продукт по id
    5. clear - очистить базу данных
    6. update - изменить данные
    7. exit - выйти из программы

    """)).lower().strip()

    with shelve.open(FILENAME) as db:
        if operation == '1' or operation == 'create':  
            create_data()
        elif operation == '2' or operation == 'delete':
            delete_data()
        elif operation == '3' or operation == 'list':
            get_all_data() 
        elif operation == '4' or operation == 'retrieve': 
            get_data_by_id()
        elif operation == '5' or operation == 'clear':
            db.clear()
        elif operation == '6' or operation == 'update':
            update_data()
        elif operation == '7' or operation == 'exit':
            print('Всего доброго!')
            break
        else:
            print('Такой операции не существует. Проверьте правильность ввода.')
            continue