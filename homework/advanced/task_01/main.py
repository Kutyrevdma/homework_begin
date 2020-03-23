import datetime
import time
from advanced.task_01 import salary, people

Date_Creation = datetime.datetime.today().strftime("%d-%m-%Y")
Time_Creation = time.strftime("%H.%M.%S")

print(f'Дата: {Time_Creation} {Date_Creation}\n')

if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()

print("Закончено выполнение if __name__ == '__main__'\n\n\n------------------\n\n\n")

"""Это для теста! Что в файле test.py выпонятеся код без конструкции if __name__ == '__main__': """
print('Это часть кода из main.py TEST')
salary.calculate_salary()
people.get_employees()

