import psycopg2
from Model import Model

class Controller:
    @staticmethod
    def my_menu():
        flag = 0
        while flag == 0:
            print("<< menu >>")
            print("1. show one table")
            print("2. show all tables")
            print("3. insert data")
            print("4. delete data")
            print("5. update data")
            print("6. randomize data in TrafficViolation")
            print("7. select data")
            print("8. exit")
            number = int(input('\nMake your number: '))
            if number == 1 or number == 2:
                Model.show_table(number)
            elif number == 3:
                try:
                    Model.Insert()
                except Exception:
                    print("\n... Key Error  ... Please try again ...\n")
            elif number == 4:
                try:
                    Model.Delete()
                except Exception:
                    print("\n... Key Error ... Please try again ...\n")
            elif number == 5:
                try:
                    Model.Update()
                except Exception:
                    print("\n... Key Error ... Please try again ...\n")
            elif number == 6:
                try:
                    Model.Random()
                except Exception:
                    print("\n... Key Error ... Please try again ...\n")
            elif number == 7:
                try:
                    Model.Select()
                except Exception:
                    print("\n... Key Error ... Please try again ...\n")
            elif number == 8:
                flag = 1
