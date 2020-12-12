class View:
    def __init__(self, table, records):
        self.table = table
        self.records = records

    @staticmethod
    def list():
        print(" 1. Rule Breaker\n", "2. Car\n", "3. Traffic Violation\n",
              "4. Policeman\n", "5. Department\n", "6. Head of department\n", "7. Protocol\n")
        number = input("\nMake your number: ")
        return int(number)

    def show(self):
        if self.table == 1:
            for row in self.records:
                print("\nrule_breaker_id =", row[0])
                print("rule_breaker_name =", row[1])
                print("rule_breaker_surname =", row[2])
                print("rule_breaker_birthDate =", row[3])
        elif self.table == 2:
            for row in self.records:
                print("\ncar_id =", row[0])
                print("owner_id =", row[1])
                print("car_model =", row[2])
                print("car_release =", row[3])
        elif self.table == 3:
            for row in self.records:
                print("\ntraffic_violation_id =", row[0])
                print("traffic_violation_type =", row[1])
                print("price = ", row[2])
        elif self.table == 4:
            for row in self.records:
                print("\npoliceman_id =", row[0])
                print("policeman_name =", row[1])
                print("policeman_surname =", row[2])
                print("policeman_rank =", row[3])
                print("department_id =", row[4])
        elif self.table == 5:
            for row in self.records:
                print("\ndepartment_id =", row[0])
                print("department_address =", row[1])
        elif self.table == 6:
            for row in self.records:
                print("\nhead_id =", row[0])
                print("head_name =", row[1])
                print("head_surname =", row[2])
                print("head_rank =", row[3])
        elif self.table == 7:
            for row in self.records:
                print("\nprotocol_id =", row[0])
                print("policeman_id =", row[1])
                print("rule_breaker_id =", row[2])
                print("traffic_violation_id =", row[3])

    @staticmethod
    def attribute_list(table):
        if table == 1:
            print(" 1. rule_breaker_id\n", "2. rule_breaker_name\n",
                  "3. rule_breaker_surname\n", "4. rule_breaker_birthDate\n")
        if table == 2:
            print(" 1. car_id\n", "2. owner_id\n", "3. car_model\n", "4. car_release\n")
        if table == 3:
            print(" 1. traffic_violation_id\n", "2. traffic_violation_type\n", "3. price\n")
        if table == 4:
            print(" 1. policeman_id\n", "2. policeman_name\n",
                  "3. policeman_surname\n", "4. policeman_rank\n", "5. department_id\n")
        if table == 5:
            print(" 1. department_id\n", "2. department_address\n")
        if table == 6:
            print(" 1. head_id\n", "2. head_name\n", "3. head_surname\n", "4. head_rank\n")
        if table == 7:
            print(" 1. protocol_id\n", "2. policeman_id\n", "3. rule_breaker_id\n", "4. traffic_violation_id\n")
        number = input('Number of attribute: ')
        return int(number)
