from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from View import View
import psycopg2
import random
import string

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'postgres',
    'password': 'dfkthfuhbirj',
    'database': 'Penalty for violation of traffic rules'
}

db = declarative_base()

class RuleBreaker(db):
    __tablename__ = 'RuleBreaker'

    rule_breaker_id = Column(Integer, primary_key = True, nullable = False)
    rule_breaker_name = Column(String, nullable = False)
    rule_breaker_surname = Column(String, nullable = False)
    rule_breaker_birthDate = Column(DateTime, nullable = False)

    def __init__(self, id, name, surname, birthDate):
        self.rule_breaker_id = id
        self.rule_breaker_name = name
        self.rule_breaker_surname = surname
        self.rule_breaker_birthDate = birthDate

    @staticmethod
    def Insert():
        new_rule_breaker_id = input('rule_breaker_id = ')
        new_rule_breaker_name = input('rule_breaker_name = ')
        new_rule_breaker_surname = input('rule_breaker_surname = ')
        new_rule_breaker_birthDate = input('rule_breaker_birthDate = ')
        new_rule_breaker = RuleBreaker(new_rule_breaker_id, new_rule_breaker_name, new_rule_breaker_surname, new_rule_breaker_birthDate)
        session.add(new_rule_breaker)
        session.commit()

    @staticmethod
    def Delete():
        delete_id = input('rule_breaker_id delete = ')
        session.delete(session.query(RuleBreaker).filter(RuleBreaker.rule_breaker_id == delete_id).first())
        session.commit()

    @staticmethod
    def Update():
        num = View.attribute_list(1)
        value = input('Attribute value to update = ')
        value2 = input('New attribute value = ')
        if num == 1:
            session.query(RuleBreaker).filter(RuleBreaker.rule_breaker_id == value).update({RuleBreaker.rule_breaker_id: value2})
        elif num == 2:
            session.query(RuleBreaker).filter(RuleBreaker.rule_breaker_name == value).update({RuleBreaker.rule_breaker_name: value2})
        elif num == 3:
            session.query(RuleBreaker).filter(RuleBreaker.rule_breaker_surname == value).update({RuleBreaker.rule_breaker_surname: value2})
        elif num == 4:
            session.query(RuleBreaker).filter(RuleBreaker.rule_breaker_birthDate == value).update({RuleBreaker.rule_breaker_birthDate: value2})
        session.commit()

    def print(self):
        return "<RuleBreaker('%s', '%s', '%s', '%s')>" % (self.rule_breaker_id, self.rule_breaker_name, self.rule_breaker_surname, self.rule_breaker_birthDate)


class Car(db):
    __tablename__ = 'Car'

    car_id = Column(Integer, primary_key = True, nullable = False)
    owner_id = Column(Integer, ForeignKey(RuleBreaker.rule_breaker_id), nullable = False)
    car_model = Column(String, nullable = False)
    car_release = Column(DateTime, nullable = False)

    def __init__(self, id, owner, model, release):
        self.car_id = id
        self.owner_id = owner
        self.car_model = model
        self.car_release = release

    @staticmethod
    def Insert():
        car_id = input('car_id = ')
        owner_id = input('owner_id = ')
        car_model = input('car_model = ')
        car_release = input('car_release = ')
        new_car = Car(car_id, owner_id, car_model, car_release)
        session.add(new_car)
        session.commit()

    @staticmethod
    def Delete():
        delete_id = input('car_id delete = ')
        session.delete(session.query(Car).filter(Car.car_id == delete_id).first())
        session.commit()

    @staticmethod
    def Update():
        num = View.attribute_list(2)
        value = input('Attribute value to update = ')
        value2 = input('New attribute value = ')
        if num == 1:
            session.query(Car).filter(Car.car_id == value).update(
                {Car.car_id: value2})
        elif num == 2:
            session.query(Car).filter(Car.owner_id == value).update(
                {Car.owner_id: value2})
        elif num == 3:
            session.query(Car).filter(Car.car_model == value).update(
                {Car.car_model: value2})
        elif num == 4:
            session.query(Car).filter(Car.car_release == value).update(
                {Car.car_release: value2})
        session.commit()

    def print(self):
        return "<Car('%s', '%s', '%s', '%s')>" % (self.car_id, self.owner_id, self.car_model, self.car_release)

class TrafficViolation(db):
    __tablename__ = 'TrafficViolation'

    traffic_violation_id = Column(Integer, primary_key = True, nullable = False)
    traffic_violation_type = Column(String, nullable = False)
    price = Column(Integer, nullable = False)

    def __init__(self, id, type, price):
        self.traffic_violation_id = id
        self.traffic_violation_type = type
        self.price = price

    @staticmethod
    def Insert():
        traffic_violation_id = input('traffic_violation_id = ')
        traffic_violation_type = input('traffic_violation_type = ')
        price = input('price = ')
        new_traffic_violation = TrafficViolation(traffic_violation_id, traffic_violation_type, price)
        session.add(new_traffic_violation)
        session.commit()

    @staticmethod
    def Delete():
        delete_id = input('traffic_violation_id delete = ')
        session.delete(session.query(TrafficViolation).filter(TrafficViolation.traffic_violation_id == delete_id).first())
        session.commit()

    @staticmethod
    def Update():
        num = View.attribute_list(3)
        value = input('Attribute value to update = ')
        value2 = input('New attribute value = ')
        if num == 1:
            session.query(TrafficViolation).filter(TrafficViolation.traffic_violation_id == value).update({TrafficViolation.traffic_violation_id: value2})
        elif num == 2:
            session.query(TrafficViolation).filter(TrafficViolation.traffic_violation_type == value).update({TrafficViolation.traffic_violation_type: value2})
        elif num == 3:
            session.query(TrafficViolation).filter(TrafficViolation.price == value).update({TrafficViolation.price: value2})
        session.commit()

    def print(self):
        return "<TrafficViolation('%s', '%s', '%s')>" % (self.traffic_violation_id, self.traffic_violation_type, self.price)

class Department(db):
    __tablename__ = 'Department'

    department_id = Column(Integer, primary_key = True, nullable = False)
    department_address = Column(String, nullable = False)

    def __init__(self, id, address):
        self.department_id = id
        self.department_address = address

    @staticmethod
    def Insert():
        department_id = input('department_id = ')
        department_address = input('department_address = ')
        new_department = Department(department_id, department_address)
        session.add(new_department)
        session.commit()

    @staticmethod
    def Delete():
        delete_id = input('department_id delete = ')
        session.delete(
            session.query(Department).filter(Department.department_id == delete_id).first())
        session.commit()

    @staticmethod
    def Update():
        num = View.attribute_list(4)
        value = input('Attribute value to update = ')
        value2 = input('New attribute value = ')
        if num == 1:
            session.query(Department).filter(Department.department_id == value).update({Department.department_id: value2})
        elif num == 2:
            session.query(Department).filter(Department.department_address == value).update({Department.department_address: value2})
        session.commit()

    def print(self):
        return "<Department('%s', '%s')>" % (self.department_id, self.department_address)

class Policeman(db):
    __tablename__ = 'Policeman'

    policeman_id = Column(Integer, primary_key = True, nullable = False)
    policeman_name = Column(String, nullable = False)
    policeman_surname = Column(String, nullable = False)
    policeman_rank = Column(String, nullable = False)
    department_id = Column(Integer, ForeignKey(Department.department_id), nullable = False)

    def __init__(self, id, name, surname, rank, department):
        self.policeman_id = id
        self.policeman_name = name
        self.policeman_surname = surname
        self.policeman_rank = rank
        self.department_id = department

    @staticmethod
    def Insert():
        policeman_id = input('policeman_id = ')
        policeman_name = input('policeman_name = ')
        policeman_surname = input('policeman_surname = ')
        policeman_rank = input('policeman_rank = ')
        department_id = input('department_id = ')
        new_policeman = Policeman(policeman_id, policeman_name, policeman_surname, policeman_rank, department_id)
        session.add(new_policeman)
        session.commit()

    @staticmethod
    def Delete():
        delete_id = input('policeman_id delete = ')
        session.delete(session.query(Policeman).filter(Policeman.policeman_id == delete_id).first())
        session.commit()

    @staticmethod
    def Update():
        num = View.attribute_list(5)
        value = input('Attribute value to update = ')
        value2 = input('New attribute value = ')
        if num == 1:
            session.query(Policeman).filter(Policeman.policeman_id == value).update({Policeman.policeman_id: value2})
        elif num == 2:
            session.query(Policeman).filter(Policeman.policeman_name == value).update({Policeman.policeman_name: value2})
        elif num == 3:
            session.query(Policeman).filter(Policeman.policeman_surname == value).update({Policeman.policeman_surname: value2})
        elif num == 4:
            session.query(Policeman).filter(Policeman.policeman_rank == value).update({Policeman.policeman_rank: value2})
        elif num == 5:
            session.query(Policeman).filter(Policeman.department_id == value).update({Policeman.department_id: value2})
        session.commit()

    def print(self):
        return "<Policeman('%s', '%s', '%s', '%s', '%s')>" % (self.policeman_id, self.policeman_name, self.policeman_surname, self.policeman_rank, self.department_id)

class HeadOfDepartment(db):
    __tablename__ = 'HeadOfDepartment'

    head_id = Column(Integer, ForeignKey(Department.department_id), primary_key=True, nullable=False)
    head_name = Column(String, nullable=False)
    head_surname = Column(String, nullable=False)
    head_rank = Column(String, nullable=False)

    def __init__(self, id, name, surname, rank):
        self.head_id = id
        self.head_name = name
        self.head_surname = surname
        self.head_rank = rank

    @staticmethod
    def Insert():
        head_id = input('head_id = ')
        head_name = input('head_name = ')
        head_surname = input('head_surname = ')
        head_rank = input('head_rank = ')
        new_head = HeadOfDepartment(head_id, head_name, head_surname, head_rank)
        session.add(new_head)
        session.commit()

    @staticmethod
    def Delete():
        delete_id = input('head_id delete = ')
        session.delete(session.query(HeadOfDepartment).filter(HeadOfDepartment.head_id == delete_id).first())
        session.commit()

    @staticmethod
    def Update():
        num = View.attribute_list(6)
        value = input('Attribute value to update = ')
        value2 = input('New attribute value = ')
        if num == 1:
            session.query(HeadOfDepartment).filter(HeadOfDepartment.head_id == value).update({HeadOfDepartment.head_id: value2})
        elif num == 2:
            session.query(HeadOfDepartment).filter(HeadOfDepartment.head_name == value).update(
                {HeadOfDepartment.head_name: value2})
        elif num == 3:
            session.query(HeadOfDepartment).filter(HeadOfDepartment.head_surname == value).update(
                {HeadOfDepartment.head_surname: value2})
        elif num == 4:
            session.query(HeadOfDepartment).filter(HeadOfDepartment.head_rank == value).update(
                {HeadOfDepartment.head_rank: value2})
        session.commit()

    def print(self):
        return "<HeadOfDepartment('%s', '%s', '%s', '%s')>" % (self.head_id, self.head_name, self.head_surname, self.head_rank)

class Protocol(db):
    __tablename__ = 'Protocol'

    protocol_id = Column(Integer, primary_key=True, nullable=False)
    policeman_id = Column(Integer, ForeignKey(Policeman.policeman_id), nullable=False)
    rule_breaker_id = Column(Integer, ForeignKey(RuleBreaker.rule_breaker_id), nullable=False)
    traffic_violation_id = Column(Integer, ForeignKey(TrafficViolation.traffic_violation_id), nullable=False)

    def __init__(self, id, policeman, rule_breaker, traffic_violation):
        self.protocol_id = id
        self.policeman_id = policeman
        self.rule_breaker_id = rule_breaker
        self.traffic_violation_id = traffic_violation

    @staticmethod
    def Insert():
        new_protocol_id = input('protocol_id = ')
        new_policeman_id = input('policeman_id = ')
        new_rule_breaker_id = input('rule_breaker_id = ')
        new_traffic_violation_id = input('traffic_violation_id = ')
        new_protocol = Protocol(new_protocol_id, new_policeman_id, new_rule_breaker_id, new_traffic_violation_id)
        session.add(new_protocol)
        session.commit()

    @staticmethod
    def Delete():
        delete_id = input('protocol_id delete = ')
        session.delete(session.query(Protocol).filter(Protocol.protocol_id == delete_id).first())
        session.commit()

    @staticmethod
    def Update():
        num = View.attribute_list(7)
        value = input('Attribute value to update = ')
        value2 = input('New attribute value = ')
        if num == 1:
            session.query(Protocol).filter(Protocol.protocol_id == value).update(
                {Protocol.protocol_id: value2})
        elif num == 2:
            session.query(Protocol).filter(Protocol.policeman_id == value).update(
                {Protocol.policeman_id: value2})
        elif num == 3:
            session.query(Protocol).filter(Protocol.rule_breaker_id == value).update(
                {Protocol.rule_breaker_id: value2})
        elif num == 4:
            session.query(Protocol).filter(Protocol.traffic_violation_id == value).update(
                {Protocol.traffic_violation_id: value2})
        session.commit()

    def print(self):
        return "<Protocol('%s', '%s', '%s', '%s')>" % (self.protocol_id, self.policeman_id, self.rule_breaker_id, self.traffic_violation_id)

engine = create_engine(URL(**DATABASE))
db.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def show_table(number):
    flag = 0
    table = 0
    while flag == 0:
        if number == 1:
            table = View.list()
            flag = 1
        elif number == 2:
            table += 1
            if table == 7:
                flag = 1
        if table == 1:
            print("table: RuleBreaker")
            for row in session.query(RuleBreaker):
                print(row.print())
            print("\n")
        elif table == 2:
            print("table: Car")
            for row in session.query(Car):
                print(row.print())
            print("\n")
        elif table == 3:
            print("table: TrafficViolation")
            for row in session.query(TrafficViolation):
                print(row.print())
            print("\n")
        elif table == 4:
            print("table: Policeman")
            for row in session.query(Policeman):
                print(row.print())
            print("\n")
        elif table == 5:
            print("table: Department")
            for row in session.query(Department):
                print(row.print())
            print("\n")
        elif table == 6:
            print("table: HeadOfDepartment")
            for row in session.query(HeadOfDepartment):
                print(row.print())
            print("\n")
        elif table == 7:
            print("table: Protocol")
            for row in session.query(Protocol):
                print(row.print())
            print("\n")


