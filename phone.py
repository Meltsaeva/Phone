# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

# Показывает информацию в файле
def show_data(filename):
    print("\n №| Name | Phone | inf")
    with open(filename, "r", encoding="utf-8") as data:
        print(data.read())
    print("")

# Записывает информацию в файл
def export_data(filename):
    with open(filename, "r", encoding="utf-8") as data:
        tel_file = data.read()
    num = len(tel_file.split("\n"))
    with open(filename, "a", encoding="utf-8") as data: 
        fio = input("Enter a name: ")
        phone_number = input("Enter a phone: ")
        inform = input("Enter the information")
        data.write(f"{num} | {fio} | {phone_number} | {inform}\n")
        print(f"An entry has been added: {num} | {fio} | {phone_number} | {inform}\n")

# Изменяет информацию из файла
def edit_data(filename):
    print("\n № | Name | Phone | inf")
    with open(filename, "r", encoding='utf-8') as data:
        tel_book = data.read()
    print(tel_book)
    print("")
    index_delete_data = int(input("Enter the line number to edit: ")) - 1
    tel_book_lines = tel_book.split("\n")
    edit_tel_book_lines = tel_book_lines[index_delete_data]
    elements = edit_tel_book_lines.split(" | ")
    fio = input("Enter a name: ")
    phone = input("Enter a phone: ")
    inform = input("Enter the information")
    num = elements[0]
    if len(fio) == 0:
        fio = elements[1]
    if len(phone) == 0:
        phone = elements[2]
    if len(inform) == 0:
        inform = elements[3]
    edited_line = f"{num} | {fio} | {phone} | {inform}"
    tel_book_lines[index_delete_data] = edited_line
    print(f"Note - {edit_tel_book_lines}, has been changed to - {edited_line}\n")
    with open(filename, "w", encoding='utf-8') as f:
        f.write("\n".join(tel_book_lines))

# Удаляет информацию из файла
def delete_data(filename):
    print("\n № | Name | Phone | inf")
    with open(filename, "r", encoding="utf-8") as data:
        tel_book = data.read()
        print(tel_book)
    print("")
    index_delete_data = int(input("Enter the line number to delete: ")) - 1
    tel_book_lines = tel_book.split("\n")
    del_tel_book_lines = tel_book_lines[index_delete_data]
    tel_book_lines.pop(index_delete_data)
    print(f"deleted: {del_tel_book_lines}\n")
    with open(filename, "w", encoding='utf-8') as data:
        data.write("\n".join(tel_book_lines))

def main():
    my_choice = -1
    file_tel = "tel.txt"

    # Создает файл если его нет в папке
    with open(file_tel, "a", encoding="utf-8") as file:
         file.write("")

    while my_choice != 0:
        print("Choose one of the actions:")
        print("1 - Display info on the screen")
        print("2 - Export data")
        print("3 - Make a data change")
        print("4 - Delete data")
        print("0 - Exit")
        action = int(input("Action: "))
        if action == 1:
            show_data(file_tel)
        elif action == 2:
            export_data(file_tel)
        elif action == 3:
            edit_data(file_tel)
        elif action == 4:
            delete_data(file_tel)
        else:
            my_choice = 0

    print("See you")

if __name__ == "__main__":
    main()
