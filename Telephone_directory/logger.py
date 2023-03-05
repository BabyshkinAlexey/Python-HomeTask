import os
from data_create import name_data, surname_data, phone_data, address_data

file_name = "data.txt"

def print_data():
    number = 0
    if os.path.exists(file_name):
        print(f"=== Ввывод данных из файла: === \n")
        with open(file_name, "r", encoding = "utf-8") as file:
            list_data = file.readlines()
            for element in list_data:
                number += 1
                print(f"{number}) {element} \n")
    else:
        print("Файл не существует!")
    
def input_data():
    print("Введите данные: ")
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    with open(file_name, "a", encoding = "utf-8") as file:
        file.write(f"{name}; {surname}; {phone}; {address}. \n", )
        
def filter_data(filter_string):
    with open(file_name, "r", encoding = "utf-8") as file:
        list_data = file.readlines()
        if ";" in filter_string:
            list_filter = filter_string.split(";")
        else:
            list_filter = [filter_string]
        is_found = False
        for element in list_data:
            temp_record = element.split(";")
            count = 0
            for record in temp_record:
                for element_filter in list_filter:
                    if element_filter.lower() in record.lower() and len(element_filter.lower()) == len(record.lower()):
                        count += 1
            if count == len(list_filter):
                print(element)
                is_found = True
    if not is_found:
        print("Записей не найдено!")
        
def swap_value():
    search_text= input("Что нужно изменить: ")
    replace_text = input("На что нужно изменить: ")
    with open(file_name, 'r') as file:
        data = file.read()
        data = data.replace(search_text.lower().strip(), replace_text.lower().strip())
    with open(file_name, 'w') as file:
        file.write(data)

        
def remove_record():
    with open(file_name, 'r') as file:
        data = file.readlines()
    with open(file_name, 'w') as file:
        a = input("Введите данные для удаления: ")
        for line in data:
            if line.lower().strip() != a.lower().strip():
                file.write(line)
        
# Игорь; Игорев; 2345; Березники 
# Михаил; Носков; 2345678; Уфа 
# Алексей; Воробьев; 12345678; Пермь 
