import csv
import re as regexp


def start():
    csv_path = 'funcs_homework_employees_sample.csv'
    with open(csv_path, newline='', encoding='utf-8') as f:
        employees = csv_reader(f, separate=';')
    department = department_create(employees)
    print(
        '1. Вывести все отделы.\n2. Сводный отчет по отделам.\n3. Сохранить сводный отчёт (см. п.2) в виде csv-файла. ')
    option = ''
    options = ['1', '2', '3']
    while option not in options:
        print('Выберите пункт меню: {}, {}, {}'.format(*options))
        option = input()
    if option == '1':
        print('Отделы:')
        print(','. join(department))
    elif option == '2':
        report = report_department_make(employees, department)
        for i in range(len(report)):
            report[i] = list(map(str, report[i][:]))
            print(''.join('{:>25}'.format(x) for x in report[i]))
    elif option == '3':
        report = report_department_make(employees, department)
        save_report(report)


def csv_reader(f_obj, separate):
    """
        Чтение csv файла и запись
    """

    reader = csv.reader(f_obj, delimiter=separate)
    employees = []
    for row in reader:
        employees.append(row)
    for i in range(1, len(employees)):
        employees[i][4] = int(employees[i][4])
        search_index = regexp.search(r'->', employees[i][2])
        if search_index is not None:
            employees[i][2] = employees[i][2][0:search_index.start()].strip()
    return employees


def department_create(employees):
    """
        Создание уникального массива отдела
    """
    col2 = []
    for i in range(1, len(employees)):
        col2.append(employees[i][2])
    department = set(col2)
    return department


def report_department_make(employees, department):
    """
        Сводный отчет по отделам
    """
    report_department = [['Отдел', 'Количество сотрудников', 'Минимальная з/п', 'Максимальная з/п', 'Средняя з/п']]
    for i in department:
        report_department.append([i, 0, 0, 0, 0])
    for i in range(1, len(employees)):
        for j in range(1, len(report_department)):
            if employees[i][2] == report_department[j][0]:
                report_department[j][1] += 1
                if report_department[j][1] == 1:
                    report_department[j][2] = employees[i][4]
                elif employees[i][4] < report_department[j][2]:
                    report_department[j][2] = employees[i][4]
                if employees[i][4] > report_department[j][3]:
                    report_department[j][3] = employees[i][4]
                report_department[j][4] += employees[i][4]
    return report_department


def save_report(report):
    """
        Сохранение отчета по отделам в файл
    """
    with open("report_department.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(report)
    print('Файл создан')


start()
