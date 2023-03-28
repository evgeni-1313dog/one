def write_data(user):
    with open("data.txt", "a") as file:
        file.write(user + "\n")

def read_data():
    with open("data.txt", "r") as file:
        content = file.readline()
        return content
    
def find_user(lst, str):
    for value in lst:
        if str in value:
            print (value)

def delete_person(name):
    persons = read_data()
    with open("data.txt", "w" ) as file:
        for person in persons:
            if name != person:
                file.write(person)

def change_person(new_name, old_name):
    persons = read_data()
    with open("data.txt", "w", ) as file:
        for person in persons:
            if  old_name != person:
                file.write(person)
            else:
                file.write(new_name + "\n")