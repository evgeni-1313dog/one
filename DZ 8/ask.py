def choice():
    choice = int(input("Введите категорию 1 - импорт данных, 2 - экспорт данных, 3 - удалить контакт, 4 - редоктировать: "))
    return choice

def get_user():
    return input("Введите имя, фамилия, номер телефона (даные ввести через пробел): ")
    
def ask():
    return input("Введите имя, фамилия, номер телефона для поиска в базе: ")

def delete_person():
    return input("Удалить контакт: ")

def change_person():
    return input("Редоктировать контакт: ")