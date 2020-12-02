1.	Открыть what_is_year_now_test.py в PyCharm.
2.	Файл what_is_year_now.py должен лежать в той же директории, что и what_is_year_now_test.py
3.	Выполнить запуск в консоли с помощью команды: python -m pytest what_is_year_now_test.py	
4.  Для того, чтобы узнать покрытие необходимо выполнить в консоли команду: python -m pytest --cov .
5.  Для выгрузки покрытия в формате html необходимо выполнить в консоли команду: python -m pytest --cov . --cov-report html
