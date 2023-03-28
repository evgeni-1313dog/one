from ask import *
from function import *

while True:
    request = choice()
    if request ==1:
        user = get_user()
        write_data(user)
    elif request == 2:
        users = read_data()
        name = ask()
        find_user(users, name)
    elif request == 3:
        name = input('кого удаляем?: ')
        delete_person(name)
    elif request == 4:
        old_name = input('кого хотим переименовать?: ')
        new_name = input('как хотим его назвать?: ')
        change_person(new_name,old_name)
    elif request == 5:
        break
    else:
        print('No mode')


    # if mode == '1':
    #     print(show_data())
    # elif mode == '0':
    #     find_data()
    # elif mode == '2':
    #     new_data()
    # elif mode == '3':
    #     name = input('кого удаляем?: ')
    #     delete_person(name)
    # elif mode == '4':
    #     old_name = input('кого хотим переименовать?: ')
    #     new_name = input('как хотим его назвать?: ')
    #     change_person(new_name,old_name)
    # elif mode == '5':
    #     break
    # else:
    #     print('No mode')