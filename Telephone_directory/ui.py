from logger import input_data, print_data, filter_data, swap_value, remove_record
    
def interface():
    print("""Выбирите режим работы в программе:
                1 - запись данных
                2 - вывод  данных
                3 - поиск  данных
                4 - изменение данных
                5 - удаление данных
          """)
    comman_number = int(input("Введите номер комманды: ")) 
    while comman_number < 1 or comman_number > 5:
        print("Введите корректный номер команды: ")
        comman_number = int(input("Введите номер комманды: "))
    
    if comman_number == 1:
        input_data()
    elif comman_number == 2:
        print_data()
    elif comman_number == 3:
        print("Введите параметры поиска через ';' : ")
        filter_string = input()
        filter_data(filter_string)
    elif comman_number == 4:
        print_data()
        swap_value()
    elif comman_number == 5:
        print_data()
        remove_record()      