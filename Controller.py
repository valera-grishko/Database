import Model
from View import View

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
            print("6. exit")
            number = int(input('\nMake your number: '))
            if number == 1 or number == 2:
                Model.show_table(number)
            elif number == 3:
                number2 = View.list()
                try:
                    if number2 == 1:
                        Model.RuleBreaker.Insert()
                    elif number2 == 2:
                        Model.Car.Insert()
                    elif number2 == 3:
                        Model.TrafficViolation.Insert()
                    elif number2 == 4:
                        Model.Policeman.Insert()
                    elif number2 == 5:
                        Model.Department.Insert()
                    elif number2 == 6:
                        Model.HeadOfDepartment.Insert()
                    elif number2 == 7:
                        Model.Protocol.Insert()
                except Exception:
                    print("\n... Key Error  ... Please try again ...\n")
            elif number == 4:
                number2 = View.list()
                try:
                    if number2 == 1:
                        Model.RuleBreaker.Delete()
                    elif number2 == 2:
                        Model.Car.Delete()
                    elif number2 == 3:
                        Model.TrafficViolation.Delete()
                    elif number2 == 4:
                        Model.Policeman.Delete()
                    elif number2 == 5:
                        Model.Department.Delete()
                    elif number2 == 6:
                        Model.HeadOfDepartment.Delete()
                    elif number2 == 7:
                        Model.Protocol.Delete()
                except Exception:
                    print("\n... Key Error ... Please try again ...\n")
            elif number == 5:
                number2 = View.list()
                try:
                    if number2 == 1:
                        Model.RuleBreaker.Update()
                    elif number2 == 2:
                        Model.Car.Update()
                    elif number2 == 3:
                        Model.TrafficViolation.Update()
                    elif number2 == 4:
                        Model.Policeman.Update()
                    elif number2 == 5:
                        Model.Department.Update()
                    elif number2 == 6:
                        Model.HeadOfDepartment.Update()
                    elif number2 == 7:
                        Model.Protocol.Update()
                except Exception:
                    print("\n... Key Error ... Please try again ...\n")
            elif number == 6:
                flag = 1
